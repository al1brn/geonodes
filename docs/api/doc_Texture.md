Class Texture

## Properties

### bl_idname

         Shortcut for `self.bsocket.bl_idname`
        


### bnode

         Shortcut for `self.bsocket.node`
        


### is_multi_input

         Shortcut for `self.bsocket.is_multi_output`
        


### is_output

         Shortcut for `self.bsocket.is_output`
        


### links

         Shortcut for `self.bsocket.links`
        


### name

         Shortcut for `self.bsocket.name`
        


### node_chain_label

         Shortcut for *self.node.chain_label*
        


### socket_index

         Return the index of the socket within the list of node sockets.
        
        Depending on the _is_output_ property, the socket belongs either to *node.inputs* or
        *node.outputs*.
        



## Class and static methods

### Input

```python
@classmethod
def Input(cls, value=None, name="Texture", description="")
```

         Create a Texture input socket in the Group Input Node
        
        Args:
            name: The socket name
            description: User tip
            
        Returns:
            Texture: The Texture data socket
        



### brick

```python
@staticmethod
def brick(vector=None, color1=None, color2=None, mortar=None, scale=None, mortar_size=None, mortar_smooth=None, bias=None, brick_width=None, row_height=None, offset=0.5, offset_frequency=2, squash=1.0, squash_frequency=2)
```

         Node BrickTexture.

        Node reference [Brick Texture](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/texture/brick.html)
        Developer reference [ShaderNodeTexBrick](https://docs.blender.org/api/current/bpy.types.ShaderNodeTexBrick.html)

        Args:
            vector: Vector
            color1: Color
            color2: Color
            mortar: Color
            scale: Float
            mortar_size: Float
            mortar_smooth: Float
            bias: Float
            brick_width: Float
            row_height: Float
            offset (float): 0.5
            offset_frequency (int): 2
            squash (float): 1.0
            squash_frequency (int): 2

        Returns:
            tuple ('color', 'fac')
        


### checker

```python
@staticmethod
def checker(vector=None, color1=None, color2=None, scale=None)
```

         Node CheckerTexture.

        Node reference [Checker Texture](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/texture/checker.html)
        Developer reference [ShaderNodeTexChecker](https://docs.blender.org/api/current/bpy.types.ShaderNodeTexChecker.html)

        Args:
            vector: Vector
            color1: Color
            color2: Color
            scale: Float

        Returns:
            tuple ('color', 'fac')
        


### get_bl_idname

```python
@staticmethod
def get_bl_idname(class_name)
```

         Get the node socket bl_idname name from the Socket class
        
        :param class_name: The class name
        :type class_name: str
        :return: The bl_idname associated to this class name
        :rtype: str
        
        Used to create a new group input socket. Called in `DataClass.Input` method to determine
        which socket type must be created.
        
        Note that here the class_name argument accepts additional values which correspond to *sub classes*:
            
        .. list-table:: 
           :widths: 20 40
           :header-rows: 0
        
           * - Unsigned
             - Integer sub class (NodeSocketIntUnsigned)
           * - Factor
             - Float sub class (NodeSocketFloatFactor)
           * - Angle
             - Float sub class  (NodeSocketFloatAngle)
           * - Distance
             - Float sub class (NodeSocketFloatDistance)
           * - Rotation
             - Vector sub class (NodeSocketVectorEuler)
           * - xyz
             - Vector sub class (NodeSocketVectorXYZ)
           * - Translation
             - Vector sub class (NodeSocketVectorTranslation)
          
        These additional values allow to enter angle, distance, factor... as group input values.
        



### get_class_name

```python
@staticmethod
def get_class_name(socket, with_sub_class = False)
```

         Get the DataSocket class name corresponding to the socket type and name.
        
        :param socket: The socket to determine the class of
        :param with_sub_class: Return the sub class if True
        :typ socket: bpy.types.NodeSocket, Socket
        :type with_sub_class: bool
        :return: The name of the class associated to the bl_idname of the socket
        :rtype: str
        
        .. list-table:: Correspondance table
           :widths: 30 20 20
           :header-rows: 1
           
           * - NodeSocket
             - class name
             - sub class name
           * - NodeSocketBool 
             - 'Boolean'
             - 
           * - NodeSocketInt 
             - 'Integer'
             - 
           * - NodeSocketIntUnsigned 
             - 'Integer'
             - 'Unsigned'
           * - NodeSocketFloat 
             - 'Float' 
             - 
           * - NodeSocketFloatFactor 
             - 'Float'
             - 'Factor'
           * - NodeSocketFloatAngle  
             - 'Float'
             - 'Angle'
           * - NodeSocketFloatDistance 
             - 'Float'
             - 'Distance'
           * - NodeSocketVector 
             - 'Vector'
             - 
           * - NodeSocketVectorEuler 
             - 'Vector'
             - 'Rotation'
           * - NodeSocketVectorXYZ 
             - 'Vector'
             - 'xyz'
           * - NodeSocketVectorTranslation 
             - 'Vector'
             - 'Translation'
           * - NodeSocketColor 
             - 'Color'
             - 
           * - NodeSocketString' 
             - 'String'
             - 
           * - NodeSocketCollection 
             - 'Collection'
             - 
           * - NodeSocketImage 
             - 'Image'
             - 
           * - NodeSocketMaterial 
             - 'Material'
             - 
           * - NodeSocketObject 
             - 'Object'
             - 
           * - NodeSocketTexture 
             - 'Texture'
             - 
           * - NodeSocketGeometry
             - 'Geometry'
             - 
          
          
        If the name of the socket is in ['Mesh', 'Points', 'Instances', 'Volume', 'Spline', 'Curve', 'Curves'],
        the name is chosen as the class name.
        


### gives_bsocket

```python
@staticmethod
def gives_bsocket(value)
```

         Test if the argument provides a valid output socket.
        
        :param value: The value to test
        :type value: any
        :return: True if *value* is or wraps a socket
        :rtype: bool
        
        Returns True if value is:
            
        - A Blender Geometry Node Socket
        - An instance of Socket        
        



### gradient

```python
@staticmethod
def gradient(vector=None, gradient_type='LINEAR')
```

         Node GradientTexture.

        Node reference [Gradient Texture](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/texture/gradient.html)
        Developer reference [ShaderNodeTexGradient](https://docs.blender.org/api/current/bpy.types.ShaderNodeTexGradient.html)

        Args:
            vector: Vector
            gradient_type (str): 'LINEAR' in [LINEAR, QUADRATIC, EASING, DIAGONAL, SPHERICAL, QUADRATIC_SPHERE, RADIAL]

        Returns:
            tuple ('color', 'fac')
        


### gradient_diagonal

```python
@staticmethod
def gradient_diagonal(vector=None)
```

         Node GradientTexture.

        Node reference [Gradient Texture](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/texture/gradient.html)
        Developer reference [ShaderNodeTexGradient](https://docs.blender.org/api/current/bpy.types.ShaderNodeTexGradient.html)

        Args:
            vector: Vector

        Returns:
            tuple ('color', 'fac')
        


### gradient_easing

```python
@staticmethod
def gradient_easing(vector=None)
```

         Node GradientTexture.

        Node reference [Gradient Texture](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/texture/gradient.html)
        Developer reference [ShaderNodeTexGradient](https://docs.blender.org/api/current/bpy.types.ShaderNodeTexGradient.html)

        Args:
            vector: Vector

        Returns:
            tuple ('color', 'fac')
        


### gradient_linear

```python
@staticmethod
def gradient_linear(vector=None)
```

         Node GradientTexture.

        Node reference [Gradient Texture](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/texture/gradient.html)
        Developer reference [ShaderNodeTexGradient](https://docs.blender.org/api/current/bpy.types.ShaderNodeTexGradient.html)

        Args:
            vector: Vector

        Returns:
            tuple ('color', 'fac')
        


### gradient_quadratic

```python
@staticmethod
def gradient_quadratic(vector=None)
```

         Node GradientTexture.

        Node reference [Gradient Texture](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/texture/gradient.html)
        Developer reference [ShaderNodeTexGradient](https://docs.blender.org/api/current/bpy.types.ShaderNodeTexGradient.html)

        Args:
            vector: Vector

        Returns:
            tuple ('color', 'fac')
        


### gradient_quadratic_sphere

```python
@staticmethod
def gradient_quadratic_sphere(vector=None)
```

         Node GradientTexture.

        Node reference [Gradient Texture](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/texture/gradient.html)
        Developer reference [ShaderNodeTexGradient](https://docs.blender.org/api/current/bpy.types.ShaderNodeTexGradient.html)

        Args:
            vector: Vector

        Returns:
            tuple ('color', 'fac')
        


### gradient_radial

```python
@staticmethod
def gradient_radial(vector=None)
```

         Node GradientTexture.

        Node reference [Gradient Texture](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/texture/gradient.html)
        Developer reference [ShaderNodeTexGradient](https://docs.blender.org/api/current/bpy.types.ShaderNodeTexGradient.html)

        Args:
            vector: Vector

        Returns:
            tuple ('color', 'fac')
        


### gradient_spherical

```python
@staticmethod
def gradient_spherical(vector=None)
```

         Node GradientTexture.

        Node reference [Gradient Texture](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/texture/gradient.html)
        Developer reference [ShaderNodeTexGradient](https://docs.blender.org/api/current/bpy.types.ShaderNodeTexGradient.html)

        Args:
            vector: Vector

        Returns:
            tuple ('color', 'fac')
        


### image

```python
@staticmethod
def image(image=None, vector=None, frame=None, extension='REPEAT', interpolation='Linear')
```

         Node ImageTexture.

        Node reference [Image Texture](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/texture/image.html)
        Developer reference [GeometryNodeImageTexture](https://docs.blender.org/api/current/bpy.types.GeometryNodeImageTexture.html)

        Args:
            image: Image
            vector: Vector
            frame: Integer
            extension (str): 'REPEAT' in [REPEAT, EXTEND, CLIP]
            interpolation (str): 'Linear' in [Linear, Closest, Cubic]

        Returns:
            tuple ('color', 'alpha')
        


### is_socket

```python
@staticmethod
def is_socket(value)
```

         An alternative to isinstance(value, Socket)

        :param value: The value to test
        :type value: any
        :return: True if *value* is an instance of Socket
        :rtype: bool
        


### is_vector

```python
@staticmethod
def is_vector(value)
```

         Determine is the parameter is a vector.

        :param value: The value to test
        :type value: any
        :return: True if *value* is an instance of Socket
        :rtype: bool
        



### magic

```python
@staticmethod
def magic(vector=None, scale=None, distortion=None, turbulence_depth=2)
```

         Node MagicTexture.

        Node reference [Magic Texture](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/texture/magic.html)
        Developer reference [ShaderNodeTexMagic](https://docs.blender.org/api/current/bpy.types.ShaderNodeTexMagic.html)

        Args:
            vector: Vector
            scale: Float
            distortion: Float
            turbulence_depth (int): 2

        Returns:
            tuple ('color', 'fac')
        


### musgrave

```python
@staticmethod
def musgrave(vector=None, w=None, scale=None, detail=None, dimension=None, lacunarity=None, offset=None, gain=None, musgrave_dimensions='3D', musgrave_type='FBM')
```

         Node MusgraveTexture.

        Node reference [Musgrave Texture](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/texture/musgrave.html)
        Developer reference [ShaderNodeTexMusgrave](https://docs.blender.org/api/current/bpy.types.ShaderNodeTexMusgrave.html)

        Args:
            vector: Vector
            w: Float
            scale: Float
            detail: Float
            dimension: Float
            lacunarity: Float
            offset: Float
            gain: Float
            musgrave_dimensions (str): '3D' in [1D, 2D, 3D, 4D]
            musgrave_type (str): 'FBM' in [MULTIFRACTAL, RIDGED_MULTIFRACTAL, HYBRID_MULTIFRACTAL, FBM, HETERO_TERRAIN]

        Returns:
            socket `fac`
        


### noise

```python
@staticmethod
def noise(vector=None, w=None, scale=None, detail=None, roughness=None, distortion=None, noise_dimensions='3D')
```

         Node NoiseTexture.

        Node reference [Noise Texture](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/texture/noise.html)
        Developer reference [ShaderNodeTexNoise](https://docs.blender.org/api/current/bpy.types.ShaderNodeTexNoise.html)

        Args:
            vector: Vector
            w: Float
            scale: Float
            detail: Float
            roughness: Float
            distortion: Float
            noise_dimensions (str): '3D' in [1D, 2D, 3D, 4D]

        Returns:
            tuple ('color', 'fac')
        


### noise_1D

```python
@staticmethod
def noise_1D(w=None, scale=None, detail=None, roughness=None, distortion=None)
```

         Node NoiseTexture.

        Node reference [Noise Texture](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/texture/noise.html)
        Developer reference [ShaderNodeTexNoise](https://docs.blender.org/api/current/bpy.types.ShaderNodeTexNoise.html)

        Args:
            w: Float
            scale: Float
            detail: Float
            roughness: Float
            distortion: Float

        Returns:
            tuple ('color', 'fac')
        


### noise_2D

```python
@staticmethod
def noise_2D(vector=None, scale=None, detail=None, roughness=None, distortion=None)
```

         Node NoiseTexture.

        Node reference [Noise Texture](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/texture/noise.html)
        Developer reference [ShaderNodeTexNoise](https://docs.blender.org/api/current/bpy.types.ShaderNodeTexNoise.html)

        Args:
            vector: Vector
            scale: Float
            detail: Float
            roughness: Float
            distortion: Float

        Returns:
            tuple ('color', 'fac')
        


### noise_3D

```python
@staticmethod
def noise_3D(vector=None, scale=None, detail=None, roughness=None, distortion=None)
```

         Node NoiseTexture.

        Node reference [Noise Texture](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/texture/noise.html)
        Developer reference [ShaderNodeTexNoise](https://docs.blender.org/api/current/bpy.types.ShaderNodeTexNoise.html)

        Args:
            vector: Vector
            scale: Float
            detail: Float
            roughness: Float
            distortion: Float

        Returns:
            tuple ('color', 'fac')
        


### noise_4D

```python
@staticmethod
def noise_4D(vector=None, w=None, scale=None, detail=None, roughness=None, distortion=None)
```

         Node NoiseTexture.

        Node reference [Noise Texture](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/texture/noise.html)
        Developer reference [ShaderNodeTexNoise](https://docs.blender.org/api/current/bpy.types.ShaderNodeTexNoise.html)

        Args:
            vector: Vector
            w: Float
            scale: Float
            detail: Float
            roughness: Float
            distortion: Float

        Returns:
            tuple ('color', 'fac')
        


### value_data_type

```python
@staticmethod
def value_data_type(value, default='FLOAT', color_domain='FLOAT_COLOR')
```

         Returns the domain to which the socket belongs
        
        :param value: The socket
        :type value: any
        :return: data type in ['BOOLEAN', 'INT', 'FLOAT', 'FLOAT_VECTOR', 'FLOAT_COLOR']
        :rtype: str
        
        .. list-table:: Correspondance table
           :widths: 30 20
           :header-rows: 1
        
           * - Socket bl_idname
             - Domain code
           * - NodeSocketBool
             - 'BOOLEAN'
           * - NodeSocketInt               
             - 'INT'
           * - NodeSocketIntUnsigned       
             - 'INT'
           * - NodeSocketFloat            
             - 'FLOAT'
           * - NodeSocketFloatFactor       
             - 'FLOAT'
           * - NodeSocketFloatAngle        
             - 'FLOAT'
           * - NodeSocketFloatDistance     
             - 'FLOAT'         
           * - NodeSocketVector            
             - 'FLOAT_VECTOR'
           * - NodeSocketVectorEuler       
             - 'FLOAT_VECTOR'
           * - NodeSocketVectorXYZ         
             - 'FLOAT_VECTOR'
           * - NodeSocketVectorTranslation
             - 'FLOAT_VECTOR'
           * - NodeSocketColor      
             - 'FLOAT_COLOR'
           * - NodeSocketString           
             - 'FLOAT_COLOR'
        
        



### voronoi

```python
@staticmethod
def voronoi(vector=None, w=None, scale=None, smoothness=None, exponent=None, randomness=None, distance='EUCLIDEAN', feature='F1', voronoi_dimensions='3D')
```

         Node VoronoiTexture.

        Node reference [Voronoi Texture](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/texture/voronoi.html)
        Developer reference [ShaderNodeTexVoronoi](https://docs.blender.org/api/current/bpy.types.ShaderNodeTexVoronoi.html)

        Args:
            vector: Vector
            w: Float
            scale: Float
            smoothness: Float
            exponent: Float
            randomness: Float
            distance (str): 'EUCLIDEAN' in [EUCLIDEAN, MANHATTAN, CHEBYCHEV, MINKOWSKI]
            feature (str): 'F1' in [F1, F2, SMOOTH_F1, DISTANCE_TO_EDGE, N_SPHERE_RADIUS]
            voronoi_dimensions (str): '3D' in [1D, 2D, 3D, 4D]

        Returns:
            tuple ('distance', 'color', 'position', 'w')
        


### voronoi_1D

```python
@staticmethod
def voronoi_1D(w=None, scale=None, smoothness=None, exponent=None, randomness=None, distance='EUCLIDEAN', feature='F1', voronoi_dimensions='3D')
```

         Node VoronoiTexture.

        Node reference [Voronoi Texture](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/texture/voronoi.html)
        Developer reference [ShaderNodeTexVoronoi](https://docs.blender.org/api/current/bpy.types.ShaderNodeTexVoronoi.html)

        Args:
            w: Float
            scale: Float
            smoothness: Float
            exponent: Float
            randomness: Float
            distance (str): 'EUCLIDEAN' in [EUCLIDEAN, MANHATTAN, CHEBYCHEV, MINKOWSKI]
            feature (str): 'F1' in [F1, F2, SMOOTH_F1, DISTANCE_TO_EDGE, N_SPHERE_RADIUS]
            voronoi_dimensions (str): '3D' in [1D, 2D, 3D, 4D]

        Returns:
            tuple ('distance', 'color', 'w')
        


### voronoi_2D

```python
@staticmethod
def voronoi_2D(vector=None, scale=None, smoothness=None, exponent=None, randomness=None, distance='EUCLIDEAN', feature='F1', voronoi_dimensions='3D')
```

         Node VoronoiTexture.

        Node reference [Voronoi Texture](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/texture/voronoi.html)
        Developer reference [ShaderNodeTexVoronoi](https://docs.blender.org/api/current/bpy.types.ShaderNodeTexVoronoi.html)

        Args:
            vector: Vector
            scale: Float
            smoothness: Float
            exponent: Float
            randomness: Float
            distance (str): 'EUCLIDEAN' in [EUCLIDEAN, MANHATTAN, CHEBYCHEV, MINKOWSKI]
            feature (str): 'F1' in [F1, F2, SMOOTH_F1, DISTANCE_TO_EDGE, N_SPHERE_RADIUS]
            voronoi_dimensions (str): '3D' in [1D, 2D, 3D, 4D]

        Returns:
            tuple ('distance', 'color', 'position')
        


### voronoi_3D

```python
@staticmethod
def voronoi_3D(vector=None, scale=None, smoothness=None, exponent=None, randomness=None, distance='EUCLIDEAN', feature='F1', voronoi_dimensions='3D')
```

         Node VoronoiTexture.

        Node reference [Voronoi Texture](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/texture/voronoi.html)
        Developer reference [ShaderNodeTexVoronoi](https://docs.blender.org/api/current/bpy.types.ShaderNodeTexVoronoi.html)

        Args:
            vector: Vector
            scale: Float
            smoothness: Float
            exponent: Float
            randomness: Float
            distance (str): 'EUCLIDEAN' in [EUCLIDEAN, MANHATTAN, CHEBYCHEV, MINKOWSKI]
            feature (str): 'F1' in [F1, F2, SMOOTH_F1, DISTANCE_TO_EDGE, N_SPHERE_RADIUS]
            voronoi_dimensions (str): '3D' in [1D, 2D, 3D, 4D]

        Returns:
            tuple ('distance', 'color', 'position')
        


### voronoi_4D

```python
@staticmethod
def voronoi_4D(vector=None, w=None, scale=None, smoothness=None, exponent=None, randomness=None, distance='EUCLIDEAN', feature='F1', voronoi_dimensions='3D')
```

         Node VoronoiTexture.

        Node reference [Voronoi Texture](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/texture/voronoi.html)
        Developer reference [ShaderNodeTexVoronoi](https://docs.blender.org/api/current/bpy.types.ShaderNodeTexVoronoi.html)

        Args:
            vector: Vector
            w: Float
            scale: Float
            smoothness: Float
            exponent: Float
            randomness: Float
            distance (str): 'EUCLIDEAN' in [EUCLIDEAN, MANHATTAN, CHEBYCHEV, MINKOWSKI]
            feature (str): 'F1' in [F1, F2, SMOOTH_F1, DISTANCE_TO_EDGE, N_SPHERE_RADIUS]
            voronoi_dimensions (str): '3D' in [1D, 2D, 3D, 4D]

        Returns:
            tuple ('distance', 'color', 'position', 'w')
        


### wave

```python
@staticmethod
def wave(vector=None, scale=None, distortion=None, detail=None, detail_scale=None, detail_roughness=None, phase_offset=None, bands_direction='X', rings_direction='X', wave_profile='SIN', wave_type='BANDS')
```

         Node WaveTexture.

        Node reference [Wave Texture](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/texture/wave.html)
        Developer reference [ShaderNodeTexWave](https://docs.blender.org/api/current/bpy.types.ShaderNodeTexWave.html)

        Args:
            vector: Vector
            scale: Float
            distortion: Float
            detail: Float
            detail_scale: Float
            detail_roughness: Float
            phase_offset: Float
            bands_direction (str): 'X' in [X, Y, Z, DIAGONAL]
            rings_direction (str): 'X' in [X, Y, Z, SPHERICAL]
            wave_profile (str): 'SIN' in [SIN, SAW, TRI]
            wave_type (str): 'BANDS' in [BANDS, RINGS]

        Returns:
            tuple ('color', 'fac')
        


### wave_bands

```python
@staticmethod
def wave_bands(vector=None, scale=None, distortion=None, detail=None, detail_scale=None, detail_roughness=None, phase_offset=None, direction='X', wave_profile='SIN')
```

         Node WaveTexture.

        Node reference [Wave Texture](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/texture/wave.html)
        Developer reference [ShaderNodeTexWave](https://docs.blender.org/api/current/bpy.types.ShaderNodeTexWave.html)

        Args:
            vector: Vector
            scale: Float
            distortion: Float
            detail: Float
            detail_scale: Float
            detail_roughness: Float
            phase_offset: Float
            direction (str): 'X' in [X, Y, Z, DIAGONAL]
            wave_profile (str): 'SIN' in [SIN, SAW, TRI]

        Returns:
            tuple ('color', 'fac')
        


### wave_bands_saw

```python
@staticmethod
def wave_bands_saw(vector=None, scale=None, distortion=None, detail=None, detail_scale=None, detail_roughness=None, phase_offset=None, direction='X')
```

         Node WaveTexture.

        Node reference [Wave Texture](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/texture/wave.html)
        Developer reference [ShaderNodeTexWave](https://docs.blender.org/api/current/bpy.types.ShaderNodeTexWave.html)

        Args:
            vector: Vector
            scale: Float
            distortion: Float
            detail: Float
            detail_scale: Float
            detail_roughness: Float
            phase_offset: Float
            direction (str): 'X' in [X, Y, Z, DIAGONAL]

        Returns:
            tuple ('color', 'fac')
        


### wave_bands_sine

```python
@staticmethod
def wave_bands_sine(vector=None, scale=None, distortion=None, detail=None, detail_scale=None, detail_roughness=None, phase_offset=None, direction='X')
```

         Node WaveTexture.

        Node reference [Wave Texture](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/texture/wave.html)
        Developer reference [ShaderNodeTexWave](https://docs.blender.org/api/current/bpy.types.ShaderNodeTexWave.html)

        Args:
            vector: Vector
            scale: Float
            distortion: Float
            detail: Float
            detail_scale: Float
            detail_roughness: Float
            phase_offset: Float
            direction (str): 'X' in [X, Y, Z, DIAGONAL]

        Returns:
            tuple ('color', 'fac')
        


### wave_bands_triangle

```python
@staticmethod
def wave_bands_triangle(vector=None, scale=None, distortion=None, detail=None, detail_scale=None, detail_roughness=None, phase_offset=None, direction='X')
```

         Node WaveTexture.

        Node reference [Wave Texture](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/texture/wave.html)
        Developer reference [ShaderNodeTexWave](https://docs.blender.org/api/current/bpy.types.ShaderNodeTexWave.html)

        Args:
            vector: Vector
            scale: Float
            distortion: Float
            detail: Float
            detail_scale: Float
            detail_roughness: Float
            phase_offset: Float
            direction (str): 'X' in [X, Y, Z, DIAGONAL]

        Returns:
            tuple ('color', 'fac')
        


### wave_rings

```python
@staticmethod
def wave_rings(vector=None, scale=None, distortion=None, detail=None, detail_scale=None, detail_roughness=None, phase_offset=None, direction='X', wave_profile='SIN')
```

         Node WaveTexture.

        Node reference [Wave Texture](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/texture/wave.html)
        Developer reference [ShaderNodeTexWave](https://docs.blender.org/api/current/bpy.types.ShaderNodeTexWave.html)

        Args:
            vector: Vector
            scale: Float
            distortion: Float
            detail: Float
            detail_scale: Float
            detail_roughness: Float
            phase_offset: Float
            direction (str): 'X' in [X, Y, Z, SPHERICAL]
            wave_profile (str): 'SIN' in [SIN, SAW, TRI]

        Returns:
            tuple ('color', 'fac')
        


### wave_rings_saw

```python
@staticmethod
def wave_rings_saw(vector=None, scale=None, distortion=None, detail=None, detail_scale=None, detail_roughness=None, phase_offset=None, direction='X')
```

         Node WaveTexture.

        Node reference [Wave Texture](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/texture/wave.html)
        Developer reference [ShaderNodeTexWave](https://docs.blender.org/api/current/bpy.types.ShaderNodeTexWave.html)

        Args:
            vector: Vector
            scale: Float
            distortion: Float
            detail: Float
            detail_scale: Float
            detail_roughness: Float
            phase_offset: Float
            direction (str): 'X' in [X, Y, Z, SPHERICAL]

        Returns:
            tuple ('color', 'fac')
        


### wave_rings_sine

```python
@staticmethod
def wave_rings_sine(vector=None, scale=None, distortion=None, detail=None, detail_scale=None, detail_roughness=None, phase_offset=None, direction='X')
```

         Node WaveTexture.

        Node reference [Wave Texture](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/texture/wave.html)
        Developer reference [ShaderNodeTexWave](https://docs.blender.org/api/current/bpy.types.ShaderNodeTexWave.html)

        Args:
            vector: Vector
            scale: Float
            distortion: Float
            detail: Float
            detail_scale: Float
            detail_roughness: Float
            phase_offset: Float
            direction (str): 'X' in [X, Y, Z, SPHERICAL]

        Returns:
            tuple ('color', 'fac')
        


### wave_rings_triangle

```python
@staticmethod
def wave_rings_triangle(vector=None, scale=None, distortion=None, detail=None, detail_scale=None, detail_roughness=None, phase_offset=None, direction='X')
```

         Node WaveTexture.

        Node reference [Wave Texture](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/texture/wave.html)
        Developer reference [ShaderNodeTexWave](https://docs.blender.org/api/current/bpy.types.ShaderNodeTexWave.html)

        Args:
            vector: Vector
            scale: Float
            distortion: Float
            detail: Float
            detail_scale: Float
            detail_roughness: Float
            phase_offset: Float
            direction (str): 'X' in [X, Y, Z, SPHERICAL]

        Returns:
            tuple ('color', 'fac')
        


### white_noise

```python
@staticmethod
def white_noise(vector=None, w=None, noise_dimensions='3D')
```

         Node WhiteNoiseTexture.

        Node reference [White Noise Texture](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/texture/white_noise.html)
        Developer reference [ShaderNodeTexWhiteNoise](https://docs.blender.org/api/current/bpy.types.ShaderNodeTexWhiteNoise.html)

        Args:
            vector: Vector
            w: Float
            noise_dimensions (str): '3D' in [1D, 2D, 3D, 4D]

        Returns:
            tuple ('value', 'color')
        


### white_noise_1D

```python
@staticmethod
def white_noise_1D(w=None)
```

         Node WhiteNoiseTexture.

        Node reference [White Noise Texture](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/texture/white_noise.html)
        Developer reference [ShaderNodeTexWhiteNoise](https://docs.blender.org/api/current/bpy.types.ShaderNodeTexWhiteNoise.html)

        Args:
            w: Float

        Returns:
            tuple ('value', 'color')
        


### white_noise_2D

```python
@staticmethod
def white_noise_2D(vector=None)
```

         Node WhiteNoiseTexture.

        Node reference [White Noise Texture](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/texture/white_noise.html)
        Developer reference [ShaderNodeTexWhiteNoise](https://docs.blender.org/api/current/bpy.types.ShaderNodeTexWhiteNoise.html)

        Args:
            vector: Vector

        Returns:
            tuple ('value', 'color')
        


### white_noise_3D

```python
@staticmethod
def white_noise_3D(vector=None)
```

         Node WhiteNoiseTexture.

        Node reference [White Noise Texture](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/texture/white_noise.html)
        Developer reference [ShaderNodeTexWhiteNoise](https://docs.blender.org/api/current/bpy.types.ShaderNodeTexWhiteNoise.html)

        Args:
            vector: Vector

        Returns:
            tuple ('value', 'color')
        


### white_noise_4D

```python
@staticmethod
def white_noise_4D(vector=None, w=None)
```

         Node WhiteNoiseTexture.

        Node reference [White Noise Texture](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/texture/white_noise.html)
        Developer reference [ShaderNodeTexWhiteNoise](https://docs.blender.org/api/current/bpy.types.ShaderNodeTexWhiteNoise.html)

        Args:
            vector: Vector
            w: Float

        Returns:
            tuple ('value', 'color')
        


## Methods

### connected_sockets

```python
def connected_sockets(self)
```

         Returns the list of Socket instances linked to this socket.
        



### get_blender_socket

```python
def get_blender_socket(self)
```

         Returns the property bsocket.
        
        :return: self.bsocket
        :rtype: bpy.types.NodeSocket
        



### init_domains

```python
def init_domains(self)
```

         Initialize the geometry domains
        
        To be overloaded by sub classes.        
        


### init_socket

```python
def init_socket(self)
```

         Complementary init
        
        Called at the end of initialization for further operations.
        


### plug

```python
def plug(self, *values)
```

         Plug values in the socket (input sockets only)
        
        :param values: The output sockets. More than one values can be passed
            if the input socket is multi input.
        :type values: array of bpy.types.NodeSocket, Socket, values
        
        see :func:`plug_bsocket`
        


### reroute

```python
def reroute(self)
```

         Reroute all output links
        


### reset_properties

```python
def reset_properties(self)
```

         Reset the properties
        
        Properties such as components are cached.
        
        After a node is called, the wrapped socket changes and this makes the cache obsolete.
        After a change, the cache is erased.
        
        :example:
        
        .. code-block:: python
    
            class Vector(...):
                def __init__(self, ...):
                     ...
                     self.reset_properties()
                     ...
            
                 def reset_properties(self):
                     super().reset_properties()
                     self.separate_ = None      # Created by property self.seperate() with node SeparateXyz

        
        



### stack

```python
def stack(self, node, socket_name=None)
```

         Change the wrapped socket
        
        :param node: The new node owning the output socket to wrap
        :type node: Node
        :return: self
        
        Methods are implemented in two modes:
        
        - Creation
        - Transformation
        
        In **creation mode**, the node is considered as creating new data. The result is a new instance of DataSocket.
        
        In **transformation mode**, the node is considered as transforming data which is kept in the result of the method.
        After the method returns, the calling DataSocket instance refers to a new Blender output socket.
        The stack method changes the socket the instance refers to and reinitialize properties
        
        .. code-block:: python

            # 1. Creation mode
            # 
            # to_mesh method creates a new mesh from a curve.
            # The curve instance refers to the same output node socket
            # We need to get the result of the method in a new variable
            
            new_mesh = curve.to_mesh(profile_curve=circle)
            
            # 2. Transformation mode
            #
            # set_shade_smooth method transforms the mesh.
            # After the call, the mesh instance refers to the output socket of the
            # newly created node "Set Shade Smooth". There is no need to get the result
            # of the method.
            
            mesh.set_shade_smooth()
            
            # Note that a transformation method returns self and so, the following line
            # is equivallent:
            
            mesh = mesh.set_shade_smooth()
        
        



### switch

```python
def switch(self, switch=None, true=None)
```

         Node Switch.

        Node reference [Switch](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/switch.html)
        Developer reference [GeometryNodeSwitch](https://docs.blender.org/api/current/bpy.types.GeometryNodeSwitch.html)

        Args:
            switch: Boolean
            true: Texture

        Returns:
            socket `output`
        


### to_output

```python
def to_output(self, name=None)
```

         Plug the data socket to the group output
        
        :param name: The name to give to the modifier output
        :type name: str
        
        The socket is added to the outputs of the geometry nodes tree.
        
        .. Note:: To define a data socket as the result geometry of the tree, use ``tree.output_geometry = my_geometry``.
        
        


### view

```python
def view(self, domain='AUTO', label=None, node_color=None)
```

         Link the data socket to the viewer
        
        If the data socket is a geometry (Curve, Mesh...) it is linked to the geometry input of the viewer.
        
        If it ias a value (Integer, Float,...) it is linked to the value socket and the viewer is configured
        accordingly.
        


