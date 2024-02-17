#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Blender Python Geometry module

Created on Wed Jun 29 17:03:43 2022

@author: alain.bernard
@email: alain@ligloo.net

-----

Vectorized version of Blender function curves. Allow to reuse existing animation curves.
"""


import inspect

import numpy as np    

# ====================================================================================================
# Keying values

def keyed(value, t):
    
    if t is None:
        return None
    
    elif hasattr(value, '__call__'):
        args = inspect.getfullargspec(value).args
        if len(args) == 1 and args[0] == 't':
            return value(t)
        else:
            return value
    
    elif isinstance(value, tuple):
        return tuple([keyed(v, t) for v in value])
    
    else:
        return value


# =============================================================================================================================
# Useful constants

ZERO    = 1e-6
TAU     = np.pi*2
HALF_PI = np.pi/2

BACK      = 1.70158
PERIOD    = 0.3
AMPLITUDE = 0.4

# =============================================================================================================================
# Interpolation function = function such as f(0) = 0 and f(1) = 1
# Immplemented interpolation functions
#
#        'CONSTANT'  : 'tangents': [0, 0]},
#        'LINEAR'    : 'tangents': [1, 1]},
#        'BEZIER'    : 'tangents': [0, 0]},
#        'SINE'      : 'tangents': [0, 1]},
#        'QUAD'      : 'tangents': [0, 1]},
#        'CUBIC'     : 'tangents': [0, 1]},
#        'QUART'     : 'tangents': [0, 1]},
#        'QUINT'     : 'tangents': [0, 1]},
#        'EXPO'      : 'tangents': [10*np.log(2), 0]},
#        'CIRC'      : 'tangents': [0, 0]},
#        'BACK'      : 'EASE_IN',  'tangents': [0, 0]},
#        'BOUNCE'    : 'EASE_OUT', 'tangents': [0, 0]},
#        'ELASTIC'   : 'tangents': [0, 0]},

# ----------------------------------------------------------------------------------------------------
# Interpolation function

class Easing:
    """A standard easing function.
    
    The Easing class from and to the unitary square. The __call__ function
    can be called with a np.array.
    """
    
    EASINGS = {
            'CONSTANT'  : {'can': 'constant',   'left': 0.,   'right': 0.,   'auto':'EASE_IN'}, 
            'LINEAR'    : {'can': 'linear',     'left': 1.,   'right': 1.,   'auto':'EASE_IN'},
            'BEZIER'    : {'can': 'bezier',     'left': None, 'right': None, 'auto':'EASE_IN'},
            'SINE'      : {'can': 'sine',       'left': 0.,   'right': 1.,   'auto':'EASE_IN'},
            'QUAD'      : {'can': 'quadratic',  'left': 0.,   'right': 2.,   'auto':'EASE_IN'},
            'CUBIC'     : {'can': 'cubic',      'left': 0.,   'right': 3.,   'auto':'EASE_IN'},
            'QUART'     : {'can': 'quartic',    'left': 0.,   'right': 4.,   'auto':'EASE_IN'},
            'QUINT'     : {'can': 'quintic',    'left': 0.,   'right': 5.,   'auto':'EASE_IN'},
            'EXPO'      : {'can': 'exponential','left': 0.,   'right': None, 'auto':'EASE_IN'},
            'CIRC'      : {'can': 'circular',   'left': 0.,   'right': 0.,   'auto':'EASE_IN'},
            
            'BACK'      : {'can': 'back',       'left': 0.,   'right': None, 'auto':'EASE_OUT'},
            'BOUNCE'    : {'can': 'bounce',     'left': 0.,   'right': 0.,   'auto':'EASE_OUT'},
            'ELASTIC'   : {'can': 'elastic',    'left': 0.,   'right': None, 'auto':'EASE_OUT'},
           }
    
    def __init__(self, x, y, name='LINEAR', ease='AUTO'):
        """A standard Eassing.
        
        Parameters
        ----------
        name : str, optional
            A valid Easing code. The default is 'LINEAR'.
        ease : str, optional
            A valid ease code. The default is 'AUTO'.

        Returns
        -------
        None.

        """
        
        self.name = name
        self.ease = ease
        
        # Easing parameters
        self.factor    = 10        # Exponential
        self.back      = BACK      # Back
        self.bounces   = 3         # Bounce
        self.period    = PERIOD    # Elastic
        self.amplitude = AMPLITUDE # Elastic
        
        # Corner and Bezier handles
        self.points = np.array(((x, y), (2/3, 0.), (1/3, 0.)))
        
    @staticmethod
    def check_easing(name):
        synos = {
            'QUADRATIC':   'QUAD',
            'QUARTIC':     'QUART',
            'QUINTIC':     'QUINT',
            'EXPONENTIAL': 'EXPO',
            'CIRCULAR':    'CIRC'
            }
        syno = synos.get(name)
        if syno is not None: name = syno
        
        if not name in Easing.EASINGS:
            raise Exception(f"Easing: invalid easing code: '{name}'. must be in {Easing.EASINGS.keys()}.")
            
        return name
        
    @property
    def name(self):
        """The easing code.

        Returns
        -------
        str
            The easing code.
        """
        return self.name_
    
    @name.setter
    def name(self, value):
        
        self.name_ = Easing.check_easing(value)
        
        easing = self.EASINGS.get(self.name_)
            
        setattr(self, 'canonic', getattr(self, '_' + easing['can']))
        self.left_     = easing['left']
        self.right_    = easing['right']
        self.auto_ease = easing['auto']
        
    def __str__(self):
        return f"<Easing {self.name:10s} x: {self.x:5.1f}, y: {self.y:5.1f}, handles: {self.handle_left}, {self.handle_right}>"
    
    def __repr__(self):
        s = f"<Easing {self.name} {self.auto_ease}, x: {self.x:.1f}, y: {self.y:.1f}, handles: {self.handle_left}, {self.handle_right}"
        return s + ">"
    
    def clone(self, delta_x=0.):
        easing = Easing(0., 0., self.name, self.ease)
        
        easing.factor    = self.factor
        easing.back      = self.back
        easing.bounces   = self.bounces
        easing.period    = self.period
        easing.amplitude = self.amplitude
        easing.points    = np.array(self.points)
        
        easing.x += delta_x
        
        return easing
    
    # ----------------------------------------------------------------------------------------------------
    # Corner and Bezier handles

    @property
    def co(self):
        return self.points[0]
    
    @co.setter
    def co(self, value):
        self.points[0] = value
    
    @property
    def x(self):
        return self.points[0, 0]
    
    @x.setter
    def x(self, value):
        self.points[0, 0] = value
    
    @property
    def y(self):
        return self.points[0, 1]
    
    @y.setter
    def y(self, value):
        self.points[0, 1] = value
    
    @property
    def handle_left(self):
        return self.points[0] + self.points[1]
    
    @handle_left.setter
    def handle_left(self, value):
        self.points[1] = list(value) - self.points[0]
    
    @property
    def handle_right(self):
        return self.points[0] + self.points[2]
    
    @handle_right.setter
    def handle_right(self, value):
        self.points[2] = list(value) - self.points[0]
        
    def is_at(self, x):
        return abs(self.x - x) < ZERO
        
    def in_interval(self, x0, x1):
        return (abs(self.x - x0) < ZERO) or (abs(self.x - x1) < ZERO) or (self.x >= x0 and self.x <= x1)
    
    # ----------------------------------------------------------------------------------------------------
    # Left tangent
    
    def left_tangent(self, next_easing=None):
        """Compute left and right tangents.
        
        Left and right tangents are used for extrapolation.

        Returns
        -------
        float
            The left tangent.
        float
            The right tangent.

        """
        
        # ----- Bezier curve dont use left_ & right_ attributes
        
        if self.name == 'BEZIER':
            handle = self.handle_left
            return 0. if abs(handle[0]) < 0 else handle[1]/andle[0]
        
        # ----- Non Bezier
            
        ease = self.auto_ease if self.ease == 'AUTO' else self.ease
        
        if ease == 'EASE_IN':
            tg = self.left_
        elif ease == 'EASE_OUT':
            tg = self.right_
        else:
            tg = self.left_
            
        if tg is None:
            tg = 0.
            
        if next_easing is None:
            return tg
        else:
            return tg*(next_easing.y - self.y)/(next_easing.x - self.x)
        
    # ----------------------------------------------------------------------------------------------------
    # Right tangent
        
    def right_tangent(self, prev_easing=None):
        """Compute left and right tangents.
        
        Left and right tangents are used for extrapolation.

        Returns
        -------
        float
            The left tangent.
        float
            The right tangent.

        """
        
        # ----- Bezier curve dont use left_ & right_ attributes
        
        if self.name == 'BEZIER':
            handle = self.handle_right
            return 0. if abs(handle[0]) < 0 else handle[1]/andle[0]
        
        # ----- Non Bezier
            
        ease = self.auto_ease if self.ease == 'AUTO' else self.ease
        
        if ease == 'EASE_IN':
            tg = self.right_
        elif ease == 'EASE_OUT':
            tg = self.left_
        else:
            tg = self.left_
            
        if tg is None:
            tg = 0.
            
        if prev_easing is None:
            return tg
        else:
            return tg*(self.y - prec_easing.y)/(self.x -prev_easing.x)        

    # ----- The call to the function
    
    def __call__(self, t, next_easing=None):
        """Compute the easing function.
        
        Parameters
        ----------
        t : float or array of floats
            The x values where to compute the easing.

        Returns
        -------
        float or array of floats
            The computed values.
        """
        
        # ----- For debug
        
        if next_easing is None:
            next_easing = Easing(self.x + 1., self.y+1.)

        # ----- Bezier has no canonic computation
        
        if self.name == 'BEZIER':
            return self.bezier_with_next(t, next_easing)
            
        # ----- Need an array of t
        
        if not hasattr(t, '__len__'):
            return self(np.array([t], next_easing=next_easing))[0]
        
        # ----- Let's normalize the parameter
        
        x_amp = next_easing.x - self.x
        y_amp = next_easing.y - self.y
        
        t = (t - self.x)/x_amp
        
        # ------ We compute the canonical function
        
        ease = self.auto_ease if self.ease == 'AUTO' else self.ease

        if (ease == 'EASE_IN'):
            y = self.canonic(t)
        
        elif ease == 'EASE_OUT':
            y = 1 - self.canonic(1 - t)
        
        else:
            y = np.zeros(len(t), float)
                
            idx = t < 0.5
            y[idx] = self.canonic(t[idx]*2)/2
            
            idx = np.logical_not(idx)
            y[idx] = 1 - self.canonic(2 - t[idx]*2)/2

        # ------ Let's return in the target scape
            
        return self.y + y*y_amp
        
    # ===========================================================================
    # The easing functions
    # EASE_IN implementation
    # Argument must be a np.array
    
    # ---------------------------------------------------------------------------
    # Linear

    def _linear(self, t):
        return t

    # ---------------------------------------------------------------------------
    # Constant interpolation
    
    def _constant(self, t):
        y = np.zeros_like(t)
        y[t == 1.] = 1
        return y

    # ---------------------------------------------------------------------------
    # Sine interpolation
    
    def _sine(self, t):
        return 1 - np.cos(t * HALF_PI)

    # ---------------------------------------------------------------------------
    # Quadratic interpolation
    
    def _quadratic(self, t):
        return t*t
    
    # ---------------------------------------------------------------------------
    # Cubic interpolation
    
    def _cubic(self, t):
        return t*t*t
    
    # ---------------------------------------------------------------------------
    # Quartic interpolation
    
    def _quartic(self, t):
        t2 = t*t
        return t2*t2

    # ---------------------------------------------------------------------------
    # Quintic interpolation
    
    def _quintic(self, t):
        t2 = t*t
        return t2*t2*t
    
    # ---------------------------------------------------------------------------
    # Exponential interpolation
    
    def _exponential(self, t):
        return np.power(2, -self.factor * (1. - t))
    
    # ---------------------------------------------------------------------------
    # Circular interpolation
    
    def _circular(self, t):
        return 1 - np.sqrt(1 - t*t)

    # ---------------------------------------------------------------------------
    # Back interpolation
    
    def _back(self, t):
        return t*t*((self.back + 1)*t - self.back)
    
    # ---------------------------------------------------------------------------
    # Bounce interpolation
    
    def _bounce(self, t):

        # Number of bounces
        n = len(self.di)
    
        # Duplicaton of the t for each of the intervals starting abscissa
        # NOTE: 1-t because the computation is made on falling from 1 to 0
        # but the default ease in is time reversed from 0 to 1
    
        ats = np.full((n, len(t)), 1 - t).transpose()
    
        # Distances to the parabola centers
        y = ats - self.ci
    
        # Parabola equation
        # a and di are supposed to be correctly initialized :-)
        y = self.a*y*y + self.di
    
        # Return the max values (normally, only one positive value per line)
    
        return np.max(y, axis=1)  
    
    # ---------------------------------------------------------------------------
    # Bounce utilities
    
    @property
    def bounces(self):
        return len(self.di)
    
    @bounces.setter
    def bounces(self, n):
        """Compute bounces based on xi, di and ci params
    
        Let's name n the number of bounces after the half initial one.
        Each bounces is half of the previouse one. Let's note q the length
        of bounce 0 (the half one).
        The total length is L = q + q/2 + q/4 + ... -q/2
        Hence: L/q = (1-q/2^(n+1))/(1-1/2) - 1/2 = 3/2 - 1/2^n
        We want L = 1, hence 1/q = 3/2 - 1/2^n
    
        Let's note: d = q/2
    
        The equation of the initial parabola (half one) is: y = a(d^2 - x^2)
        At x= 0, y = 1, hence: a = 4/q^2
    
        Each xi is given by: xi = q(3/2-1/2^i)
    
        The parameters are the following:
            - a  : float -> used to compute the parabola a*(t^2 - ??)
            - xi : [0, q/2, q, ... 3/2 - 1/2^i ... 1]
            - di : [q/2, q/2,  ... xi+1 - xi]
            - ci : [0.,  3/2q, ... xi + di/2]
    
        These parameters are computed at initialization time
    
        NOTE that the ease in falls from right to left !
        The parameters must be initialized in consequence :-)
        """        

        r = 2 # Default

        # All but the first half one

        n      = min(7, max(0, n))

        qinv   = 1.5 - 1/r**n
        q      = 1/qinv
        xi     = np.array([q*(1.5 - 1/r**i) for i in range(n+1)])
        xi[-1] = 1
        di     = xi[1:] - xi[:-1]
        a      = 4*qinv*qinv

        self.a  = -a
        self.xi = np.insert(xi[:-1], 0, 0)          # 0, q/2, q, ...
        self.di = np.insert(a * di * di / 4, 0, 1)  # Parabola equation : a*x*x + di
        self.ci = np.insert(xi[:-1] + di/2, 0, 0)            

    # ---------------------------------------------------------------------------
    # Elastic interpolation
    
    def _elastic(self, t):

        period    = .3 if self.period < 0.0001 else self.period
        amplitude = self.amplitude
        
        # t = -np.array(t)  # OUT
        t = -np.array(1-t)  # IN
        f = np.ones_like(t)
        
        if period < 0.0001:
            period = .3
            
        if amplitude < 1:
            
            s = period / 4
            f *= amplitude
                
            ids = np.where(abs(t) < s)[0]
            l = abs(t[ids])/s
            f[ids] = (f[ids]*l) + (1. - l)
            
            amplitude = 1.
            
        else:
            
            s = period / TAU * np.arcsin(1/amplitude)
            
        # return (f * (amplitude * np.power(2, 10*ts) * np.sin((t - s) * twopi / period))) + 1 # OUT
        return -(f * (amplitude * np.power(2, 10*t) * np.sin((t - s) * TAU / period)))      # IN

    # ---------------------------------------------------------------------------
    # Elastic utilities
        
    def set_peramp(self, period=None, amplitude=None, next_point=None):
        
        if next_point is None:
            self.period    = PERIOD if period is None else period
            self.amplitude = AMPLITUDE if amplitude is None else amplitude
        else:
            dx = next_point.x - self.x
            dy = next_point.y - self.y

            self.period    = PERIOD if period is None else period/dx
            self.amplitude = AMPLITUDE if amplitude is None else amplitude/dy
            
    def get_peramp(self, next_point=None):
        if next_point is None:
            return self.period, self.amplitude
        else:
            dx = next_point.x - self.x
            dy = next_point.y - self.y
            return self.period*dx, self.amplitude*dy
    
    # ---------------------------------------------------------------------------
    # Bezier interpolation
    
    def bezier_with_next(self, t, next_easing=None):
        
        if next_easing is None:
            return np.ones_like(t)*self.y
        
        # ----- Bezier computation
        # Q = (1-t)^3P0 + 3t(1-t)^2P1 + 3t^2(1-t)P2 + t^3P3
        # P0 : 1 - 3t + 3t^2 - t^3
        # P1 : 3t - 6t^2 + 3t^3
        # P2 : 3t^2 - 3t^3
        # P3 : t^3
        #
        # Q = t^3(-P0 + 3P1 - 3P2 + P3) + t^2.3(P0 - 2P1 + P2) + t.3(-P0 + P1) + P0
        # P(0) = P0
        # P(1) = P3
        #
        # Let's note:
        # B0 = P3 - 3P2 + 3P1 - P0
        # B1 = 3(P0 - 2P1 + P2)
        # B2 = 3(P1 - P0)
        # B3 = P0
        #
        # We have:
        #
        # Q = t^3.B0 + t^2.B1 + t.B2 + P0 = t(t(t.B0 + B1) + B2) + P0
        #
        # Here:
        # P0 = self.x y
        # P1 = self.right_handle
        # P2 = other.left_handle
        # P3 = other.x y
        
        B = [
            next_easing.y - 3*next_easing.handle_left[1] + 3*self.handle_right[1] - self.y,
            3*(self.y - 2*self.handle_right[1] + next_easing.handle_left[1]),
            3*(self.handle_right[1] - self.y),
            self.y,
            ]
        
        # DEBUG
        
        if False:
            print("BEZIER WITH NEXT")
            print("P0", self.co)
            print("P1", self.handle_right)
            print("P2", next_easing.handle_left)
            print("P3", next_easing.co)
            
            P0 = self.co
            P1 = self.handle_right
            P2 = next_easing.handle_left
            P3 = next_easing.co
            
            B0 = P3 - 3*P2 + 3*P1 - P0
            B1 = 3*(P0 - 2*P1 + P2)
            B2 = 3*(P1 - P0)
            B3 = P0
        
            B = [B0[1], B1[1], B2[1], B3[1]]
            
        if np.shape(t) == ():
            u = (t - self.x)/(next_easing.x - self.x)
        else:
            u = (np.array(t) - self.x)/(next_easing.x - self.x)

        return u*(u*(u*B[0] + B[1]) + B[2]) + B[3]

    
    # ---------------------------------------------------------------------------
    # Bezier interpolation
    # CANONICAL VERSION 
    # NOT USED ANYMORE
    
    def _bezier(self, t):
        
        # Bounds of dychotomy computation
        t0 = np.zeros(len(t), float)
        t1 = np.ones(len(t), float)
        
        # t --> (x, y) points
        # Loop until x = t with a certain precision

        # ----- Bezier computation        
        # P = _u3*P0 + 3*_u2*u*P1 + 3*_u*u2*P2 +  u3*P3
        # P0 = (0, 0) -> No term in P0
        # P# = (1, 1) -> Non P3
        
        u = np.array(t)
        x1 = self.P1[0]
        x2 = self.P2[0]
        
        zero = 0.001
        
        for i in range(15):

            u2   = u*u
            u3   = u2*u

            _u  = 1 - u
            _u2 = _u*_u

            x = 3*_u2*u*x1 +  3*_u*u2*x2 + u3
            ds = x - t
            if max(abs(ds)) < zero:
                break
            
            ineg = ds < -zero
            t0[ineg] = u[ineg] 
            
            ipos = ds > zero
            t1[ipos] = u[ipos] 
            
            ich = np.logical_or(ineg, ipos)
            u[ich] = (t0[ich] + t1[ich])/2

        return 3*_u2*u*self.P1[1] +  3*_u*u2*self.P2[1] + u3
    

    # ===========================================================================
    # From / to blender keyframe

    @classmethod
    def FromKFPoint(cls, kf, next_point=None):
        
        easing = cls(kf.co.x, kf.co.y, name=kf.interpolation, ease=kf.easing)
        
        easing.set_peramp(kf.period, kf.amplitude, next_point)
        easing.back         = kf.back
        easing.handle_left  = kf.handle_left
        easing.handle_right = kf.handle_right

        return easing
    
    def to_kf_point(self, kf, next_easing=None):
        
        from mathutils import Vector
        
        kf.type          = 'KEYFRAME'
        kf.interpolation = self.name
        kf.easing        = self.ease
        kf.co            = Vector(self.co)

        kf.handle_left_type  = 'FREE'
        kf.handle_right_type = 'FREE'
        kf.handle_left   = Vector(self.handle_left)
        kf.handle_right  = Vector(self.handle_right)

        kf.back          = self.back
        p, a = self.get_peramp(next_easing)
        kf.period        = p
        kf.amplitude     = a
        
        return kf
    
# ====================================================================================================
# Function    
    
class Function(list):
    
    BACK = 1.70158
    
    EXTRAPOLATIONS = ['CONSTANT', 'LINEAR', 'PERIODIC']
    
    """A collection of easing functions mapped on intervals.
    """
    
    def __init__(self, default_value=0., extrapolation='CONSTANT'):
        """A collection of easing functions mapped on intervals.        

        Parameters
        ----------
        extrapolation : str, optional
            A valid extrapolation code. The default is 'CONSTANT'.

        Returns
        -------
        None.
        """
        super().__init__()
        self.extrapolation = extrapolation
        self.default_value = default_value
        
        if extrapolation not in Function.EXTRAPOLATIONS:
            raise Exception(f"Function extrapolation '{extrapolation}' is not valid, should be in {Function.EXTRAPOLATIONS}!")
        
    def __repr__(self):
        s = f"<Function {len(self)} easing(s), extrapolation: {self.extrapolation}"
        for i, e in enumerate(self):
            s += f"\n  {i:2d}: {e}"
            
        return s + ">"
    
    # ----------------------------------------------------------------------------------------------------
    # Properties
    
    @property
    def x0(self):
        if len(self) == 0:
            return 0.
        else:
            return self[0].x
        
    @property
    def x1(self):
        if len(self) == 0:
            return 0.
        else:
            return self[-1].x
        
    def check(self):
        for i in range(1, len(self)):
            if self[i].x < self[i-1].x or self[i].is_at(self[i-1].x):
                print(f"Function check error at {i-1} -> {i}:", self)
                return False
        print(f"Function check: OK")
        return True
    
    # ===========================================================================
    # From a function
    
    @classmethod
    def FromValues(cls, values, x0=0., x1=1.):
        
        assert(np.shape(values) != ())
        
        dx = (x1 - x0)/(len(values) - 1)
        func = cls()
        
        for i, v in enumerate(values):
            func.append(Easing(x0 + i*dx, v, 'LINEAR'))
            
        return func
    
    # ===========================================================================
    # From a function
    
    @classmethod
    def FromFunction(cls, f, t0=0., t1=1., count=10, interpolation='BEZIER'):
        
        P = np.zeros((count, 2), float)
        
        P[:, 0] = np.linspace(t0, t1, count)
        P[:, 1] = f(P[:, 0])
        
        delta = (t1 - t0)/(count - 1)

        dt = delta/100
        tg = (f(P[:, 0] + dt) - f(P[:, 0] - dt))*(1.5*delta/dt)
        
        func = cls()
        for i in range(count):
            easing = Easing(0, 0, interpolation)
            easing.points[0] = P[i]
            easing.points[1] = - tg[i]
            easing.points[2] = + tg[i]
            
            func.append(easing)
            
        return func
    
    # ====================================================================================================
    # Blender read / write
        
    # ---------------------------------------------------------------------------
    # From fcurve
        
    @classmethod
    def FromFCurve(cls, fcurve):
        """Generate a Function from a Blender fcurve.        

        Parameters
        ----------
        fcurve : Blender fcurbe
            The fcurve to copy.

        Returns
        -------
        Function
            A Function instance.
        """

        func = cls()
        func.extrapolation = fcurve.extrapolation
        
        kfs = fcurve.keyframe_points        
        for i, kf in enumerate(kfs):
            next_point = None if i == len(kfs) - 1 else kfs[i+1].co
            func.add_easing(Easing.FromKFPoint(kf, next_point))
            
        return func
    
    # ---------------------------------------------------------------------------
    # To fcurve
    
    def to_fcurve(self, fc):
        
        kfs = fc.keyframe_points
        
        kfs.clear()
        kfs.add(len(self))
        
        for i, kf in enumerate(kfs):
            easing = self[i]
            next_easing = None if i == len(self) - 1 else self[i+1]
            self[i].to_kf_point(kf, next_easing=next_easing)
            
        return fc
    
    # ---------------------------------------------------------------------------
    # From data path
    
    @classmethod
    def FromKeyFrames(cls, spec, data_path, index=-1):
        
        from geopy import blender
        
        return cls.FromFCurve(blender.get_fcurve(spec, data_path, index=index, create=False))
    
    # ---------------------------------------------------------------------------
    # From data path
    
    def to_key_frames(self, spec, data_path, index=-1):
        
        from geopy import blender
        
        fc = blender.get_fcurve(spec, data_path, index=index, create=True)
        return self.to_fcurve(fc)
    
    # ---------------------------------------------------------------------------
    # Compute
    
    def __call__(self, x):
        """Compute the blender curve on a array of values.
        
        xBounds and yBounds can provide bounds per value in t.
        This allow to use a curve on various intervals
        
        Parameters
        ----------
        t : array of floats
            The abscissa of the curve
        xbounds : array of couple of floats, optional
            One interval per value to use as the replacement of the default interval.
        ybounds : array of couple of floats, optional
            One interval per value to use as the replacement of the default y interval.
            
        Returns
        -------
        array of float
            The curve values
        """
        
        # ----- Empty or one easing
        
        if len(self) == 0:
            return np.ones_like(x).astype(float)*self.default_value
        
        elif len(self) == 1:
            return np.ones_like(x).astype(float)*self[0].y

        # ----- Work with an array of values
        
        if np.shape(x) == ():
            return self([x])[0]
        
        # ----- Let's go 
        
        x = np.array(x, float)
        y = np.zeros_like(x)
        
        x0 = self.x0
        x1 = self.x1
        
        # ----- Extrapolation
        
        if self.extrapolation == 'CONSTANT':
            x = np.clip(x, x0, x1)
            
        elif self.extrapolation == 'PERIODIC':
            xm, x_, dx, xmod  = np.min(x), x, x1 - x0, (x - x0) % (x1 - x0)
            x = x0 + ((x - x0) % (x1 - x0))
            
        else:
            # Before
            
            sel = np.where(x < self[0].x)
            if np.sum(sel) > 1:
                y[sel] = self[0].left_tangent(self[1])*x[sel]
            
            # After
    
            sel = np.where(x >= self[-1].x)
            if np.sum(sel) > 1:
               y[sel] = self[-1].left_tangent(self[-1])*x[sel]
        
        # ----- Loop
        
        for easing, next_easing in zip(self[:-1], self[1:]):
            sel = np.logical_and(x >= easing.x, x <= next_easing.x)
            if np.sum(sel) > 0:
                y[sel] = easing(x[sel], next_easing)
                
        # ----- Done
        
        return y
    
    # ---------------------------------------------------------------------------
    # To curve
    
    def to_curve(self, count=100):
        
        from geopy.core.curvebuilder import CurveBuilder
        
        if len(self) < 2:
            return None
        
        verts = np.zeros((count, 3), float)
        
        verts[:, 0] = np.linspace(self[0].x, self[-1] .x, count)
        verts[:, 2] = self(verts[:, 0])
        
        cb = CurveBuilder()
        cb.add_splines(verts)
        
        return cb
    
    # ====================================================================================================
    # Construction
    
    # ----------------------------------------------------------------------------------------------------
    # Insertion index
    
    def insertion_index(self, x):
        # returns : index, replace (True) or insert (False)
        # if index is None: append
        
        for index, easing in enumerate(self):
            if abs(easing.x - x) < ZERO:
                return index, True
            
            elif x < easing.x:
                return index, False
            
        return None, None
    
    # ----------------------------------------------------------------------------------------------------
    # Normalize Bezier handles after an insertion
    
    def normalize_bezier(self, index0, index1):
        if index0 < 0 or index1 >= len(self):
            return
        
        easing0 = self[index0]
        easing1 = self[index1]
        
        width  = easing1.x - easing0.x
        
        easing0.handle_right = (easing0.x + width/3, easing0.y)
        easing1.handle_left  = (easing1.x - width/3, easing1.y)
    
    # ----------------------------------------------------------------------------------------------------
    # Add an easing the curve
    
    def add_easing(self, easing):
        """Add and easing to the function.

        Typical use is to append a new easing at the end of existing ones,
        but if the end point is not after the current end point, the easing
        is inserted within the existing ones.

        Parameters
        ----------
        end_point : point
            End of the easing.
        easing : Easing, optional
            The easing to use. The default is Easing('LINEAR', 'AUTO').

        Returns
        -------
        int
            The index of the created easing with the BCurve.
        """
        
        # ----- Insertion point
        
        index, replace = self.insertion_index(easing.x)
        
        # ----- Append or insert the easing
        
        if index is None:
            self.append(easing)
            index = len(self) - 1
            
        elif replace:
            self[index] = easing
            
        else:
            self.insert(index, easing)
            
        # ----- Normalize the Bezier handles
        
        self.normalize_bezier(index-1, index)
        self.normalize_bezier(index, index+1)

        return self[index]
    
    # ----------------------------------------------------------------------------------------------------
    # Replace an easing
    
    def replace(self, index, easing):
        assert(self[index].is_at(easing.x))
        # Keep the left handle
        easing.points[1] = self[index].points[1]
        
        self[index] = easing
    
    # ----------------------------------------------------------------------------------------------------
    # Delete indices
    
    def del_selection(self, indices):
        for i in reversed(sorted(indices)):
            del self[i]
    
    # ----------------------------------------------------------------------------------------------------
    # Indices in a interval
    
    def indices_in_interval(self, x0, x1):
        return [i for i in range(len(self)) if self[i].in_interval(x0, x1)]
    
    # ----------------------------------------------------------------------------------------------------
    # Add a list of easings
    
    def paste(self, easings, delta=0):
        x0 = easings[0].x  + delta
        x1 = easings[-1].x + delta
        self.del_selection(self.indices_in_interval(x0, x1))
        
        index, replace = self.insertion_index(x0)
        if index is None:
            self.extend(easings)
        else:
            for easing in reversed(easings):
                self.insert(index, easing)
    
    # ----------------------------------------------------------------------------------------------------
    # Add a key frame
    
    def add(self, x, y, interpolation=None, ease='AUTO'):

        back = None
        
        # ----- Interpolation
        
        if interpolation is None:
            if len(self) == 0:
                interpolation = 'LINEAR'
            else:
                index, replace = self.insertion_index(x)
                if index is None:
                    interpolation = self[-1].name
                elif replace or index == 0:
                    interpolation = self[index].name
                else:
                    interpolation = self[index-1].name
                    
        elif not isinstance(interpolation, str):
            back = interpolation
            interpolation = 'BACK'
                    
        # ----- Add the easing
        
        easing = Easing(x, y, name=interpolation, ease=ease)
        if back is not None:
            easing.back = back

        return self.add_easing(easing)
        
    # ====================================================================================================
    # Building methods        
    
    # ----------------------------------------------------------------------------------------------------
    # Ad a pick
    
    def add_peak(self, x, width, y0, y1, interpolation='BEZIER', quick=False):
        
        x0 = x - width/2
        x1 = x + width/2
        
        if interpolation == 'CONSTANT':
            self.add(x0, y1, 'CONSTANT')
            
        else:
            self.add(x0, y0, interpolation, ease='EASE_IN' if quick else 'EASE_OUT')
            self.add(x,  y1, interpolation, ease='EASE_OUT' if quick else 'EASE_IN')
        
        return self.add(x1, y0, 'CONSTANT')
    
    # ----------------------------------------------------------------------------------------------------
    # Add a change from one value to another
            
    def add_change(self, x, width, y0, y1, interpolation='BEZIER', quick=False):
        
        ease = 'EASE_IN' if quick else 'EASE_OUT'
        self.add(x, y0, interpolation, ease=ease)
        return self.add(x + width, y1, 'CONSTANT', ease=ease)
    
    # ----------------------------------------------------------------------------------------------------
    # Add an interval
            
    def add_interval(self, x0, x1, width, y0, y1, interpolation='BEZIER', quick=False):

        self.add_change(x0, width, y0, y1, interpolation=interpolation, quick=quick)
        return self.add_change(x1 - width, width, y1, y0, interpolation=interpolation, quick=not quick)
        
    # ----------------------------------------------------------------------------------------------------
    # Add bounces
        
    def add_bounces(self, x, width, y0, y1, starting=False, count=3):
        
        ease = 'EASE_IN' if starting else 'EASE_OUT'
        easing = self.add(x, y0, interpolation='BOUNCE', ease=ease)
        easing.bounces = count
        return self.add(x + width, y1, interpolation='CONSTANT')
    
    # ----------------------------------------------------------------------------------------------------
    # Add elastic
        
    def add_elastic(self, x, width, y0, y1, starting=False, period=None, amplitude=None):

        ease = 'EASE_IN' if starting else 'EASE_OUT'
        easing = self.add(x, y0, interpolation='ELASTIC', ease=ease)
        next_easing = self.add(x + width, y1, interpolation='CONSTANT')
        easing.set_peramp(period, amplitude, next_point = next_easing)
        
        return next_easing
    
    # ----------------------------------------------------------------------------------------------------
    # Add sine
    
    def add_half_sine(self, x, width, y0, y1):
        
        self.add_change(x, width/2, y0, y1, 'SINE', quick=False)
        return self.add_change(x + width/2, width/2, y1, y0, 'SINE', quick=True)
    
    def add_sine(self, x, width, y0, y1, count=1):
        w = width / count
        for i in range(count):
            easing = self.add_half_sine(x + w*i, w, y0, y1*(1 if i%2 == 0 else -1))
        return easing
    
    
    # ====================================================================================================
    # Operations
    
    # ----------------------------------------------------------------------------------------------------
    # Translation
    
    def translate(self, delta_x=0., delta_y=0.):
        for easing in self:
            easing.points[0] += (delta_x, delta_y)

    # ----------------------------------------------------------------------------------------------------
    # Scaling
    
    def scale(self, scale_x=None, scale_y=None, pivot_x=0., pivot_y=0.):
        for easing in self:
            if scale_x is not None:
                easing.x -= pivot_x
                easing.points[:, 0] *= scale_x
                easing.x += pivot_x
                
            if scale_y is not None:
                easing.y -= pivot_y
                easing.points[:, 1] *= scale_y
                easing.y += pivot_y
                
    def normalize(self, x_max=None, y_max=None):
        
        scale_x, scale_y = None, None
        
        if x_max is not None:
            scale_x = x_max/self.x1
            
        if y_max is not None:
            scale_y = y_max/np.max(self(np.linspace(self.x0, self.x1, 1000)))
            
        self.scale(scale_x, scale_y)
                
    # ----------------------------------------------------------------------------------------------------
    # Multiplying
    
    def multiply(self, f):
        for easing in self:
            easing.y = easing.y*f(easing.x)

    # ----------------------------------------------------------------------------------------------------
    # Noise
    
    @staticmethod
    def get_noise(scale, count, seed):

        rng = np.random.default_rng(seed)
        
        try:
            from mathutils import noise

            pts = rng.uniform(0, scale, (count, 3))
            
            return np.array([noise.noise(pt) for pt in pts])
        
        # DEBUG
        except:
            return rng.uniform(0, 1, count)
            
    def noise_add(self, amplitude=1, scale=1., count=None, add=True, seed=0):
        
        npts = len(self) if count is None else count
        
        noise = Function.get_noise(scale, npts, seed)
        if add:
            noise -= .5
            noise *= 2
        
        if count is None:
            for easing, v in zip(self, noise):
                if add:
                    easing.y += v*amplitude
                else:
                    easing.y *= v*amplitude
                
        else:
            dx = (self.x1 - self.x0)/(count - 1)
            new_easings = []
            for i, v  in enumerate(noise):
                x = self.x0 + i*dx
                if add:
                    new_easings.append(Easing(x, self(x) + amplitude*v))
                else:
                    new_easings.append(Easing(x, self(x)*amplitude*v))
                
            self.clear()
            self.extend([easing for easing in new_easings])
        
                
    # ----------------------------------------------------------------------------------------------------
    # Duplication
                
    def duplicate(self, indices=None, to_x=None, count=1):
        
        # ----- List of easings to duplicate
        
        if indices is None:
            indices = range(len(self))
            
        easings = [self[i].clone() for i in indices]
        if len(easings) == 0:
            return
        
        width = easings[-1].x - easings[0].x

        # ----- Where to locate the duplicates
        
        if to_x is None or to_x < easings[0].x + width:
            to_x = easings[-1].x

        delta = to_x - easings[0].x
        stick = easings[-1].is_at(easings[0].x + delta)
            
        # ----- Delete the target interval

        sel = self.indices_in_interval(to_x, to_x + width*count)
        self.del_selection(sel)
        
        # ----- Where to insert the duplicates

        index, replace = self.insertion_index(to_x)
        if index is None:
            index = len(self)
        
        # ----- Loop on the number of duplications
        
        for i_dupl in range(count):

            # Loop on the easings to duplicate
            
            for i in range(len(easings)):
                
                easing = easings[i].clone(delta*(i_dupl + 1))
                if i == 0 and replace:
                    self[index] = easing
                else:
                    self.insert(index + i, easing)
                    index += 1
                    
                if i == 0:
                    self.normalize_bezier(index-1, index)
                    
                if i == len(easings) - 1:
                    self.normalize_bezier(index, index+1)
                    
            if stick:
                replace = True
                index -= 1
                    
    # ====================================================================================================
    # Integral
    # When the y values are a speed relative to x, the integral allows
    # to get the location at time x

    def integral(self, t0, t1, count=100):
        """Compute the integral of the BCurve between to values.

        Note that if t1 is an array of float, t0 can be a single float value.
        If t0 is an array, it must be of the same shape as t1.        

        Parameters
        ----------
        t0 : float or array of floats
            Start value.
        t1 : float or array of floats
            End value.
        count : int, optional
            Number of steps to use to compute the integral. The default is 100.

        Returns
        -------
        float or array of floats
            The integral or array of integrals.
        """
        
        shape = np.broadcast_shapes(np.shape(t0), np.shape(t1))
        
        if shape == ():
            x = np.linspace(t0, t1, count)
            return np.sum(self(x), axis=-1) * ((t1 - t0)/(count-1))
        
        x0 = np.empty(shape, float)
        x1 = np.empty(shape, float)
        x0[:] = t0
        x1[:] = t1
        
        x = np.linspace(x0, x1, count).T
        
        return np.sum(self(x), axis=-1) * ((x1 - x0)/(count-1))

    # ---------------------------------------------------------------------------
    # Primitive
    
    def primitive(self, count=100):
        
        x0 = self.x0
        x1 = self.x1
        dx = (x1 - x0)/(count - 1)
        
        if True:
            x = np.linspace(x0, x1, count*10)
            h = np.sum(np.reshape(self(x), (count, 10)), axis=-1)*(dx/10)
            y = np.append([0.], np.cumsum(h)[:-1])
        else:
            y = np.zeros(count, float)
            for i in range(1, count):
                y[i] = self.integral(x0, x0 + dx*i, count=i*10)
                
        return Function.FromValues(y, x0, x1)
    
    def derivative(self, count=100):
        x0 = self.x0
        x1 = self.x1
        x = np.linspace(x0, x1, count)
        dx = (x1 - x0)/(count - 1)/100
        
        y = (self(x + dx) - self(x - dx))/(2*dx)
        return Function.FromValues(y, x0, x1)
                
    


# =============================================================================================================================
# Test

if __name__ == '__main__':

    import matplotlib.pyplot as plt
    
    # ====================================================================================================
    # Easings
    
    def plot_easing(easing, xax=None, count=100):
        
        if xax is None:
            fig, ax = plt.subplots()
        else:
            ax = xax
            
        x = np.linspace(0., 1., count)
        ax.plot(x, easing(x))
        
        if xax is None:
            ax.set(title=easing.name + '- ' + easing.ease)
            plt.show()
            
    def plot_bezier(points0, points1):
        e0 = Easing(0, 0, 'BEZIER')
        e0.points = np.array(points0)
        e1 = Easing(0, 0, 'BEZIER')
        e1.points = np.array(points1)
        
        fig, ax = plt.subplots()
        
        x = np.linspace(e0.x, e1.x, 100)
        y = e0(x, e1)
        
        ax.plot(x, y)
        
        plt.show()
    
            
    def plot_easings(ease='AUTO', codes=None, count=100):
        
        for name in Easing.EASINGS:
            if codes is None or name in codes:
                
                fig, ax = plt.subplots()
                ax.set(title=name)
                
                for ease in ['EASE_IN', 'EASE_OUT']:
                    easing = Easing(0, 0, name, ease=ease)
                    print(f"Plot {name}: {easing.ease}")
                    plot_easing(easing, xax=ax, count=count)
            
                plt.show()

                easing = Easing(0, 0, name, ease='AUTO')
                print(f"Plot {name}: {easing.ease}")
                plot_easing(easing, xax=None, count=count)
                
    # ====================================================================================================
    # Functions
    
    def plot_function(f, title="Function", count=1000, ax=None):
        
        owner = ax is None
            
        if owner:
            fig, ax = plt.subplots()
            
        x = np.linspace(f[0].x-1, f[-1].x + 1, count)

        ax.plot(x, f(x))
        
        if title is not None:
            plt.title(title)
            
        if owner:
            plt.show()
            
    def function_all():
        
        f = Function()

        for i, name in enumerate(Easing.EASINGS):
            #for ease in ['EASE_IN', 'EASE_OUT', 'EASE_IN_OUT']:
            easing = Easing(i, i, name)
            f.add_easing(easing)
                
        return f
    
    def some_functions():
        
        # ----- Picks
        
        f = Function()
        f.add_peak(10, 5, 0, 3)
        f.add_peak(20, 5, 0, 4, 'BEZIER')
        f.add_peak(30, 5, 0, 3, 'CONSTANT')
        f.add_peak(40, 5, 0, 4, Function.BACK, quick=True)
        
        plot_function(f, 'Peaks')

        # ----- Intervals
        
        for quick in [False, True]:
            f = Function()
            f.add_interval(10, 20, 3, 0, 3, 'QUARTIC', quick=quick)
            f.add_interval(22, 32, 3, 0, 3, 'SINE', quick=quick)
            f.add_interval(34, 46, 3, 0, 3, 'CIRC', quick=quick)
            f.add_interval(48, 60, 3, 0, 3, 1.5, quick=quick)
            
            plot_function(f, f"Intervals: quick {quick}")
            
        # ----- Bounces
        
        f = Function()
        f.add_bounces(10, 5, 0, 3, False)
        f.add_bounces(20, 5, 3, 0, True, count=2)

        plot_function(f, f"Bounces")
        
        # ----- Elastic
        
        f = Function()
        f.add_elastic(10, 5, 3, False)
        f.add_elastic(17, 5, 0, True, period=.6, amplitude=1)

        plot_function(f, f"Elastic")
        
        # ----- Duplication
        
        f = Function()
        f.add_peak(5, 2, 0, 3, interpolation=Function.BACK, quick=True)
        
        f.duplicate(count=2)
        f.duplicate(to_x=f.x1 + 1)
        
        f.duplicate(range(3), to_x = 20)
        
        plot_function(f, f"Duplicate")
        
        # ----- Sine

        f = Function()
        f.add_sine(x=0, width=20, y0=0, y1=5, count=7)
        f.multiply(lambda x: x**2/400)
        
        plot_function(f, f"Sine")

        # ----- From function
        
        f = Function.FromFunction(lambda x: np.sin(x)/x, t0=-15, t1=+15, count=100, interpolation='LINEAR')
        
        plot_function(f, f"Function")
        
        # ----- Noise
        
        fig, ax = plt.subplots()
        
        f = Function.FromFunction(lambda x: np.sin(x), t0=-np.pi*3, t1=np.pi*3, count=11, interpolation='BEZIER')
        plot_function(f, f"Add Noise", ax=ax)
        
        f.noise_add(amplitude=3)
        plot_function(f, None, ax=ax)
        
        f.noise_add(amplitude=3, count=100)
        plot_function(f, None, ax=ax)
        
        plt.show()
        
        fig, ax = plt.subplots()
        
        f = Function.FromFunction(lambda x: np.sin(x), t0=-np.pi*3, t1=np.pi*3, count=11, interpolation='BEZIER')
        plot_function(f, f"Mult Noise", ax=ax)
        
        f.noise_add(amplitude=1, add=False)
        plot_function(f, None, ax=ax)
        
        f.noise_add(amplitude=1, count=100, add=False)
        plot_function(f, None, ax=ax)
        
        plt.show()
        
        # ----- Integral
        
        fig, ax = plt.subplots()
        
        x0 = 0
        x1 = 3
        
        f = Function()
        f.add_change(x0, x1 - x0, 0, 3, 'LINEAR')
        
        plot_function(f, title="Integral", ax=ax)
        
        #y = f.integral(x0, np.linspace(x0+.1, x1, 100))
        #f = Function.FromValues(y, x0, x1)
        
        prim = f.primitive()
        plot_function(prim, title=None, ax=ax)
        
        der = prim.derivative()
        plot_function(der, title=None, ax=ax)
        
        plt.show()
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
                
    # Tests
    
    #plot_easings()
    #plot_function(function_all())
    some_functions()
    

                
                
        

    
    
    


