"""
This file is part of the geonodes distribution (https://github.com/al1brn/geonodes).
Copyright (c) 2025 Alain Bernard.

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, version 3.

This program is distributed in the hope that it will be useful, but
WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program. If not, see <http://www.gnu.org/licenses/>.

-----------------------------------------------------
Scripting Geometry Nodes
-----------------------------------------------------

module : demo facvalue
----------------------


updates
-------
- creation :   2026/07/11


Convert a Curve as a XY function.
The input curve is interpretated as a XY function.
It is converted into a Curve where factor is the abscissa with three
named attributes:
- Value
- Integral
- Derivative

It is used in Trajectory where the Input XY curve defines the speed norm
when moving on the curve
"""

# ====================================================================================================
# Function to Curve
# ====================================================================================================

with GeoNodes("FacValue From Curve"):
    
    curve = Curve()
    count = Integer(100, "Resolution", 2,10000)
    x_as_factor = Boolean(True, "X as Factor")
    normalize_integral = Boolean(True, "Normalize Integral")
    
    curve = curve.resample(mode='Count', count=count)
    
    node = curve.points.attribute_statistic(nd.position).node
    x0, y0, _ = node.min.xyz
    x1 = node.max.x

    #dt = 1.0/(count - 1)
    
    for rep in repeat(count, curve=curve, y_integ=0.0):
        
        sel = rep.iteration == nd.index
        rep.curve.points[sel].Integral = rep.y_integ
        
        pos = curve.points.sample_index(nd.position, index=rep.iteration)
        x, y, _ = pos.xyz
        
        x.switch(x_as_factor, x.map_range(x0, x1))
        
        rep.curve[sel].position = (x, 0.0, 0.0)
        rep.curve.points[sel].Value = y

        rep.y_integ += y
        
    fcurve = rep.curve
    
    with Layout("Normalize Integral"):
        integ = Float("Integral")
        max_integ = fcurve.points.sample_index(integ, index=count-1)
        normalized = Curve(fcurve)
        normalized.points.Integral = integ/max_integ
        fcurve.switch(normalize_integral, normalized)
        
    
    px = nd.position.x
    value = Float("Value")
    
    with Layout("Derivative"):
        i0 = nd.index - 1
        i1 = nd.index + 1
        v0 = fcurve.points.sample_index(value, i0)
        v1 = fcurve.points.sample_index(value, i1)
        
        x0 = fcurve.points.sample_index(px, i0)
        x1 = fcurve.points.sample_index(px, i1)
        
        fcurve.points.Derivative = (v1 - v0)/(x1 - x0)
        
    with Layout("First Derivative"):
        
        i0 = 0
        i1 = 1
        v0 = fcurve.points.sample_index(value, i0)
        v1 = fcurve.points.sample_index(value, i1)
        
        x0 = fcurve.points.sample_index(px, i0)
        x1 = fcurve.points.sample_index(px, i1)
        
        fcurve.points[nd.index == 0].Derivative = (v1 - v0)/(x1 - x0)
        
    with Layout("Last Derivative"):
        
        i0 = count - 2
        i1 = count - 1
        v0 = fcurve.points.sample_index(value, i0)
        v1 = fcurve.points.sample_index(value, i1)
        
        x0 = fcurve.points.sample_index(px, i0)
        x1 = fcurve.points.sample_index(px, i1)
        
        fcurve.points[nd.index == i1].Derivative = (v1 - v0)/(x1 - x0)
        
    fcurve.out()
    
# ====================================================================================================
# Function curve to curve
# ====================================================================================================

with GeoNodes("FacValue to Curves"):
    
    curve = Curve()
    count = Integer(100, "Count", 2, 10000)
    x_max = Float(1.0, "X Max")
    y_scale = Float(1.0, "Y Scale")
    use_der = Boolean(True, "Derivative")
    use_func = Boolean(True, "Function")
    use_integ = Boolean(True, "Integral")
    

    with Layout("Function"):
        func = Curve.Line().resample(mode="Count", count=count)
        t = nd.index/(count-1)
        func.position = x_max*t, curve.sample_factor(Float("Value"), factor=t), 0.0
        
        geo = func.switch_false(use_func)
    
    with Layout("Integral"):
        integ = Curve.Line().resample(mode="Count", count=count)
        t = nd.index/(count-1)
        integ.position = x_max*t, curve.sample_factor(Float("Integral")*y_scale, factor=t), 0.0
        
        geo += integ.switch_false(use_integ)
        
    with Layout("Derivative"):
        der = Curve.Line().resample(mode="Count", count=count)
        t = nd.index/(count-1)
        der.position = x_max*t, curve.sample_factor(Float("Derivative")*y_scale, factor=t), 0.0
        
        geo += der.switch_false(use_der)
        
    geo.out("Curve")
    
# ====================================================================================================
# A curve as a trajectory
# ====================================================================================================

with GeoNodes("Trajectory"):
    
    curve = Curve()
    t = Float.Factor(0.0, "Factor", 0, 1, shape="Single")
    speed_obj = Object(None, "Speed Curve")
    count = Integer(100, "Resolution", 2, 10_000)
    
    
    with Layout("Radial Acceleration"):
        s_curve = curve.resample(mode='Count', count=count)
        dt = 1.0/(count - 1)
        
        tg0 = s_curve.points.sample_index(nd.curve_tangent, nd.index-1)
        tg1 = s_curve.points.sample_index(nd.curve_tangent, nd.index+1)

        s_curve.points.Radial = (tg1 - tg0)/(2*dt) 
        radial_acc = Vector("Radial")
        s_curve.points[0].Radial = s_curve.points.sample_index(radial_acc, index=1)
        s_curve.points[count-1].Radial = s_curve.points.sample_index(radial_acc, index=count-2)
        
    with Layout("Speed Curve"):
        speed_curve = Curve(speed_obj.info().geometry)
        speed_func = G().facvalue_from_curve(speed_curve)
        
        
        speed_length = speed_func.sample_factor(Float("Value"), factor=t)
        factor = speed_func.sample_factor(Float("Integral"), factor=t)
        acc_length = speed_func.sample_factor(Float("Derivative"), factor=t)
        
        
    with Layout("Get the values"):
        radial = s_curve.sample_factor(Vector("Radial"), factor=factor)

        node = radial.node
        pos = node.position
        tangent = node.tangent
        
        speed = tangent.scale(speed_length**2)
        
        rad_acc = radial.scale(speed_length)
        tg_acc = tangent.scale(acc_length)
        
        acc = rad_acc + tg_acc
        
    
    curve = curve.trim(end=factor)
    curve.out()
    pos.out("Position")
    speed.out("Speed")
    acc.out("Acceleration")
    factor.out("Factor")
    tg_acc.out("Tangent Acceleration")
    rad_acc.out("Radial Acceleration")
    

    