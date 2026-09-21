"""One-level pose bundles for Observer.

The observer_bundle contains eight pose bundles and a Walk clock bundle.
Each child contains only attributes, never another bundle. Appearance and mesh construction remain
Observer modifier settings; animation helpers resolve expressions and presets
into the explicit pose values below.

Angles are radians, positions are in meters at final character size.
The character faces +Y, with +Z up; its anatomical left side is -X.
Root transforms affect the entire character; body transforms
move the upper assembly independently of the feet. Arm locations are shoulder
anchors. Foot locations are in character space before the root transform.
Hand twist and finger angles retain the old Hand group's conventions.
Eyelid tilt is a direct rotation about Y, replacing the angryness control.

Call demo() to build the Observer modifier and its construction groups.
ObserverBundles reads pose values from the input geometry. The generated mesh
retains the resolved pose bundle. A modifier placed before Observer can edit
its pose using ObserverBundles, then update() and output its geometry.
Only resolution and appearance remain exposed on Observer. Walk cycles and
hand presets are intentionally left to animation helpers.

build_animation() also builds Obs Anim Walk. Time is in seconds and Speed in
meters per second (one Blender unit is treated as one meter). Pace (0..1)
controls a smooth walking-to-running profile. Step Length is the distance per
complete cycle; cadence is Speed / Step Length. Every gait closure takes Phase,
Step Length and Step Height. Custom closures retain their captured style settings.
Manual phase and distance use current inputs for all elapsed time. Simulation
integrates time, phase, distance and displacement per frame, starting at Time.
Each part's influence is Factor multiplied by its own factor.
The Walk clock is never blended; its sinusoids use the derived cycle phase.
Read the shared clock in a later modifier with:

    bundles = ObserverBundles(geometry)
    walk = bundles["Walk"]
    arm = bundles["Right Arm"]
    arm["Forward"] = Float(0.8) + walk["Right Amplitude"] * 0.1
    bundles.update()

Mesh construction adapted from demos/observer.py, copyright (c) 2025 Alain
Bernard, under the GNU General Public License version 3, as in this project.
"""

from copy import deepcopy
import math
from math import radians
import bpy

from geonodes import *

CLOSURES_NAME = "Closures"

# ====================================================================================================
# Body structures
# ====================================================================================================

# Main Bundle containing body part bundles

OBS_BUNDLE_SIGNATURE = {
    "Location"    : Bundle,
    "Body"        : Bundle,
    "Head"        : Bundle,
    "Left Arm"    : Bundle,
    "Right Arm"   : Bundle,
    "Left Hand"   : Bundle,
    "Right Hand"  : Bundle,
    "Left Leg"    : Bundle,
    "Right Leg"   : Bundle,
    "Walk"        : Bundle,
    "Cloth"       : Bundle,
    CLOSURES_NAME : Bundle,
}

# Animated location

LOCATION_DEFAULTS = {
    "Time"      : 0.0,              # Simulated time
    "Location"  : (0.0, 0.0, 0.0),  # Simulated location
    "Distance"  : 0.0,              # Simulated distance
    "Direction" : 0.0,              # Current direction
    "Phase"     : 0.0,              # Current phase
}

BODY_DEFAULTS = {
    "Body Location": (0.0, 0.0, 0.0),
    "Body Rotation": (0.0, 0.0, 0.0),
}

# Head default settings

HEAD_DEFAULTS = {
    "Horizontal"            : 0.0,
    "Vertical"              : 0.0,
    "Lateral"               : 0.0,
    "Eyes Horizontal"       : 0.0, 
    "Eyes Vertical"         : 0.0,
    "Left Eye Horizontal"   : 0.0,
    "Left Eye Vertical"     : 0.0,
    "Right Eye Horizontal"  : 0.0,
    "Right Eye Vertical"    : 0.0,
    "Eyelid"                : 0.25,
    "Left Eyelid"           : 0.0,
    "Right Eyelid"          : 0.0,
    "Left Eyelid Tilt"      : 0.0,
    "Right Eyelid Tilt"     : 0.0,
}

# Arm default settings

ARM_DEFAULTS = {
    "Lateral"       : 0.0,
    "Forward"       : 0.0,
    "Elbow"         : 0.0,
    "Hand Flap"     : 0.0,
    "Hand Twist"    : 0.0,
}

# Foot default settings

FOOT_DEFAULTS = {
    "Location"  : (0.0, 0.0, 0.0),
    "Tilt"      : 0.0,
    "Twist"     : 0.0,
    "Tiptoe"    : 0.0,
}

# Foot is controlled by legs

LEG_DEFAULTS = {f"Foot {name}": value for name, value in FOOT_DEFAULTS.items()}

# Shared clock: Time is in seconds, Speed in m/s, Walk Distance in meters.

WALK_DEFAULTS = {
    "Time"              : 0.0,
    "Speed"             : 0.5,
    "Pace"              : 0.5,
    "Left Amplitude"    : 0.0,
    "Right Amplitude"   : 0.0,
    "Walk Distance"     : 0.0,
}

# Normalized left-side gait. Step Length is the distance per full cycle, in meters.
# Foot Location includes the left foot's spacing; the animator mirrors X for right.
PACE_SIGNATURE = ({
        "Phase"             : Float,
        "Step Length"       : Float,
        "Step Height"       : Float,
    },{
        "Foot Location"     : Vector,
        "Foot Tilt"         : Float,
        "Body Height"       : Float, 
        "Body Forward Tilt" : Float, 
        "Body Side Tilt"    : Float,
        "Arm Forward"       : Float, 
        "Arm Elbow"         : Float,
    })

CLOTH_DEFAULTS = {
    "Seed"              : 0,
    "Amplitude"         : 0.0,
    "Walk Amplitude"    : 0.0,
    "Noise Scale"       : 3.0,
    "Speed"             : 1.0,
}

# ----------------------------------------------------------------------------------------------------
# Hand
# ----------------------------------------------------------------------------------------------------

FINGER_NAMES = ('Thumb',) + tuple(f"Finger {i}" for i in range(1, 5))

LATERAL = 'Lateral'
FOLD    = 'Fold'

FINGER_POSE_SIG = {
    LATERAL : Float,
    FOLD    : Vector,
}

HAND_POSE_SIG = {**{f"{name} {i}" : value for name, value in FINGER_POSE_SIG.items() for i in range(5)}}

# Finger : [Lateral, Fold.X, Fold.Y, Fold.Z]
# Finger i copy last finger available
# Angles in degrees

HAND_POSE_PRESETS = {
    'Flat':     [[0, 0, 0, 0],      [0, 0, 0, 0]],
    'Rest' :    [[-3, 10, 10, 10],  [1, 5, 5, 5]],
    'Victory':  [[-25, 4, 35, 35],  [15, 0, 0, 0], [-15, 0, 0, 0], [0, 80, 80, 80]],
    'Point At': [[-25, 0, 30, 45],  [0, 80, 80, 80]],
    'Fist':     [[3, 35, 55, 48],   [0, 90, 90, 90]],
    'Handle':   [[23, 47, 43, 44],  [0, 60, 60,60]],
    'Thumb Up': [[3, 35, 55, 48],   [0, 90, 90, 90]],
}
HAND_DEFAULTS = {
    'Lateral 0': radians(-3), 'Fold 0': (radians(10), radians(10), radians(10)),
    'Lateral 1': radians(1),  'Fold 1': (radians(5), radians(5), radians(5)),
    'Lateral 2': radians(1),  'Fold 2': (radians(5), radians(5), radians(5)),
    'Lateral 3': radians(1),  'Fold 3': (radians(5), radians(5), radians(5)),
    'Lateral 4': radians(1),  'Fold 4': (radians(5), radians(5), radians(5)),
}

HAND_POSE_FUNC = ({'Factor': Float}, HAND_POSE_SIG)

# ----------------------------------------------------------------------------------------------------
# Observer
# ----------------------------------------------------------------------------------------------------

OBSERVER_BUNDLE_DEFAULTS = {
    "Cloth"         : deepcopy(CLOTH_DEFAULTS),
    "Location"      : deepcopy(LOCATION_DEFAULTS),
    "Walk"          : deepcopy(WALK_DEFAULTS),
    "Body"          : deepcopy(BODY_DEFAULTS),
    "Head"          : deepcopy(HEAD_DEFAULTS),
    "Left Arm"      : deepcopy(ARM_DEFAULTS),
    "Right Arm"     : deepcopy(ARM_DEFAULTS),
    "Left Hand"     : deepcopy(HAND_DEFAULTS),
    "Right Hand"    : deepcopy(HAND_DEFAULTS),
    "Left Leg"      : deepcopy(LEG_DEFAULTS),
    "Right Leg"     : deepcopy(LEG_DEFAULTS),
}

#OBSERVER_BUNDLE_DEFAULTS["Left Arm"]["Location"] = (-0.375, 0.0, 1.25)
#OBSERVER_BUNDLE_DEFAULTS["Right Arm"]["Location"] = (0.375, 0.0, 1.25)
OBSERVER_BUNDLE_DEFAULTS["Left Leg"]["Foot Location"] = (-1.0 / 6.0, 0.0, 0.0)
OBSERVER_BUNDLE_DEFAULTS["Right Leg"]["Foot Location"] = (1.0 / 6.0, 0.0, 0.0)

# Retain the original public name for callers using create_pose/new_bundle.
POSE_DEFAULTS = OBSERVER_BUNDLE_DEFAULTS

# ----------------------------------------------------------------------------------------------------
# Observer dimensions
# ----------------------------------------------------------------------------------------------------

BODY_HEIGHT = 1.224
# Local body Z above which the coat stays fixed; influence grows toward the hem.
CLOTH_SWAY_START_Z = 0.8
HEAD_HEIGHT = 0.455
NECK_HEIGHT = HEAD_HEIGHT/5
HEAD_EYE_Z = 0.2*HEAD_HEIGHT

# BOUNDS

HEAD_INCL_MAX = math.radians(20)
HEAD_HRZ_MAX = math.radians(65)
HEAD_VRT_MAX = math.radians(40)
EYES_HRZ_MAX = math.radians(35)
EYES_VRT_MAX = math.radians(25)

# ====================================================================================================
# Hand pose utilities
# ====================================================================================================

# ----------------------------------------------------------------------------------------------------
# Get a preset pose
# ----------------------------------------------------------------------------------------------------

def get_preset_hand_pose(preset=None):
    """ Return a preset hand pose dict
    """
    
    if preset is None:
        preset = HAND_POSE_PRESETS['Flat']
    
    if isinstance(preset, str):
        preset = HAND_POSE_PRESETS[preset]
    
    hand_pose = {}
    for i in range(5):            
        if i >= len(preset):
            p = preset[-1]
        else:
            p = preset[i]
            
        hand_pose[LATERAL + f" {i}"] = radians(p[0])
        hand_pose[FOLD + f" {i}"] = (radians(p[1]), radians(p[2]), radians(p[3]))
                    
    return hand_pose

# ----------------------------------------------------------------------------------------------------
# Finger Angle inputs
# ----------------------------------------------------------------------------------------------------

def create_finger_inputs(i_finger=0):
    """ Create input sockets for a finger
    
    Returns
    -------
    - dict : finger pose
    """

    raw = {LATERAL: LATERAL, FOLD: FOLD}
    num = {LATERAL: f"{LATERAL} {i_finger}", FOLD: f"{FOLD} {i_finger}"}

    if i_finger is None:
        keys = raw
        names = raw

    #elif i_finger == 0:
    #    keys  = num
    #    names = raw

    else:
        keys  = num
        names = num
    
    """
    keys = {LATERAL: f"{LATERAL} {i_finger}", FOLD: f"{FOLD} {i_finger}"}
    if i_finger == 0:
        names = {LATERAL: LATERAL, FOLD: FOLD}
    else:
        names = keys
    """
        
    d = {}
    d[keys[LATERAL]] = Float.Angle(0, names[LATERAL], -pi, pi, shape='Single')
    d[keys[FOLD]]    = Vector.Euler(0, names[FOLD], shape='Single')

        
    return d

# ----------------------------------------------------------------------------------------------------
# Hand pose inputs
# ----------------------------------------------------------------------------------------------------

def create_hand_pose_inputs():
    """ Create input sockets for the hand
    
    Arguments
    ---------
    - is_thumb (bool = False) : thumb or finger
    - full (bool = False) : ask second fold

    Returns
    -------
    - dict : hande pose
    """
    
    params = {}
    for i in range(5):
        d = create_finger_inputs(i)
        params = {**params, **d}
                
    return params

# ----------------------------------------------------------------------------------------------------
# Hand pose closure
# ----------------------------------------------------------------------------------------------------

def create_hand_pose_func(pose0, pose1):
    """ Create a hande pose func (i.e. Closure)
    
    Arguments
    ---------
    - pose0 (dict) : start hand pose
    - pose1 (dict) : end hand pose
    """
    
    is_str0 = isinstance(pose0, str)
    is_str1 = isinstance(pose1, str)
    
    # ---------------------------------------------------------------------------
    # Constant function
    # ---------------------------------------------------------------------------
    
    if (is_str0 and is_str1) and (pose0 == pose1):
        pose = get_preset_hand_pose(pose0)
        with Closure() as func:
            factor = Float(1.0, "Factor")
            
            for k, v in pose.items():
                HAND_POSE_SIG[k](v).out(k)
                
            # Avoid warning for unusing factor
            factor.out("Factor")
                
        return func
    
    # ---------------------------------------------------------------------------
    # Actual function
    # ---------------------------------------------------------------------------

    if is_str0:
        pose0 = get_preset_hand_pose(pose0)
        
    if is_str1:
        pose1 = get_preset_hand_pose(pose1)
    
    with Closure() as func:
        factor = Float(1.0, "Factor")
        
        final = {}
        
        for k, v in pose0.items():
            final[k] = HAND_POSE_SIG[k].Mix(v, pose1[k], factor=factor, clamp_factor=True)._lc(k)
            final[k].out(k)
        
    return func

# =============================================================================================================================
# Bundles management
# =============================================================================================================================

# -----------------------------------------------------------------------------------------------------------------------------
# Functions
# -----------------------------------------------------------------------------------------------------------------------------

def get_observer_bundles(geometry):
    node = G().obs_bundle_parameters(geometry).node
    return {name: node[name] for name in OBS_BUNDLE_SIGNATURE.keys()}

def set_observer_bundles(geometry, bundles):
    obs_bundle = Bundle.Combine(bundles)
    geometry.set_bundle(obs_bundle)
    return geometry

def get_bundle_parameters(bundles, name):
    signature = OBSERVER_BUNDLE_DEFAULTS[name]
    bundle = bundles[name]
    node = bundle.separate(signature=signature)
    return {key: node[key] for key in signature}

def set_bundle_parameters(bundles, name, parameters):
    bundle = Bundle.Combine(parameters)
    bundles[name] = bundle
    return bundle

# -----------------------------------------------------------------------------------------------------------------------------
# Bundle management wrapper class
# -----------------------------------------------------------------------------------------------------------------------------

class BundleParams:
    def __init__(self, observer_bundles, name, bundle_socket, factor):
        self.observer_bundles = observer_bundles
        self.name = name
        self._bundle_socket = bundle_socket
        self.factor = factor
        self._parameters = None

    @property
    def is_dynamic(self):
        return self.name in [CLOSURES_NAME]

    @property
    def signature(self):
        if self.is_dynamic:
            return {}
        else:
            return OBSERVER_BUNDLE_DEFAULTS[self.name]

    @property
    def bundle_socket(self):
        if self._parameters is not None:
            with Layout(f"Combine Bundle {self.name}"):
                new_values = {}
                for key in self._parameters.keys():
                    v0 = self._initial_values[key]
                    v1 = self._parameters[key]
                    if self.factor is None:
                        new_values[key] = v1
                    else:
                        new_values[key] = v0.mix(v1, factor=self.factor)

                #self._bundle_socket = Bundle.Combine(**self._parameters)
                self._bundle_socket = Bundle.Combine(**new_values)

        return self._bundle_socket

    @bundle_socket.setter
    def bundle_socket(self, bundle):
        self._bundle_socket = bundle
        self._parameters = None

    @property
    def parameters(self):
        if self.is_dynamic:
            raise RuntimeError(
                f"Bundle '{self.name}' is dynamic: parameters is unavailable. "
                "Use get_dynamic() and set_dynamic() instead."
            )
        if self._parameters is None:
            node = self._bundle_socket.separate(signature=self.signature)
            self._parameters = {key: node[key] for key in self.signature.keys()}
            self._initial_values = {key: type(value)(value) for key, value in self._parameters.items()}

        return self._parameters

    def __getitem__(self, name):
        return self.parameters[name]

    def __setitem__(self, name, value):
        self.parameters[name] = value

    def replace_parameters(self, **parameters):
        """Replace a complete static bundle without reading unused old values."""
        if self.is_dynamic or set(parameters) != set(self.signature):
            raise ValueError(f"Expected all parameters of static bundle '{self.name}'")
        if self.factor is None:
            self._bundle_socket = Bundle.Combine(parameters)
            self._parameters = None
        else:
            self.parameters.update(parameters)

    def set_dynamic(self, name, socket):
        self._bundle_socket.store_item(name, socket)

    def get_dynamic(self, name, socket_type):
        return self._bundle_socket.get_item(name, socket_type=socket_type)

# -----------------------------------------------------------------------------------------------------------------------------
# All bundles management wrapper class
# -----------------------------------------------------------------------------------------------------------------------------

class ObserverBundles:
    """Read/edit pose bundles, optionally exposing global and per-part influence.

    Location stores accumulated motion; Walk stores shared animation metadata.
    Both bypass influence mixing.
    Head and hand factors are available for helpers that animate those parts;
    Obs Anim Walk itself leaves their local parameters unchanged.
    """
    def __init__(self, geometry, use_factor=True, per_bundle_factors=False):

        is_bundles = geometry.SOCKET_TYPE == 'BUNDLE'
        if is_bundles:
            self.geometry = None
            self.bundles = geometry
        else:
            self.geometry = geometry
            self.bundles = get_observer_bundles(self.geometry)

        if use_factor:
            self.factor = Float(1.0, "Factor", 0, 1)
        else:
            self.factor = None

        self.parameters = {
            name: BundleParams(self, name, self.bundles[name],
                               None if name in ("Location", "Walk", CLOSURES_NAME) else self.factor)
            for name in self.names
        }

        if per_bundle_factors:
            with Panel("Influence"):
                for name in self.names:
                    if name not in ("Location", "Walk", CLOSURES_NAME):
                        self.parameters[name].factor = self.factor * Float.Factor(
                            1.0, f"{name} Factor", 0.0, 1.0,
                        )

    @property
    def names(self):
        return OBS_BUNDLE_SIGNATURE.keys()

    def __getitem__(self, name):
        return self.parameters[name]

    def eyes_location(self):
        """Return the eye midpoint at reference size, before Observer's UI Scale."""
        with Layout("Eyes Location"):
            # Read the effective pose, including pending edits and influence factors.
            #bundles = {
            #    name: self[name].bundle_socket
            #    for name in ("Body", "Head")
            #}
            #body = get_bundle_parameters(bundles, "Body")
            #head = get_bundle_parameters(bundles, "Head")

            oloc = self["Location"]
            body = self["Body"]
            head = self["Head"]

            eye_offset = Vector((
                0.0, 0.3 * HEAD_HEIGHT,
                NECK_HEIGHT + HEAD_HEIGHT / 2 + HEAD_EYE_Z,
            ))
            head_rotation = Rotation.FromEuler(Vector((
                head["Vertical"], -head["Lateral"], head["Horizontal"],
            )))
            position = Vector((0.0, 0.0, BODY_HEIGHT)) + head_rotation @ eye_offset
            position = body["Body Location"] + Rotation.FromEuler(body["Body Rotation"]) @ position
            return oloc["Location"] + Rotation.FromEuler(Vector((0, 0, oloc["Direction"]))) @ position

    def update(self, geometry=None):
        geo = self.geometry if geometry is None else geometry
        if geo is not None:
            return set_observer_bundles(geo, {name: self.parameters[name].bundle_socket for name in self.names})
        else:
            return None

# =============================================================================================================================
# Main
# =============================================================================================================================

def build_animation():

    # ----------------------------------------------------------------------------------------------------
    # Extract the sub-bundles from Geometry bundle
    # ----------------------------------------------------------------------------------------------------

    with GeoNodes("Obs Bundle Parameters", is_group=True):
        geometry = Geometry()

        with Layout("Read Observer Bundle"):
            obs_bundle = geometry.get_bundle(remove=False)
            # Observer bundles are either all present or all absent.
            exists = obs_bundle.get_item("Body", socket_type='BUNDLE').exists
            bundles = obs_bundle.separate(signature=OBS_BUNDLE_SIGNATURE)

        for name in OBS_BUNDLE_SIGNATURE:
            defaults = OBSERVER_BUNDLE_DEFAULTS.get(name, {})
            with Layout(f"Bundle '{name}'"):
                Bundle.Switch(exists, Bundle.Combine(defaults),
                              bundles[name]).out(name)

    # ----------------------------------------------------------------------------------------------------
    # Add a dynamic closure in the bundle of closures
    # ----------------------------------------------------------------------------------------------------

    with GeoNodes("Obs Bundle Add Closure", is_group=True):
        geometry = Geometry()
        bundles = ObserverBundles(geometry, use_factor=False)
        name = String("", "Name")
        closure = Closure(None, "Closure")
        bundles[CLOSURES_NAME].set_dynamic(name, closure)
        bundles.update()
        geometry.out()

    # ====================================================================================================
    # Animation modifiers
    # ====================================================================================================

    # ----------------------------------------------------------------------------------------------------
    # Lab Coat Animation
    # ----------------------------------------------------------------------------------------------------

    with GeoNodes("Obs Anim Lab Coat"):
        geometry = Geometry()
        bundles = ObserverBundles(geometry, use_factor=False)
        seed = Integer(0, "Seed")
        amplitude = Float(0.1, "Amplitude", 0.0, 1.0)
        walk_amplitude = Float(0.1, "Walk Amplitude", 0.0, 1.0)
        noise_scale = Float(3.0, "Noise Scale", 0.0)
        speed = Float(1.0, "Speed", 0.0)

        with Layout("Cloth Parameters"):
            cloth = bundles["Cloth"]
            cloth.replace_parameters(**{
                "Seed": seed, "Amplitude": amplitude,
                "Walk Amplitude": walk_amplitude,
                "Noise Scale": noise_scale, "Speed": speed,
            })
            bundles.update().out()

    # ----------------------------------------------------------------------------------------------------
    # Body Animation
    # ----------------------------------------------------------------------------------------------------

    with GeoNodes("Obs Anim Body"):
        geometry = Geometry()
        bundles = ObserverBundles(geometry, use_factor=False)

        controls = {}
        for name in ("Height", "Rotation"):
            with Panel(name):
                factor = Float.Factor(1.0, "Factor", 0.0, 1.0)
                relative = Boolean(True, "Relative")
                if name == "Height":
                    value = Float(0.0, "Value")
                    amplitude = Float(0.0, "Amplitude")
                else:
                    value = Vector.Euler((0, 0, 0), "Value")
                    amplitude = Vector.Euler((0, 0, 0), "Amplitude")
                leg_walk = Boolean(True, "Leg Walk", tip=(
                    "Synchronize with the left leg of the current Walk; "
                    "disable for two oscillations per walk cycle."
                ))
                controls[name] = (factor, relative, value, amplitude, leg_walk)

        with Layout("Walk Drivers"):
            phase = bundles["Location"]["Phase"]
            leg_sine = (phase * (2*pi)).sin()
            body_sine = (phase * (4*pi)).sin()

        body = bundles["Body"]
        for name, (factor, relative, value, amplitude, leg_walk) in controls.items():
            with Layout(name):
                driver = Float(body_sine).switch(leg_walk, leg_sine)
                computed_value = value + amplitude * driver
                if name == "Height":
                    location = body["Body Location"]
                    current = location.z
                    target = Float(computed_value).switch(relative, current + computed_value)
                    height = Float(current).mix(target, factor=factor)
                    body["Body Location"] = Vector((location.x, location.y, height))
                else:
                    current = body["Body Rotation"]
                    target = Vector(computed_value).switch(relative, current + computed_value)
                    body["Body Rotation"] = Vector(current).mix(target, factor=factor)

        with Layout("Write Pose"):
            bundles.update().out()


    # ====================================================================================================
    # Walk Animation
    # ====================================================================================================

    # ----------------------------------------------------------------------------------------------------
    # Create a Walk Closure
    # ----------------------------------------------------------------------------------------------------

    with GeoNodes("Obs Closure Create Walk", is_group=True):
        
        with Panel("Duration"):
            step_duration = Float.Factor(.6, "Step Duration", 0.1, 0.95)
            step_before = Float.Factor(0.5, "Before Duraion", 0, 1)
            
        with Panel("Foot Motion"):
            foot_tilt = Float.Angle(1, "Foot Angle", 0, pi/2)
            
        with Panel("Body"):
            foot_space = Float(0.4, "Foot Space")
            side_amplitude = Float.Angle(0.05, "Side Amplitude", 0, pi/2)
            forward_tilt = Float.Angle(0.05, "Forward Tilt", -pi/2, pi/2)
            forward_amplitude = Float.Angle(0.02, "Forward Amplitude", 0, pi/2)
            body_bounce = Float.Factor(0.1, "Body Bounce", 0, 1)

        with Panel("Arms"):
            elbow = Float.Angle(0.0, "Elbow", 0, pi)
            arm_amplitude = Float.Angle(0.4, "Forward Amplitude", 0, pi/2)
            
        with Layout("Durations"):
            dur1 = step_duration
            dur02 = (1.0 - dur1)._lc("Durations 0 + 2")
            dur0 = (dur02 * step_before)._lc("Duration 0")
            dur01 = (dur0 + dur1)._lc("Duration 0 + 1")
            
        with Closure() as walk_func:
            
            phase = Float(0.0, "Phase")
            step_length = Float(1.0, "Step Length", 0.0,
                                tip="Distance traveled during one complete cycle, in meters")
            step_height = Float(0.15, "Step Height", 0.0)
            t = phase % 1.0
            t._lc("t")
            
            with Layout("Factors"):        
                fac1 = t.map_range(dur0, dur01)._lc("Factor 1")
                
            with Layout("Body Location"):
                y_body = step_length*t
                
            with Layout("Foot Location"):
                ry = step_length/2
                rz = step_height
                ag = fac1*pi
                y_foot = ry - ry*ag.cos()
                z_foot = rz*ag.sin()
                
            with Layout("Foot Tilt"):
                tilt = fac1.map_range(to_min=foot_tilt, to_max=-foot_tilt) 
                
            y_foot -= y_body

            with Layout("Body Motion"):
                # Phase describes the left leg (-X). Lean left at phase 0,
                # right at phase 0.5: one lateral oscillation per full cycle.
                side = -side_amplitude * (2*pi*t).cos()
                # Positive forward settings lean toward +Y (negative X rotation).
                # Forward motion repeats at each step, twice per cycle.
                forward = -forward_tilt - forward_amplitude * (4*pi*t).cos()
                height = step_height * body_bounce * (1 - (4*pi*t).cos()) / 2

            with Layout("Arm Motion"):
                # Left arm swings opposite the left leg; shift phase by 0.5 for right.
                arm_forward = arm_amplitude * (2*pi*t).sin()

            # Outing
            Vector((-foot_space/2, y_foot, z_foot)).out("Foot Location")                
            tilt.out("Foot Tilt")
            forward.out("Body Forward Tilt")
            side.out("Body Side Tilt")
            height.out("Body Height")
            arm_forward.out("Arm Forward")
            elbow.out("Arm Elbow")

        walk_func.out("Walk")

    # ----------------------------------------------------------------------------------------------------
    # Utility : get a Walk Closure
    # ----------------------------------------------------------------------------------------------------

    with GeoNodes("Obs Closure Get Walk", is_group=True):

        geometry = Geometry()
        bundles = ObserverBundles(geometry, use_factor=False)

        speed = Float(2.0, "Speed", 0.0, 10.0, tip="Movement speed in meters per second")
        pace = Float.Factor(0.5, "Pace", 0.0, 1.0,
                            tip="Gait style and step amplitude")

        foot_spacing = Float(1.5, "Foot Spacing", 0.0)
        distance_scale = Float(1.0, "Distance Scale",
                            tip="Translation multiplier; zero walks in place")
        
        closure_name = String("", "Closure Name",
                            tip="Registered gait closure; empty uses standard Walk")


        with Layout("Pace Settings"):
            speed = gnmath.max(speed, 0.0)._lc("Speed")
            pace = pace.clamp(0.0, 1.0)._lc("Pace")
            # Smooth progression from short walking steps to a running gait.
            style = pace * pace * (3.0 - 2.0 * pace)
            step_length = (style * 5.0)._lc("Step Length")
            step_height = (style * style * 0.45)._lc("Step Height")
            cadence = (speed / gnmath.max(step_length, 0.000001)).switch(step_length.equal(0), 0.0)
            #cycle_phase = (time * cadence._lc("Candence"))._lc("Cycle Phase")

        with Layout("Default Walk Closure"):
            default = G().obs_closure_create_walk(
                step_duration=style.map_range(to_min=0.3, to_max=0.8),
                foot_angle=style * 0.8,
                foot_space=1.0 / 3.0,
                side_amplitude=style * 0.07,
                forward_tilt=style * 0.25,
                body_bounce=style.map_range(to_min=0.1, to_max=0.35),
                elbow=style * (pi/2),
            ).node
            default["Body > Forward Amplitude"] = style * 0.04
            default["Arms > Forward Amplitude"] = style * 0.8
            walk_closure = default["Walk"]

        with Layout("Select Animation Closure"):
            custom = bundles[CLOSURES_NAME].bundle_socket.get_item(closure_name, socket_type='CLOSURE')
            use_custom = closure_name.length() > 0
            walk_closure = walk_closure.switch(use_custom & custom.exists, custom)

        walk_closure.out("Walk")
        speed.out("Speed")
        cadence.out("Cadence")
        step_length.out("Step Length")
        step_height.out("Step Height")
        foot_spacing.out("Foot Spacing")

    # ----------------------------------------------------------------------------------------------------
    # Utility : Apply a walk Closure
    # ----------------------------------------------------------------------------------------------------

    with GeoNodes("Obs Closure Apply Walk", is_group=True):

        geometry = Geometry()
        bundles = ObserverBundles(geometry, per_bundle_factors=False)

        walk_func = Closure(None, "Walk")
        step_length = Float(0, "Step Length")
        step_height = Float(0, "Step Height")
        foot_spacing = Float(1.5, "Foot Spacing", 0.0)

        body = bundles["Body"]
        oloc = bundles["Location"]

        cycles = {}
        for side in ("Left", "Right"):
            with Layout(f"{side} Leg"):
                side_phase = oloc["Phase"] + (0.0 if side == "Left" else 0.5)
                phase01 = (side_phase % 1).switch(
                    side_phase < 0, 1 - ((-side_phase) % 1),
                )
                cycle = walk_func.evaluate(
                    signature=PACE_SIGNATURE, phase=phase01,
                    step_length=step_length, step_height=step_height,
                ).node
                cycles[side] = cycle
                leg = bundles[f"{side} Leg"]
                # Add gait displacement to the incoming resting foot position.
                rest = OBSERVER_BUNDLE_DEFAULTS[f"{side} Leg"]["Foot Location"]
                mirror = 1.0 if side == "Left" else -1.0
                location = cycle["Foot Location"] * Vector((mirror * foot_spacing, 1.0, 1.0))
                leg["Foot Location"] = leg["Foot Location"] + location - Vector(rest)
                leg["Foot Tilt"] = leg["Foot Tilt"] + cycle["Foot Tilt"]

        with Layout("Arms"):
            for side in ("Left", "Right"):
                arm = bundles[f"{side} Arm"]
                arm["Forward"] = arm["Forward"] + cycles[side]["Arm Forward"]
                arm["Elbow"] = arm["Elbow"] + cycles[side]["Arm Elbow"]

        with Layout("Body"):
            left = cycles["Left"]
            height = left["Body Height"]
            front = left["Body Forward Tilt"]
            lateral = left["Body Side Tilt"]
            body["Body Location"] = body["Body Location"] + Vector((0.0, 0.0, height))
            body["Body Rotation"] = body["Body Rotation"] + Vector((front, lateral, 0.0))

        bundles.update()
        geometry.out()       

    # ----------------------------------------------------------------------------------------------------
    # Walk driven by direction and speed
    # ----------------------------------------------------------------------------------------------------

    with GeoNodes("Obs Anim Walk"):

        geometry = Geometry()
        anim_factor = Float(1.0, "Factor", 0, 1)

        with Panel("Speed"):
            direction = Float.Angle(0.0, "Direction",
                            tip="Heading around Z; zero faces +Y, or offsets the curve heading")

            node = G().obs_closure_get_walk(geometry).link_inputs().node
            walk_func = node.walk
            speed = node.speed
            cadence = node.cadence
            step_length = node.step_length
            step_height = node.step_height
            foot_spacing = node.foot_spacing

        for sim in simulation(geometry=geometry):
            bundles = ObserverBundles(sim.geometry, use_factor=False)
            bundles.factor = anim_factor

            oloc = bundles["Location"]

            dt = sim.delta_time*anim_factor

            delta_distance = speed * dt
            oloc["Time"] += dt
            oloc["Phase"] += cadence * dt
            oloc["Distance"] += delta_distance

            forward = Rotation.FromEuler(Vector((0, 0, direction))) @ Vector((0.0, 1.0, 0.0))
            oloc["Location"] += forward * (distance_scale * delta_distance)
            oloc["Direction"] = direction

            sim.geometry = bundles.update()

        geometry = G().obs_closure_apply_walk(sim.geometry,
                        factor = anim_factor,
                        walk = walk_func,
                        step_length = step_length,
                        step_height = step_height,
                        foot_spacing = foot_spacing,
                        )

        geometry.out() 

    # ----------------------------------------------------------------------------------------------------
    # Walk driven by a Curve
    # ----------------------------------------------------------------------------------------------------

    with GeoNodes("Obs Anim Follow Curve"):

        geometry = Geometry()
        anim_factor = Float(1.0, "Factor", 0, 1)

        path_object = Object(None, "Path Object")

        with Panel("Speed"):
            node = G().obs_closure_get_walk(geometry).link_inputs().node
            walk_func = node.walk
            speed = node.speed
            cadence = node.cadence
            step_length = node.step_length
            step_height = node.step_height
            foot_spacing = node.foot_spacing

            path = path_object.info(as_instance=False, transform_space='RELATIVE',).geometry.curve


        for sim in simulation(geometry=geometry):
            bundles = ObserverBundles(sim.geometry, use_factor=False)
            bundles.factor = anim_factor

            oloc = bundles["Location"]

            dt = sim.delta_time*anim_factor

            delta_distance = speed * dt
            oloc["Time"] += dt
            oloc["Phase"] += cadence * dt
            oloc["Distance"] += delta_distance

            location = path.sample_length(length=oloc["Distance"], curve_index=0).position
            oloc["Location"] = location

            tangent = location.tangent_*(1.0, 1.0, 0.0)
            rotation = Rotation().align_y_to_vector(
                vector=tangent, factor=1.0, pivot_axis='Z',
            ).to_euler()

            rotz = rotation.z
            oloc["Direction"] = gnmath.atan2(rotz.sin(), rotz.cos())

            sim.geometry = bundles.update()

        geometry = G().obs_closure_apply_walk(sim.geometry,
                        factor=anim_factor,
                        walk = walk_func,
                        step_length = step_length,
                        step_height = step_height,
                        foot_spacing = foot_spacing,
                        )

        geometry.out() 

    # ====================================================================================================
    # Hand Animation
    # ====================================================================================================

    # ----------------------------------------------------------------------------------------------------
    # Group selecting a preset hand pose
    # ----------------------------------------------------------------------------------------------------
    
    with GeoNodes("Obs Hand Get Preset Hand Pose Function", is_group=True):
        
        PR_NAMES = list(HAND_POSE_PRESETS.keys())
        pose_index = Integer.MenuSwitch(
            named_sockets={
                **{name: i for i, name in enumerate(PR_NAMES)}},
             menu=Input("Preset"))
             
        funcs = [create_hand_pose_func('Rest', name) for name in PR_NAMES]
        func = Closure.IndexSwitch(*funcs, index=pose_index)
        
        func.out()
        
        
    # ----------------------------------------------------------------------------------------------------
    # Group selecting a preset hand pose or a stored hand pose
    # ----------------------------------------------------------------------------------------------------
    
    with GeoNodes("Obs Hand Get Hand Pose Function", is_group=True):
        
        closures = Bundle(None, "Closures")
        
        func = G().obs_hand_get_preset_hand_pose_function().link_inputs()
        stored_name = String(None, "Stored")
        
        with Layout("Preset or stored closure"):
            stored_func = closures.get_item("Hand Pose " + stored_name, socket_type='CLOSURE')
            func.switch( (stored_name.length() > 0) & (stored_func.exists), stored_func)
            
        func.out()
        
    # ----------------------------------------------------------------------------------------------------
    # Group returning a hand pose
    # ----------------------------------------------------------------------------------------------------
    
    with GeoNodes("Obs Hand Get Pose", is_group=True):
        
        closures = Bundle(None, "Closures")
        
        func = G().obs_hand_get_hand_pose_function(closures=closures).link_inputs()
        factor = Float.Factor(1.0, "Factor", 0, 1)
        
        with Panel("Changes"):
            in_params = create_hand_pose_inputs()
            
        with Layout("Evaluate Closure"):
            node = func.evaluate(factor=factor, signature=HAND_POSE_FUNC).node
            
            for name, delta in in_params.items():
                (node[name] + delta).out(name)
            
    # ----------------------------------------------------------------------------------------------------
    # Modifier : Store a custom Hand Pose
    # ----------------------------------------------------------------------------------------------------
    
    with GeoNodes("Obs Hand Store Hand Pose", is_group=False):

        geometry = Geometry()
        bundles = ObserverBundles(geometry, use_factor=False)
        closures = bundles[CLOSURES_NAME].bundle_socket

        store_name = String("No Name", "Name")
        
        with Panel("Pose 0"):
            node0 = G().obs_hand_get_pose(closures=closures).link_inputs().node
            pose0 = {}
            for name in HAND_POSE_SIG.keys():
                pose0[name] = node0[name]
            
            
        with Panel("Pose 1"):
            node1 = G().obs_hand_get_pose(closures=closures).link_inputs().node
            pose1 = {}
            for name in HAND_POSE_SIG.keys():
                pose1[name] = node1[name]
        
        func = create_hand_pose_func(pose0, pose1)
        closures.set_item('Hand Pose' + store_name, func)
        bundles[CLOSURES_NAME].bundle_sockets = closures
        bundles.update().out()

        geometry.out()

    # ----------------------------------------------------------------------------------------------------
    # Apply Hand pose
    # ----------------------------------------------------------------------------------------------------

    with GeoNodes("Obs Anim Hand", is_group=False):

        geometry = Geometry()
        bundles = ObserverBundles(geometry)

        closures = bundles[CLOSURES_NAME].bundle_socket

        use_left = Boolean(True, "Left Hand")
        use_right = Boolean(True, "Right Hand")

        pose_factor = Float(0.0, "Pose Factor", 0, 1)

        with Panel("Pose 0"):
            node0 = G().obs_hand_get_pose(closures=closures).link_inputs().node
            pose0 = {}
            for name in HAND_POSE_SIG.keys():
                pose0[name] = node0[name]
            
        with Panel("Pose 1"):
            node1 = G().obs_hand_get_pose(closures=closures).link_inputs().node
            pose1 = {}
            for name in HAND_POSE_SIG.keys():
                pose1[name] = node1[name]

        func = create_hand_pose_func(pose0, pose1)
        node = func.evaluate(factor=pose_factor, signature=HAND_POSE_FUNC).node

        left_hand = bundles["Left Hand"]
        right_hand = bundles["Right Hand"]

        for name in HAND_POSE_SIG.keys():
            value = node[name]
            left_hand[name].switch(use_left, value)
            right_hand[name].switch(use_right, value)

        bundles.update().out()

    # ====================================================================================================
    # Arm animation: independent controls for each angle
    # ====================================================================================================

    with GeoNodes("Obs Anim Arm"):
        geometry = Geometry()
        bundles = ObserverBundles(geometry, use_factor=False)
        use_left = Boolean(True, "Left Arm")
        use_right = Boolean(True, "Right Arm")

        controls = {}
        for name in ("Lateral", "Forward", "Elbow", "Hand Twist"):
            with Panel(name):
                factor = Float.Factor(1.0, "Factor", 0.0, 1.0)
                relative = Boolean(True, "Relative")
                value = Float.Angle(0.0, "Value")
                amplitude = Float.Angle(0.0, "Amplitude")
                leg_walk = Boolean(True, "Leg Walk", tip=(
                    "Synchronize with the corresponding leg of the current Walk; "
                    "disable for two oscillations per walk cycle."
                ))
                controls[name] = (factor, relative, value, amplitude, leg_walk)

        with Layout("Walk Drivers"):
            phase = bundles["Location"]["Phase"]
            left_sine = (phase * (2*pi)).sin()
            right_sine = -left_sine
            body_sine = (phase * (4*pi)).sin()

        for name, (factor, relative, value, amplitude, leg_walk) in controls.items():
            with Layout(name):
                for side, enabled, leg_sine in (
                    ("Left", use_left, left_sine), ("Right", use_right, right_sine),
                ):
                    driver = Float(body_sine).switch(leg_walk, leg_sine)
                    computed_value = value + amplitude * driver
                    arm = bundles[f"{side} Arm"]
                    current = arm[name]
                    target = Float(computed_value).switch(relative, current + computed_value)
                    result = Float(current).mix(target, factor=factor)
                    arm[name] = Float(current).switch(enabled, result)

        with Layout("Write Pose"):
            bundles.update().out()


    # ----------------------------------------------------------------------------------------------------
    # Foot animation: modify the incoming Walk pose
    # ----------------------------------------------------------------------------------------------------

    with GeoNodes("Obs Anim Foot"):
        geometry = Geometry()
        bundles = ObserverBundles(geometry, use_factor=False)
        use_left = Boolean(True, "Left Foot")
        use_right = Boolean(True, "Right Foot")
        mirror = Boolean(True, "Mirror", tip=(
            "Mirror Location X and Twist on the right foot. "
            "Positive Twist opens both feet outward."
        ))

        controls = {}
        for name in ("Location", "Tilt", "Twist", "Tiptoe"):
            with Panel(name):
                factor = Float.Factor(1.0, "Factor", 0.0, 1.0)
                relative = Boolean(True, "Relative")
                if name == "Location":
                    value = Vector((0, 0, 0), "Value")
                    amplitude = Vector((0, 0, 0), "Amplitude")
                else:
                    value = Float.Angle(0.0, "Value")
                    amplitude = Float.Angle(0.0, "Amplitude")
                leg_walk = Boolean(True, "Leg Walk", tip=(
                    "Synchronize with the corresponding leg of the current Walk; "
                    "disable for two oscillations per walk cycle."
                ))
                controls[name] = (factor, relative, value, amplitude, leg_walk)

        with Layout("Walk Drivers"):
            phase = bundles["Location"]["Phase"]
            left_sine = (phase * (2*pi)).sin()
            right_sine = -left_sine
            body_sine = (phase * (4*pi)).sin()

        for name, (factor, relative, value, amplitude, leg_walk) in controls.items():
            with Layout(name):
                socket_class = Vector if name == "Location" else Float
                for side, enabled, leg_sine in (
                    ("Left", use_left, left_sine), ("Right", use_right, right_sine),
                ):
                    driver = Float(body_sine).switch(leg_walk, leg_sine)
                    computed_value = value + amplitude * driver
                    if side == "Right":
                        if name == "Location":
                            computed_value = computed_value.switch(mirror, computed_value * (-1, 1, 1))
                        elif name == "Twist":
                            computed_value = computed_value.switch(mirror, -computed_value)
                    leg = bundles[f"{side} Leg"]
                    current = leg[f"Foot {name}"]
                    target = socket_class(computed_value).switch(relative, current + computed_value)
                    result = socket_class(current).mix(target, factor=factor)
                    leg[f"Foot {name}"] = socket_class(current).switch(enabled, result)

        with Layout("Write Pose"):
            bundles.update().out()

    # ====================================================================================================
    # Head Animation
    # ====================================================================================================

    # ----------------------------------------------------------------------------------------------------
    # Head Animtion
    # ----------------------------------------------------------------------------------------------------

    with GeoNodes("Obs Anim Head"):

        geometry = Geometry()
        bundles = ObserverBundles(geometry, use_factor=False)

        controls = {}

        dct = {
            "Horizontal" : HEAD_HRZ_MAX,
            "Vertical" : HEAD_VRT_MAX,
            "Lateral" : HEAD_INCL_MAX,
            }
        
        for name, max_val in dct.items():
            with Panel(name):
                factor = Float.Factor(1.0, "Factor", 0.0, 1.0)
                relative = Boolean(True, "Relative")
                value = Float.Angle(0.0, "Value", -max_val, max_val)
                amplitude = Float.Angle(0.0, "Amplitude")
                leg_walk = Boolean(True, "Leg Walk", tip=(
                    "Synchronize with the corresponding leg of the current Walk; "
                    "disable for two oscillations per walk cycle."
                ))
                controls[name] = (factor, relative, value, amplitude, leg_walk)

        with Layout("Walk Drivers"):
            phase = bundles["Location"]["Phase"]
            left_sine = (phase * (2*pi)).sin()
            body_sine = (phase * (4*pi)).sin()

        head = bundles["Head"]
        for name, (factor, relative, value, amplitude, leg_walk) in controls.items():
            with Layout(name):
                driver = Float(body_sine).switch(leg_walk, left_sine)
                computed_value = value + amplitude * driver 

                current = head[name]
                target = Float(computed_value).switch(relative, current + computed_value)
                head[name] = Float(current).mix(target, factor=factor)

        bundles.update().out()        


    # ----------------------------------------------------------------------------------------------------
    # Eyelids: shared controls with individual overrides
    # ----------------------------------------------------------------------------------------------------

    with GeoNodes("Obs Anim Lids"):
        geometry = Geometry()
        bundles = ObserverBundles(geometry, use_factor=False)

        controls = {}
        for name in ("Both", "Left", "Right"):
            with Panel(name):
                factor = Float.Factor(0.0, "Factor", 0.0, 1.0)
                opening = Float(0.25, "Opening", -1.0, 1.0,
                                tip="-1 closes the eyelid; 1 fully opens it.")
                tilt = Float.Angle(0.0, "Tilt")
                if name == "Both":
                    mirror = Boolean(True, "Mirror", tip=(
                        "Apply opposite tilts to the left and right eyelids."
                    ))
                controls[name] = (factor, opening, tilt)

        with Panel("Blink"):
            blink = Boolean(False, "Blink")
            interval = Float(3.5, "Interval", 0.001,
                             tip="Seconds between the starts of two blinks.")
            duration = Float(0.3, "Duration", 0.001,
                             tip="Seconds for closing and reopening the eyelids.")

        with Layout("Blink"):
            period = interval.max(0.001)
            blink_duration = duration.max(0.001).min(period)
            blink_phase = ((nd.scene_time().seconds + period/2) % period).map_range(
                0.0, blink_duration, 0.0, 1.0)
            blink_amount = Float(0.0).switch(
                blink, (1.0 - (blink_phase * (2*pi)).cos()) * 0.5)

        head = bundles["Head"]
        both_factor, both_opening, both_tilt = controls["Both"]
        for side in ("Left", "Right"):
            with Layout(side + " Eyelid"):
                current_opening = head["Eyelid"] + head[side + " Eyelid"]
                current_tilt = head[side + " Eyelid Tilt"]
                shared_tilt = Float(both_tilt)
                if side == "Right":
                    shared_tilt.switch(mirror, -both_tilt)
                opening = Float(current_opening).mix(both_opening, factor=both_factor)
                tilt = Float(current_tilt).mix(shared_tilt, factor=both_factor)

                factor, individual_opening, individual_tilt = controls[side]
                opening = opening.mix(individual_opening, factor=factor)
                tilt = tilt.mix(individual_tilt, factor=factor)
                opening = opening.mix(-1.0, factor=blink_amount)
                head[side + " Eyelid"] = opening - head["Eyelid"]
                head[side + " Eyelid Tilt"] = tilt

        with Layout("Write Pose"):
            bundles.update().out()

    # ----------------------------------------------------------------------------------------------------
    # Eyes: shared controls with individual overrides
    # ----------------------------------------------------------------------------------------------------

    with GeoNodes("Obs Anim Eyes"):
        geometry = Geometry()
        bundles = ObserverBundles(geometry, use_factor=False)

        controls = {}
        for name in ("Both", "Left", "Right"):
            with Panel(name):
                factor = Float.Factor(0.0, "Factor", 0.0, 1.0)
                horizontal = Float.Angle(0.0, "Horizontal", -EYES_HRZ_MAX, EYES_HRZ_MAX)
                vertical = Float.Angle(0.0, "Vertical", -EYES_VRT_MAX, EYES_VRT_MAX)
                if name == "Both":
                    mirror = Boolean(True, "Mirror", tip=(
                        "Apply opposite horizontal angles to the two eyes; "
                        "disable to look in the same direction."
                    ))
                controls[name] = (factor, horizontal, vertical)

        head = bundles["Head"]
        both_factor, both_horizontal, both_vertical = controls["Both"]
        for side in ("Left", "Right"):
            with Layout(side + " Eye"):
                factor, horizontal, vertical = controls[side]
                shared_horizontal = Float(both_horizontal)
                if side == "Right":
                    shared_horizontal.switch(mirror, -both_horizontal)
                for axis, shared, individual in (
                    ("Horizontal", shared_horizontal, horizontal),
                    ("Vertical", both_vertical, vertical),
                ):
                    base = head["Eyes " + axis]
                    key = side + " Eye " + axis
                    current = base + head[key]
                    angle = Float(current).mix(shared, factor=both_factor)
                    angle = angle.mix(individual, factor=factor)
                    head[key] = angle - base

        with Layout("Write Pose"):
            bundles.update().out()

    # ----------------------------------------------------------------------------------------------------
    # Look at: orient the incoming head/eye pose toward a target
    # ----------------------------------------------------------------------------------------------------

    with GeoNodes("Obs Anim Look At"):
        geometry = Geometry()
        pose = ObserverBundles(geometry, use_factor=False)
        look_at_fac = Float.Factor(1.0, "Factor", 0, 1)
        look_at_obj = Object(None, "Look At")
        head_fraction = Float.Factor(0.0, "Head Fraction", 0, 1)

        with Layout("Read Pose"):
            head_params = pose["Head"]
            head_hrz = Float(head_params["Horizontal"])
            head_vrt = Float(head_params["Vertical"])
            eyes_hrz = Float(head_params["Eyes Horizontal"])
            eyes_vrt = Float(head_params["Eyes Vertical"])

        with Layout("Look At"):
            body = pose["Body"]
            target = look_at_obj.info(transform_space='RELATIVE').location_
            direction = target - pose.eyes_location()
            # Undo the character heading and local body rotation.
            heading = Rotation.FromEuler(Vector((0, 0, pose["Location"]["Direction"])))
            direction = heading.invert() @ direction
            direction = Rotation.FromEuler(body["Body Rotation"]).invert() @ direction

            horizontal = gnmath.atan2(-direction.x, direction.y)
            vertical = gnmath.atan2(
                direction.z, Vector((direction.x, direction.y, 0.0)).length(),
            )
            target_head_hrz = (horizontal * head_fraction).clamp(-HEAD_HRZ_MAX, HEAD_HRZ_MAX)
            target_head_vrt = (vertical * head_fraction).clamp(-HEAD_VRT_MAX, HEAD_VRT_MAX)
            # Eyes use the opposite horizontal sign in Obs Head.
            target_eyes_hrz = (target_head_hrz - horizontal).clamp(-EYES_HRZ_MAX, EYES_HRZ_MAX)
            target_eyes_vrt = (vertical - target_head_vrt).clamp(-EYES_VRT_MAX, EYES_VRT_MAX)

            head_params["Horizontal"] = head_hrz.mix(target_head_hrz, factor=look_at_fac)
            head_params["Vertical"] = head_vrt.mix(target_head_vrt, factor=look_at_fac)
            head_params["Eyes Horizontal"] = eyes_hrz.mix(target_eyes_hrz, factor=look_at_fac)
            head_params["Eyes Vertical"] = eyes_vrt.mix(target_eyes_vrt, factor=look_at_fac)

        pose.update()
        geometry.out()



# =============================================================================================================================
# =============================================================================================================================
# Build Observer
# =============================================================================================================================
# =============================================================================================================================

def build_observer():

    """Build materials and mesh groups. Run build_animation() first on initial setup."""
    # =============================================================================================================================
    # Shader

    if bpy.data.materials.get("Obs Skin") is None:
        with ShaderNodes("Obs Skin"):
    
            color  = [0.650011, 0.523698, 0.411225, 1.000000]
            transp = snd.attribute(attribute_type='GEOMETRY', attribute_name="Transparency").factor
    
            ped = Shader.Principled(
                base_color = color,
                roughness  = .9,
            )
    
            shader = ped.mix(Shader.Transparent(), factor=transp)
            shader.out()

    if bpy.data.materials.get("Obs Eye") is None:
        with ShaderNodes("Obs Eye"):
            white = snd.attribute(attribute_type='GEOMETRY', attribute_name="White").factor
            color = Color((0, 0, 0)).mix(white, Color((1, 1, 1)))
            transp  = snd.attribute(attribute_type='GEOMETRY', attribute_name="Transparency").factor
    
            ped = Shader.Principled(
                base_color = color,
                roughness  = 0,
            )
    
            shader = ped.mix(Shader.Transparent(), factor=transp)
    
            shader.out()

    if bpy.data.materials.get("Obs Hair") is None:
        with ShaderNodes("Obs Hair"):
    
            color   = Color(snd.attribute(attribute_type='GEOMETRY', attribute_name="Color").vector)
            transp  = snd.attribute(attribute_type='GEOMETRY', attribute_name="Transparency").factor
    
            ped = Shader.PrincipledHair(
                color = color,
            )
    
            shader = ped.mix(Shader.Transparent(), factor=transp)
    
            shader.out()

    if bpy.data.materials.get("Obs Blouse") is None:
        with ShaderNodes("Obs Blouse"):
    
            color   = Color(snd.attribute(attribute_type='GEOMETRY', attribute_name="Color").vector)
            transp  = snd.attribute(attribute_type='GEOMETRY', attribute_name="Transparency").factor
    
            ped = Shader.Principled(
                base_color = color,
                roughness  = .8,
            )
    
            shader = ped.mix(Shader.Transparent(), factor=transp)
    
            shader.out()

    if bpy.data.materials.get("Obs Shoe") is None:
        with ShaderNodes("Obs Shoe"):
    
            color   = [0.000000, 0.000000, 0.000000, 1.000000]
            transp  = snd.attribute(attribute_type='GEOMETRY', attribute_name="Transparency").factor
    
            ped = Shader.Principled(
                base_color = color,
                roughness  = .3,
            )
    
            shader = ped.mix(Shader.Transparent(), factor=transp)
    
            shader.out()

    # ====================================================================================================
    # Key function
    # ====================================================================================================

    with GeoNodes("Obs Mesh Hair Scalp", is_group=True):

        mesh     = Mesh()
        top_z    = Float(.75, "Top")
        back_z   = Float(.1, "Back")
        rot      = Vector.Euler((0, pi/4, 0), "Rotation")

        x, y, z = nd.position.xyz

        mesh.points._Yes = x < .1

        mesh.transform(rotation=rot)
        mesh.points._BScalp = (z >= back_z) & Boolean("Yes")
        mesh.transform(rotation=rot.scale(-1))

        mesh.points._BScalp = Boolean("BScalp") | (z >= top_z)

        mesh.points._Hair_Scalp = Float(Boolean("BScalp"))
        mesh.remove_named_attribute(name="BScalp")

        mesh.out()
        Float("Hair Scalp").out("Hair Scalp")

    # ====================================================================================================
    # Moustache scalp
    # ====================================================================================================

    with GeoNodes("Obs Mesh Moustache Scalp", is_group=True):

        mesh     = Mesh()
        top_z    = Float( -.3, "Top")
        bot_z    = Float( -.6, "Bottom")
        width    = Float( 1.1, "Width")

        x, y, z = nd.position.xyz

        scalp = (z <= top_z) & (z >= bot_z) & (x > 0) & (gnmath.abs(y) < width/2)
        mesh.points._Moustache_Scalp = scalp

        mesh.out()
        Float("Moustache Scalp").out("Moustache Scalp")

    # ====================================================================================================
    # Hair
    # ====================================================================================================

    with GeoNodes("Obs Mesh Hair", is_group=True):

        mesh = Mesh()
        scalp = Float.Factor(1, "Scalp", 0, 1)

        with Panel("Hair"):
            color   = Color((0.439239, 0.078419, 0.007497, 1.000000), "Color")
            length  = Float(.4, "Length")
            curl    = Float.Factor(0, "Curl", 0, 1)
            radius  = Float(.01, "Radius", 0, .1)
            density = Float(50_000., "Density")

        with Layout("Generate"):

            count = curl.map_range(to_min=6, to_max=12).to_integer()

            hair_node = G().generate_hair_curves(
                    hair_surface    = mesh,
                    hair_length     = length,
                    control_points  = count,
                    density         = density,
                    density_mask    = scalp,
                    viewport_amount = .1,
                    ).node

            # Use the generated mesh rather than an external surface object.
            hair_node._bnode.inputs['Surface Source'].default_value = 'Input'

        with Layout("To Mesh"):
            hair = hair_node.curves

            hair = G().set_hair_curve_profile(
                hair,
                replace_radius = True,
                radius     = radius,
                shape      = .5,
                factor_min = .1,
                factor_max = 1,
            )
            hair = Curve(hair)

            hair = hair.to_mesh(profile_curve=Curve.Circle(resolution=6, radius=1), scale=nd.radius, fill_caps=True)

            hair.faces.Color = color
            hair.faces.material = "Obs Hair"

        (mesh + hair).out()

    # ====================================================================================================
    # ====================================================================================================
    # Observer modifiers
    # ====================================================================================================
    # ====================================================================================================

    # ====================================================================================================
    # Building the hand
    # ====================================================================================================

    # ----------------------------------------------------------------------------------------------------
    # One Finger
    # ----------------------------------------------------------------------------------------------------

    with GeoNodes(".Obs Hand Finger", is_group=True):
        
        length = Float(1.0, "Size")
        
        d = create_finger_inputs(i_finger=None)
        lateral = d[LATERAL]
        bend, fold, fold2 = d[FOLD].xyz
        
        bend_factor = Float.Factor(0.0, "Bend Factor")
        subdiv = Integer(5, "Palm Subdivisions", 0, 20)
        position = Vector(0, "Position")
        base_offset = Vector(0, "Base Offset")

        with Layout("Full Bones"):
            # Base Segment
            line = G().build_poly_line(length=length*1.0, angle=pi/2 + lateral/2, plane='YZ')
            # Bend 
            line = G().build_poly_line(line, length=length*0.4, angle=bend, plane='XZ')
            
            line = G().build_poly_line(line, length=length*0.3, angle=fold, plane='XZ')
            line = G().build_poly_line(line, length=length*0.3, angle=fold2, plane='XZ')

            with Layout("Finger Lateral"):
                pivot = line.points.sample_index(nd.position, index=1)
                line.points[nd.index > 1].position = pivot + Rotation((lateral/2, 0, 0)) @ (nd.position - pivot)
                
            with Layout("Additional Bend"):
                ag = bend.map_range(0, radians(15), 0, radians(15)*bend_factor, interpolation_type='Smooth Step')
                line.transform(rotation=(0, ag, 0))

            line = G().round_joints(line, selection=nd.index >= 1, resolution=2, length=0.07)

            line = G().subdivide_segment(line, index=0, subdivisions=subdiv)
            line.points.radius = 1.0
            line.points[nd.index < subdiv].radius = 1.2
            line.points[nd.index == subdiv].radius = 1.1
            
            line.points[nd.index == 0].offset = base_offset
            line.offset = position
            
        with Layout("Split Palm / Finger bones"):
            palm_bones = Curve(line).points[nd.index > subdiv + 3].delete()
            finger_bones = Curve(line).points[nd.index < subdiv + 3].delete()

        with Layout("Finger Mesh"):
            if False:
                finger_mesh = finger_bones.to_mesh(
                    profile_curve = Curve.Circle(radius=0.15, resolution=8),
                    fill_caps=False)
                finger_mesh = meshutil.set_cylinder_topology(finger_mesh, finger_bones.points.count, 8)
                finger_mesh = G().close_cylinder(
                    finger_mesh,
                    rings = 3,
                    height = 0.15,
                    bottom =True,
                    top = True,
                    flatten_last = False,
                    append = True,
                    )
                finger_mesh.flip_faces()
                finger_mesh.faces.shade_smooth=True
                
            else:
                finger_mesh = finger_bones.curve_to_tube(
                        scale=0.15,
                        profile_resolution=8,
                        caps=True,
                        caps_type='Round',
                        )

        finger_mesh.out("Mesh")
        palm_bones.out("Palm Bones")
        finger_bones.out("Finger Bones")
        line.out("Bones")

    # ----------------------------------------------------------------------------------------------------
    # Thumb
    # ----------------------------------------------------------------------------------------------------

    with GeoNodes(".Obs Hand Thumb", is_group=True):

        length = 1.0

        d = create_finger_inputs(i_finger=None)
        lateral = d[LATERAL]
        bend, fold, pinch = d[FOLD].xyz
        position = Vector(None, "Position")

        with Layout("Prepare"):
            ph = length/3 

        line = G().build_poly_line(length=length*0.5, angle=3*pi/4 + lateral, plane='YZ')
        line = G().build_poly_line(line, length=ph, angle=-bend, plane='YZ')
        line = G().build_poly_line(line, length=ph, angle=-fold, plane='YZ')

        #line.transform(rotation=(0, 0, math.radians(35)))
        #line.transform(rotation=(math.radians(45) + lateral, 0, 0))
        line.transform(rotation=(0, pinch, pinch))
        
        line.offset = position
        
        with Layout("Radius"):
            line.radius = nd.spline_parameter().factor.map_range(0, 0.8, 1.5, 1.1)

        with Layout("Thumb Mesh"):
            profile = G().round_joints(line, resolution=2, length=0.07)
            thumb_mesh = profile.curve_to_tube(
                scale=0.15,
                profile_resolution=10,
                caps=True,
                caps_type='Round',
            )
            
        thumb_mesh.out("Mesh")
        line.out("Finger Bones")

    # ----------------------------------------------------------------------------------------------------
    # Hand
    # ----------------------------------------------------------------------------------------------------

    with GeoNodes("Obs Mesh Hand", is_group=False):

        DELTA_X = -0.08
        DELTA_Y = 0.3
        SUBDIV = 7
        
        size = Float(1.0, "Size", 0.001)
        is_right = Boolean(False, "Right Hand")
        
        with Layout("Finger bones"):

            with Panel("Fingers"):
                thumb = G()._obs_hand_thumb(
                    lateral = Float.Angle(0.0, "Lateral 0"),
                    fold = Vector.Euler(0.0, "Fold 0"),
                    position = (0, DELTA_Y*(-1.4), 0.1)
                ).link_inputs()

                finger1 = G()._obs_hand_finger(
                    lateral = Float.Angle(0.0, "Lateral 1"),
                    fold = Vector.Euler(0.0, "Fold 1"),
                    size=1.0, 
                    bend_factor=0.1, 
                    palm_subdivisions=SUBDIV,
                    position=(0, DELTA_Y*(-1.5), 0),
                    base_offset=(0, DELTA_Y*.2, 0),
                    ).link_inputs()

                finger2 = G()._obs_hand_finger(
                    lateral = Float.Angle(0.0, "Lateral 2"),
                    fold = Vector.Euler(0.0, "Fold 2"),
                    size=1.1, 
                    bend_factor=0.1, 
                    palm_subdivisions=SUBDIV,
                    position=(DELTA_X, DELTA_Y*(-0.5), 0),
                    base_offset=(0, DELTA_Y*.1, 0),
                    ).link_inputs()

                finger3 = G()._obs_hand_finger(
                    lateral = Float.Angle(0.0, "Lateral 3"),
                    fold = Vector.Euler(0.0, "Fold 3"),
                    size=1.05, 
                    bend_factor=0.5, 
                    palm_subdivisions=SUBDIV,
                    position=(DELTA_X, DELTA_Y*( 0.5), 0),
                    base_offset=(0, -DELTA_Y*.1, 0),
                    ).link_inputs()

                finger4 = G()._obs_hand_finger(
                    lateral = Float.Angle(0.0, "Lateral 4"),
                    fold = Vector.Euler(0.0, "Fold 4"),
                    size=0.95, 
                    bend_factor=1.0, 
                    palm_subdivisions=SUBDIV,
                    position=(0, DELTA_Y*( 1.5), 0),
                    base_offset=(0, -DELTA_Y*.2, 0),
                    ).link_inputs()

        material = Material("Obs Skin", "Material")

        fingers = [thumb, finger1, finger2, finger3, finger4]
        
        with Layout("Palm Mesh"):
            
            thumb_bones = thumb.finger_bones
            bones1 = Curve(finger1.palm_bones)
            bones2 = Curve(finger2.palm_bones)
            bones3 = Curve(finger3.palm_bones)
            bones4 = Curve(finger4.palm_bones)
            
            n = bones1.points.count
            fake = Curve.Line().resample(count=n)
            segm = Curve(thumb_bones)
            segm.points[nd.index > 1].delete()
            segm = segm.resample(count = n)
            
            segm[(nd.index < 1) | (nd.index > 5)].position = bones1.points.sample_index(nd.position, index=nd.index)
            
            segm.radius = nd.spline_parameter().factor.map_range(0, 0.6, 1.6, 1.0)

            palm_bones = segm + bones2 + bones3 + bones4
            
            palm_mesh = G().bones_envelope(
                palm_bones,
                cross_splines=True,
                radius=nd.radius*0.15,
                caps_height=0.1,
                caps_top = False,
                )
                
        with Layout("Final Hand"):
            hand = palm_mesh + tuple(fingers)
            hand.transform(scale=size)

            right_hand = Mesh(hand).transform(scale=(-1, 1, 1)).flip_faces()
            hand.switch(is_right, right_hand)

            hand.faces.material = material

        hand.out()

    # ====================================================================================================
    # Arm Curve
    # ====================================================================================================

    with GeoNodes("Obs Mesh Arm", is_group=True):

        size = Float(0.7, "Size")
        is_right = Boolean(True, "Right Arm")
        location = Vector(0, "Location")
        lateral = Float.Angle(0, "Lateral")
        forward = Float.Angle(0, "Forward")
        elbow = Float.Angle(0, "Elbow")
        hand_flap = Float.Angle(0, "Hand Flap")
        hand_twist = Float.Angle(0, "Hand Twist")
        use_merge = Boolean(False, "Merge")

        hand = Mesh(name="Hand")
        
        with Layout("Arm Bones"):
            line = Curve.Line(end=(0, 0, -1.5)).resample(count=4)
            line[nd.index==3].offset = (0, 0, 0.3)
            
            def rotate(index, rot, title="Rotation"):
                with Layout(title):
                    pivot = line.points.sample_index(nd.position, index=index)
                    line[nd.index > index].position = pivot + Rotation(rot) @ (nd.position - pivot)
                    
            rotate(2, (0, hand_flap, 0), "Hand Flap")
            rotate(1, (elbow, 0, 0), "Elbow")
            rotate(0, (forward, 0, 0), "Forward")
            rotate(0, (0, -lateral, 0), "Lateral")
            
            side_factor = Float.Switch(is_right, -1, 1)
            line.position = nd.position * (side_factor*size, size, size)
            line.offset = location*(side_factor, 1, 1)
            
        with Layout("Place Hand"):
            hand_twist.switch(is_right, -hand_twist)
            hand_twist = hand_twist
            #hand_twist -= elbow
            hand.transform(rotation=(0, 0, hand_twist))
            
            p0 = line.points.sample_index(nd.position, index=2)
            p1 = line.points.sample_index(nd.position, index=3)
            rot = Rotation().align_z_to_vector(p1 - p0, pivot_axis='X')
            
            hand.transform(rotation=rot)
            hand.offset = p0
        
        hand.switch(use_merge, hand + line)
        hand.out()


    # ====================================================================================================
    # Articulated sausage
    # ====================================================================================================

    with GeoNodes("Obs Mesh Sausage", is_group=True):

        curve    = Curve()
        profile  = Curve(None, "Profile")
        angle    = Float.Angle(.2, "Angle", hide_value=False)
        twist    = Float.Angle(0, "Twist", -pi, pi)
        axis     = Integer.MenuSwitch({'X': 0, 'Y': 1, 'Z': 2}, menu=Input("Axis"))
        use_mesh = Boolean(True, "Mesh")

        with Panel("Joints"):
            use_joints   = Boolean(True, "Joints")
            joints_width = Float.Factor(.1, "Joints Width", 0, 1)

        with Panel("Extremities"):
            start_shape = Float(.4,    "Start Shape", 0, 5)
            start_resol = Integer(0,   "Start Resolution", 0)
            end_shape   = Float(.4,    "End Shape", 0, 5)
            end_resol   = Integer(0,   "End Resolution", 0)

        n  = curve.points.count

        for rep in repeat(n-1, curve=curve):
            index   = rep.iteration + 1
            pos     = nd.position
            center  = rep.curve.points.sample_index(pos, index=index)
            ag      = rep.curve.points.sample_index(angle, index=index)
            rot     = Rotation.IndexSwitch((ag, 0, 0), (0, ag, 0), (0, 0, ag), index=axis)
            p       = center + rot @ (pos - center)
            rep.curve.points[nd.index > index].position = p

        curve = rep.curve

        with Layout("Joints"):

            # 0------1------2------3------4------5
            # 0      1 2  3 4 5  6 7 8  9 10     11

            n_joints = n - 3
            m = n + n_joints*2 # 3n - 6
            last = m - 1

            with Layout("Joints Selection"):
                i = nd.index + 2
                joint_sel   = (i % 3).equal(0)
                joint_index = i // 3

            with Layout("Left"):
                i = nd.index + 1
                left_sel = (i % 3).equal(0) & nd.index.not_equal(last)
                left0 = i // 3
                left1 = left0 + 1

            with Layout("Right"):
                i = nd.index
                right_sel = (i % 3).equal(0) & i.not_equal(0)
                right0 = i // 3
                right1 = right0 + 1

            new_curve = Curve(curve).resample(count=m)

            # ----- Left

            with Layout("Left"):

                jfac = .3*joints_width

                pos0 = curve.points.sample_index(nd.position, index=left0)
                pos1 = curve.points.sample_index(nd.position, index=left1)
                new_curve.points[left_sel].position = pos0 + jfac*(pos1 - pos0)

                r0 = curve.points.sample_index(nd.radius, index=left0)
                r1 = curve.points.sample_index(nd.radius, index=left1)
                new_curve.points[left_sel].radius = r0 + jfac*(r1 - r0)

            with Layout("Right"):

                jfac = 1 - jfac

                pos0 = curve.points.sample_index(nd.position, index=right0)
                pos1 = curve.points.sample_index(nd.position, index=right1)
                new_curve.points[right_sel].position = pos0 + jfac*(pos1 - pos0)

                r0 = curve.points.sample_index(nd.radius, index=right0)
                r1 = curve.points.sample_index(nd.radius, index=right1)
                new_curve.points[right_sel].radius = r0 + jfac*(r1 - r0)

            with Layout("Joints"):
                new_curve.points[joint_sel].position = curve.points.sample_index(nd.position, index=joint_index)
                new_curve.points[joint_sel].radius   = curve.points.sample_index(nd.radius,   index=joint_index)

            curve = Curve(curve.switch(use_joints, new_curve))
            n = curve.points.count

        with Layout("Twist"):
            curve = curve.transform(rotation=(0, 0, twist))

        with Layout("Start Shape"):

            m = n + start_resol
            start_resol1 = start_resol + 1

            new_curve = Curve(curve).resample(count=m)
            new_curve.points[nd.index > start_resol].position = curve.points.sample_index(nd.position, index=nd.index - start_resol)
            new_curve.points[nd.index > start_resol].radius   = curve.points.sample_index(nd.radius,   index=nd.index - start_resol)

            fac = nd.index/start_resol1

            pos0 = curve.points.sample_index(nd.position, index=0)
            pos1 = curve.points.sample_index(nd.position, index=1)

            new_curve.points[nd.index <= start_resol].position = pos0 + (pos1 - pos0).scale(fac)

            radius = curve.points.sample_index(nd.radius, index=1)
            new_curve.points[nd.index <= start_resol].radius = radius*fac**start_shape

            curve = new_curve
            n = curve.points.count

        with Layout("End Shape"):

            m = n + end_resol
            last = n - 2

            new_curve = Curve(curve).resample(count=m)
            new_curve.points[nd.index <= last].position = curve.points.sample_index(nd.position, index=nd.index)
            new_curve.points[nd.index <= last].radius   = curve.points.sample_index(nd.radius,   index=nd.index)

            fac = (nd.index - last)/(end_resol + 1)

            pos0 = curve.points.sample_index(nd.position, index=n-2)
            pos1 = curve.points.sample_index(nd.position, index=n-1)

            new_curve.points[nd.index > last].position = pos0 + (pos1 - pos0).scale(fac)

            radius = curve.points.sample_index(nd.radius, index=n-2)
            new_curve.points[nd.index > last].radius = radius*(1-fac)**end_shape

            curve = new_curve
            #n = curve.points.count


        mesh = curve.to_mesh(profile_curve=profile, scale=nd.radius)
        curve.switch(use_mesh, mesh).out()

    # ====================================================================================================
    # Walk control
    # ====================================================================================================

    with GeoNodes("Obs Mesh Shoe", is_group=True):
        
        FOOT_LENGTH = 0.5
        FOOT_BACK = 0.1
        FOOT_FRONT = FOOT_LENGTH - FOOT_BACK
        FOOT_HEIGHT = 0.1
        FOOT_BREAK = 0.15
        BREAK_POS = FOOT_FRONT - FOOT_BREAK

        resol  = Integer(16,    "Resolution")
        size   = Float(1,       "Size", 0)
        twist  = Float.Angle(0, "Twist")

        loc    = Vector(None,   "Location")
        tilt   = Float.Angle(0, "Tilt")
        tiptoe = Float.Angle(0, "Tiptoe")
        on_ground = Boolean(True, "On Ground")
        
        with Layout("Tip toe angle"):
            z_foot = loc.z
            
            with Layout("Positive Tilt"):
                max_tilt = gnmath.atan2(z_foot, BREAK_POS)
                tilt.switch(on_ground, gnmath.min(max_tilt, tilt))
                
                sin_tilt = tilt.sin()
                z_tip = z_foot - sin_tilt*FOOT_FRONT
                tiptoe.switch(on_ground & (tilt > 0) & (z_tip < 0), gnmath.atan2(z_tip, FOOT_BREAK))
                
            with Layout("Negative Tilt"):
                min_tilt = -gnmath.atan2(z_foot, FOOT_BACK)
                tilt.switch(on_ground, gnmath.max(min_tilt, tilt))

        with Layout("Curve"):

            ind = [nd.index.equal(i) for i in range(4)]

            curve = Curve.Line(start=(-.2, 0, 0), end=(.8, 0, 0)).resample(count=4)
            curve.points[ind[1]].position = (0, 0, 0)
            curve.points[ind[2]].position = (.5, 0, 0)

            curve.points[ind[0]].radius = 0
            curve.points[ind[1]].radius = 1
            curve.points[ind[2]].radius = .8
            curve.points[ind[3]].radius = 0

            curve.points._Angle = 0.
            curve.points[ind[2]]._Angle = tiptoe
            curve.transform(scale=size)

        with Layout("Profile"):
            profile = Curve.Circle(radius=.22).resample(count=2*resol + 2)
            profile.points[(nd.index > 0) & (nd.index <= resol)].delete()
            profile.transform(scale=size)

        with Layout("Shoe Shape"):

            shoe = G().obs_mesh_sausage(
                curve               = curve,
                profile             = profile,
                angle               = Float("Angle"),
                joints              = True,
                joints_width        = .4,
                axis                = 'Y',
                start_shape         = .4,
                start_resolution    =  4,
                end_shape           = .4,
                end_resolution      =  4,
            )
        shoe = Mesh(shoe.transform(rotation=(0, 0, pi/2)))

        with Layout("Finalize"):
            shoe.faces.shade_smooth = True
            shoe.faces.material = "Obs Shoe"

        shoe.transform(scale=.5)

        with Layout("Orientation in space"):
            shoe.transform(rotation=(-tilt, 0, 0))
            shoe.transform(translation=loc, rotation=(0, 0, twist))

        shoe.out()

    # ====================================================================================================
    # Observer Head
    # ====================================================================================================

    with GeoNodes("Obs Mesh Head", is_group=True):

        EYE_RADIUS = 0.12*HEAD_HEIGHT
        LID_RADIUS = EYE_RADIUS*1.2

        HEAD_SIZE = (0.4*HEAD_HEIGHT, 0.4*HEAD_HEIGHT, 0.5*HEAD_HEIGHT)
        NOSE_SIZE = (0.15*HEAD_HEIGHT, .195*HEAD_HEIGHT, .15*HEAD_HEIGHT)
        NOSE_LOC = (0.0, -.455*HEAD_HEIGHT, -.04*HEAD_HEIGHT)

        EYE_LOC0 = ( 0.25*HEAD_HEIGHT, -0.3*HEAD_HEIGHT, HEAD_EYE_Z)
        EYE_LOC1 = (-EYE_LOC0[0], EYE_LOC0[1], HEAD_EYE_Z)

        geometry = Geometry()
        pose = ObserverBundles(geometry, use_factor=False)

        resol  = Integer(8, "Resolution", 1, 8)

        with Panel("Hair"):
            hair_obj  = Object(None, "Hair Object")
            hair_mat  = Material("Obs Hair", "Hair Material")
            use_hair  = Boolean(True,    "Hair")
            hair_col  = Color([0.061606, 0.008269, 0.002920, 1.000000], "Hair Color")
            use_moust = Boolean(True,    "Moustache")
            moust_col = Color([0.061606, 0.008269, 0.002920, 1.000000], "Moustache Color")

        head_params = pose["Head"]
        head_hrz = head_params["Horizontal"]
        head_vrt = head_params["Vertical"]
        head_lat = head_params["Lateral"]
        hrz_angle = head_params["Eyes Horizontal"]
        vrt_angle = head_params["Eyes Vertical"]
        ag_eyelid = head_params["Eyelid"]
        left_eyelid = head_params["Left Eyelid"]
        right_eyelid = head_params["Right Eyelid"]

        with Layout("Base Sphere"):
            segments = resol*8
            rings    = resol*4

            sphere = Mesh.UVSphere(segments=segments, rings=rings, radius=1.0)
            sphere.faces.shade_smooth = True
            sphere.faces.material = "Obs Skin"

        with Layout("Hair and Moustache"):
            sphere.transform(rotation=(0, 0, pi/2))

            head = G().obs_mesh_hair_scalp(sphere)
            head = G().obs_mesh_moustache_scalp(head)

            head.transform(rotation=(0, 0, -pi/2))

        head = head.transform(scale=HEAD_SIZE)
        nose = Mesh(sphere).transform(scale=NOSE_SIZE, translation=NOSE_LOC)

        head += nose

        with Layout("Eyes"):
            eye = Mesh.UVSphere(segments=segments//2, rings=rings//2, radius=EYE_RADIUS)
            eye.faces.set('White', nd.position.z < .9*EYE_RADIUS)
            eye.transform(rotation=(pi/2, 0, 0))

            eye.faces.shade_smooth = True
            eye.faces.material = "Obs Eye"

            for side, location in (("Left", EYE_LOC0), ("Right", EYE_LOC1)):
                horizontal = hrz_angle + head_params[side + " Eye Horizontal"]
                vertical = vrt_angle + head_params[side + " Eye Vertical"]
                eye_rot = Vector((-vertical, 0, -horizontal))
                head += Mesh(eye).transform(translation=location, rotation=eye_rot)

        with Layout("Eyelids"):

            nsegms = segments // 2
            eyelid = Mesh.UVSphere(segments=nsegms, rings=rings//2, radius=LID_RADIUS)
            eyelid.points[nd.position.z < -0.01].delete()

            eyelid.faces.shade_smooth = True
            disk = Mesh.Circle(vertices=nsegms, radius=LID_RADIUS, fill_type='NGON').flip_faces()

            eyelid += disk
            eyelid.merge_by_distance()

            eyelid.faces.material = "Obs Skin"

            left_ag  = (ag_eyelid + left_eyelid).map_range(-1., 1., pi/2, -pi/2)
            right_ag = (ag_eyelid + right_eyelid).map_range(-1., 1., pi/2, -pi/2)

            left_eyelid  = Mesh(eyelid).transform(translation=EYE_LOC0, rotation=(left_ag, head_params["Left Eyelid Tilt"], 0))
            right_eyelid = Mesh(eyelid).transform(translation=EYE_LOC1, rotation=(right_ag, head_params["Right Eyelid Tilt"], 0))

            head += (left_eyelid, right_eyelid)

        with Layout("External Hair"):
            hair_geo = Mesh(hair_obj.info().geometry)
            hair_geo.faces.material = hair_mat
            hair_geo.faces._Color = hair_col
            hair_geo.transform(scale=4)
            head = Mesh(head + hair_geo)

        with Layout("Generate Hair and Moustache"):
            # In Observer, hair is generated with a head height of 0.92,
            # before the final 0.5 scale. Match its proportions at this size.
            hair_scale = HEAD_HEIGHT / 0.92
            for attribute, enabled, color, length, density in (
                ("Hair Scalp", use_hair, hair_col, 0.5, 5_000),
                ("Moustache Scalp", use_moust, moust_col, 0.16, 10_000),
            ):
                with Layout(attribute):
                    scalp = Float(attribute)
                    scalp = scalp * scalp.exists_
                    head = G().obs_mesh_hair(
                        head, scalp=scalp, color=color,
                        length=length * hair_scale, curl=0,
                        density=density / (hair_scale * hair_scale),
                        radius=0.01 * hair_scale,
                    ).switch_false(enabled, head)
            head = Mesh(head)

        with Panel("Head Orientation"):
            #head.transform(translation=(0, 0, 1.1))
            #head.transform(translation=(0, 0, -1.1), rotation=(-head_vrt, head_lat, head_hrz))
            head.transform(translation=(0, 0, NECK_HEIGHT + HEAD_HEIGHT/2))
            head.transform(rotation=(0, 0, pi))
            head.transform(rotation=(head_vrt, -head_lat, head_hrz))

        head.out()

    # ====================================================================================================
    # Observer Body
    # ====================================================================================================

    with GeoNodes("Obs Mesh Body", is_group=False):

        geometry = Geometry()
        pose = ObserverBundles(geometry, use_factor=False)
        resol  = Integer(8, "Resolution", 1, 8)
        color  = Color((1, 0, 0), "Color")

        col_attr = Attribute("Color", Color)

        with Layout("Base Sphere"):
            segments = resol*8
            rings    = resol*4

            sphere = Mesh.UVSphere(segments=segments, rings=rings, radius=1)
            sphere.faces.shade_smooth = True
            sphere.faces.material = "Obs Skin"

        with Layout("Body"):
            body = sphere.transform(scale=(1.15, 1.15, 1.8))
            tshirt = nd.position.z < 1.6
            body.faces[tshirt].set(col_attr, 1.0)
            body.faces[tshirt].material = "Obs Blouse"

            blouse = Mesh(body).transform(scale=(1.02, 1.02, 1.02))
            blouse.faces.material = "Obs Blouse"
            blouse.faces.set(col_attr, color)

            cube = Mesh.Cube(size=(3, 3, 1.7)).transform(translation=(0, 0, 1.7/2))
            # Set a différent material to delete faces
            cube.faces.material = "Obs Skin"
            blouse = blouse.intersect(cube)

            cyl = Mesh.Cylinder(vertices=8).transform(rotation=(0, 2*pi/3, 0), translation=(0.8, 0, 2.3))
            cyl.faces.material = "Obs Skin"

            blouse = blouse.difference(cyl)
            blouse.transform(rotation=(0, 0, -pi/2))

            blouse.faces[nd.material_index==0].delete()

            top = nd.position.z < .01
            for _ in range(10):
                top = blouse.edges[top].extrude(offset=(0, 0, -.25)).top_

            body.transform(translation=(0, 0, -3))
            blouse.transform(translation=(0, 0, -3))

        body.transform(translation=(0, 0, 1.5), rotation=(0, 0, pi), scale=.23)
        blouse.transform(translation=(0, 0, 1.5), rotation=(0, 0, pi), scale=.23)

        with Layout("Lab Coat Motion"):
            cloth = pose["Cloth"]
            # The hem is at local Z = 1.5 + .23 * (-2.5 - 3) = .235.
            influence = nd.position.z.map_range_smooth_step(
                CLOTH_SWAY_START_Z, 0.235, 0.0, 1.0)
            time = nd.scene_time().seconds * cloth["Speed"]
            noise = nd.noise_texture(
                vector=nd.position + Vector((cloth["Seed"] * 19.19, 0, 0)),
                w=time, scale=cloth["Noise Scale"], noise_dimensions='4D')
            random_offset = (Vector(noise.color) - Vector((0.5, 0.5, 0.5))) * 2.0
            sway = (pose["Location"]["Phase"] * (2*pi)).sin() * cloth["Walk Amplitude"]
            blouse.points.position += influence * (
                random_offset * cloth["Amplitude"] + Vector((sway, 0, 0)))

        body += blouse

        body.out()


    # ====================================================================================================
    # Observer
    # ====================================================================================================

    with GeoNodes("Observer"):

        # ---------------------------------------------------------------------------
        # Params
        # ---------------------------------------------------------------------------

        resol  = Integer(8, "Resolution", 1, 8)
        scale = Float(1.0, "Scale", 0.0, tip="Uniform character size; global location is unchanged")
        transp = Float.Factor(0, "Transparency", 0, 1)

        geometry = Geometry()
        pose = ObserverBundles(geometry, use_factor=False)
        body_params = pose["Body"]
        oloc = pose["Location"]

        # ---------------------------------------------------------------------------
        # Main
        # ---------------------------------------------------------------------------

        with Layout("Head"):
            head = G().obs_mesh_head(geometry, resolution=resol).link_inputs(from_panel="Head")
            head.transform(translation=(0, 0, BODY_HEIGHT))

        with Layout("Body"):
            body = G().obs_mesh_body(geometry, resolution=resol).link_inputs(from_panel="Body")

        obs = body + head

        with Layout("Shoes"):
            shoes = []
            for side in ("Left", "Right"):
                leg = pose[f"{side} Leg"]
                shoes.append(G().obs_mesh_shoe(
                    location=leg["Foot Location"], tilt=leg["Foot Tilt"],
                    twist=leg["Foot Twist"], tiptoe=leg["Foot Tiptoe"],
                ))

        with Layout("Arms and Hands"):
            for side in ("Left", "Right"):
                arm  = pose[f"{side} Arm"]
                hand = pose[f"{side} Hand"]

                is_right = side == 'Right'

                hand_node = G().obs_mesh_hand(
                    size         = 0.15,
                    right_hand   = is_right,
                ).node
                for name in hand.signature:
                    hand_node[name] = hand[name]    

                arm_node = G().obs_mesh_arm(
                    location = (0.35, 0.0, 1.1),
                    right_arm=side == 'Right', 
                    size=0.6,
                    hand=hand_node._out,
                    merge=True,
                    ).node
                for name in arm.signature:
                    arm_node[name] = arm[name]

                #obs += node._out.transform(translation=arm["Location"], rotation=(0, 0, pi))
                obs += arm_node._out

        with Layout("Body Posture"):
            obs.transform(translation=body_params["Body Location"],
                          rotation=body_params["Body Rotation"])
            obs += shoes

        obs = Mesh(obs)

        obs.transform(translation=oloc["Location"],
                      rotation=Vector((0, 0, oloc["Direction"])),
                      scale=scale)
        obs.faces._Transparency = transp

        #pose.update(obs)
        obs.out()


def demo():
    """Build animation groups, then the Observer mesh modifier."""
    build_animation()
    build_observer()
