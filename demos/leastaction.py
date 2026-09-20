print('-'*100)
print('-'*100)

from geonodes import *

def demo_maupertuis():

    WEIGHT_SIG = ({'Position': Vector}, {'Weight': Float})
    GEO_SIG = {'Weight Function': Closure, 'Action': Float}

    # ====================================================================================================
    # Actions
    # ====================================================================================================

    with GeoNodes("Action Select", is_group=True):
        
        idx = Integer.MenuSwitch({
                "Constant"    : 0,
                "Gradient X"  : 1,
                "Gradient Y"  : 2,
                "Fermat"      : 3,
                "Maupertuis"  : 4,
                }, menu=Input("Action"))
        a = Float(1.0, "A")
        b = Float(1.0, "B")
        h = Float(5.0, "H")
        speed = Float(1.0, "Speed")
                
        with Closure.IndexSwitch(index=idx) as weight_func:
            
            # Constant
            with Closure() as cl:
                _ = Vector(None, "Position")
                Float(1.0).out("Weight")
                
            cl.out()
            
            # Gradient X
            with Closure() as cl:
                pos = Vector(None, "Position")
                (pos.x.abs()*a + b).out("Weight")
                
            cl.out()
            
            # Gradient Y
            with Closure() as cl:
                pos = Vector(None, "Position")
                (pos.y.abs()*a + b).out("Weight")
                
            cl.out()

            # Fermat        
            with Closure() as cl:
                pos = Vector(None, "Position")
                pos.x.map_range(-a, a, b, 1/b, interpolation_type="Smooth Step").out("Weight")
                
            cl.out()
            
            # Maupertuis
            with Closure() as cl:
                pos = Vector(None, "Position")
                E = h*10 + speed**2/2
                gnmath.sqrt(2*(E - pos.y*10)).out("Weight")
                
            cl.out()
            
        weight_func.out("Weight")
        
    # ====================================================================================================
    # Store action
    # ====================================================================================================

    with GeoNodes("Store Action"):
        
        geo = Geometry()
        weight_func = G().action_select().link_inputs()
        geo.set_bundle(Bundle.Combine({"Weight Function": weight_func, "Action": 0.0}))
        geo.out()
        
    def get_weight_func(curve=None, object=None):
        if curve is not None:
            bundle = curve.get_bundle()
            return bundle.separate(signature=GEO_SIG).weight_function

        if object is None:
            object = Object(None, "Weight Object")
            
        bundle = object.info().geometry.get_bundle()
        return bundle.separate(signature=GEO_SIG).weight_function

    def get_weight(weight_func, position):
        return weight_func.evaluate(position=position, signature=WEIGHT_SIG).weight
        
    # ====================================================================================================
    # Prepare Curve
    # ====================================================================================================

    with GeoNodes("Curve Prepare"):
        
        curve = Curve()
        use_resample = Boolean(False, "Resample")
        count = Integer(10, "Count")
        weight_func = Closure(None, "Weight Function")
        
        with Layout("Prepare"):
            curve.switch(use_resample, Curve(curve).resample(count=count))
            count.switch_false(use_resample, curve.points.count)._lc("Count")
            last_index = (count - 1)._lc("Last Index")
            ext_sel = ((nd.index == 0) | (nd.index == last_index))._lc("Extremities")
            
        with Layout("Segments length"):        
            pos0 = curve.points.sample_index(nd.position, index=nd.index - 1)._lc("Before")
            pos1 = curve.points.sample_index(nd.position, index=nd.index + 1)._lc("After")
            
            segm = pos1 - nd.position
            length_attr = curve.points.get('Length', Float)
            length_attr.set(segm.length())
            curve.points[nd.index == last_index].set('Length', 0.0)
            
        with Layout("Weights"):
            pt_weight = get_weight(weight_func, nd.position)
            ptw_attr = curve.points.get('Point Weight', Float)
            ptw_attr.set(pt_weight)
            
            next_weight = curve.points.sample_index(ptw_attr.value, index=nd.index + 1)
            segw_attr = curve.points.get('Segment Weight', Float)
            segw_attr.set((ptw_attr.value + next_weight)/2)
            
        with Layout("Perp"):
            tg = pos1 - pos0
            x, y, _ = tg.xyz
            a = curve.points.set('Perp', (-y, x, 0))
            curve.points[ext_sel].set(a, (0.0, 0.0, 0.0))
            
        with Layout("Action"):
            action = curve.points.attribute_statistic(length_attr.value*segw_attr.value).sum
            curve.set_bundle(Bundle.Combine({'Weight Function': weight_func, 'Action': action}))
        
        curve.out()
        
    # ====================================================================================================
    # Compute displacements
    # ====================================================================================================

    with GeoNodes("Compute Displacements"):
        
        curve = Curve()
        delta = Float(0.1, "Delta")
        weight_func = get_weight_func(curve=curve)
        
        with Layout("Prepare"):
            count = curve.points.count._lc("Count")
            last_index = (count - 1)._lc("Last Index")
            
            disp = curve.points.get('Perp', Vector).value.scale(delta)._lc("Displacement")
            x, y, _ = disp.xyz
            disp = Vector((x, y, 0.0))
            
            idx  = nd.index
            idx0 = idx - 1
            idx1 = idx + 1
            
            pt_weight = curve.points.get('Point Weight', Float).value
            segm_length = curve.points.get('Length', Float).value
            
            pos0 = curve.points.sample_index(nd.position, index=idx0)
            pos1 = curve.points.sample_index(nd.position, index=idx1)
            
            pt_weight0 = curve.points.sample_index(pt_weight, index=idx0)
            pt_weight1 = curve.points.sample_index(pt_weight, index=idx1)

            segm_length0 = curve.points.sample_index(segm_length, index=idx0)
            
            old_action = segm_length0*(pt_weight0 + pt_weight)/2
            old_action += segm_length*(pt_weight + pt_weight1)/2
        
        for first in (True, False):
            with Layout("First Side" if first else "Second Side"):
                new_pos = (nd.position + disp) if first else (nd.position - disp)
                new_weight = get_weight(weight_func, new_pos)
                
                new_length0 = (new_pos - pos0).length() 
                new_length = (pos1 - new_pos).length()
                
                new_action = new_length0*(pt_weight0 + new_weight)/2
                new_action += new_length*(new_weight + pt_weight1)/2
                
                action_delta = new_action - old_action
                
                if first:
                    adelta0 = curve.points.set("Action Delta 0", action_delta)
                    curve.points.set("Pos 0", new_pos)
                else:
                    adelta1 = curve.points.set("Action Delta 1", action_delta)
                    curve.points.set("Pos 1", new_pos)
                
        with Layout("Finalize"):
            is_fix = (nd.index == 0) | (nd.index == last_index)
            curve.points[is_fix].set(adelta0, 0.0)
            curve.points[is_fix].set(adelta1, 0.0)
            
            move = (adelta0.value*adelta1.value) < 0.0
            
            a = curve.points.set('Move', move)
            curve.points[is_fix].set(a, False)
            
            pos0 = curve.points.get('Pos 0', Vector).value
            pos1 = curve.points.get('Pos 1', Vector).value
            
            move_to = pos0.switch(adelta0.value > 0.0, pos1)
            curve.points.set('Move To', move_to)
                
        curve.out()
        
    # ====================================================================================================
    # Algorithm
    # ====================================================================================================

    with GeoNodes("Least Action"):
        
        curve = Curve()
        weight_func = get_weight_func()
        count = Integer(30, "Count")
        delta = Float(1.0, "Delta")
        time_scale = Integer(1, "Time Scale", 1)
        delta_fac = Float.Factor(0.995, "Delta Factor", 0, 1)
        sub_steps = Integer(100, "Sub Steps", 1)
        
        curve = G().curve_prepare(curve, resample=True, count=count, weight_function=weight_func)
        
        for sim in simulation(curve=curve, delta=delta):
            
            for rep_time in repeat(time_scale, curve=sim.curve, delta=sim.delta):
            
                for rep in repeat(sub_steps, curve=rep_time.curve):
                
                    length = rep.curve.length()
                    d = length/count*sim.delta
                    
                    cur_curve = G().curve_prepare(rep.curve, resample=False, weight_function=weight_func)
                    
                    for peer in (True, False):
                        cur_curve = G().compute_displacements(cur_curve, delta=d)
                        ok = cur_curve.points.get('Move', Boolean).value
                        if peer:
                            ok &= nd.index % 2 == 0
                        else:
                            ok &= nd.index % 2 == 1
                            
                        move_to = cur_curve.points.get('Move To', Vector).value
                        cur_curve.points[ok].position = move_to
                        
                    rep.curve = cur_curve
                    
                with Layout("Decrease Delta if no point to move"):
                    cur_curve = rep.curve

                    ok_move = Attribute('Move', Boolean).value
                    n_move = cur_curve.points.attribute_statistic(Float(ok_move)).sum
                    new_delta = rep_time.delta
                    new_delta.switch(n_move == 0, new_delta * delta_fac)

                    rep_time.delta = new_delta
                    
                with Layout("Resample Curve"):            
                    rep_time.curve = rep.curve.resample(count=count)
                    
            sim.curve = rep_time.curve
            sim.delta = rep_time.delta
            
            
        Boolean(True).info("Delta: " + sim.delta.to_string(decimals=3))
            
        curve = G().curve_prepare(sim.curve, resample=False, weight_function=weight_func)
            
        curve.out()
            
    # ====================================================================================================
    # Show stress
    # ====================================================================================================
        
    with GeoNodes("Show Stress"):
        
        NX = 10
        
        curve = Curve()
        show = Boolean(True, "Show")
        delta = Float(0.1, "Delta", 0.0, 1.0)
        scale = Vector((1.0, 1.0, 1.0), "Scale", dimensions=2)
        
        ny = curve.points.count
        
        with Layout("Base grid"):
            nx = 2*NX + 1
            grid = Mesh.Grid(vertices_x = nx, vertices_y = ny)
            
            grid_j = nd.index % ny 
            grid_i = nd.index // ny
            
            
        grid.points.position = curve.points.sample_index(nd.position, index=grid_j)
            
        scale_hrz, scale_vrt, _ = scale.xyz
            
        # Loop on parallels
        for rep in repeat(NX, grid=grid):
            
            idx = rep.iteration + 1
            
            d = idx*delta/NX
            
            c = G().compute_displacements(curve, delta=d)
            pos = c.points.sample_index(nd.position, index=grid_j)
            pos0 = c.points.sample_index(c.points.get('Pos 0', Vector).value, index=grid_j)
            pos1 = c.points.sample_index(c.points.get('Pos 1', Vector).value, index=grid_j)
            tr0 = (pos0 - pos).scale(scale_hrz)
            tr1 = (pos1 - pos).scale(scale_hrz)
            
            ad0 = c.points.sample_index(c.points.get('Action Delta 0', Float).value, index=grid_j)
            ad1 = c.points.sample_index(c.points.get('Action Delta 1', Float).value, index=grid_j)
            ok = c.points.sample_index(c.points.get('Move', Boolean).value, index=grid_j)
            
            sel0 = grid_i == NX + idx 
            sel1 = grid_i == NX - idx 

            rep.grid.points[sel0].offset = tr0 + (0, 0, ad0*scale_vrt)
            rep.grid.points[sel1].offset = tr1 + (0, 0, ad1*scale_vrt)
            
            rep.grid.points[sel0].set('Color', Color.Switch(ok & (ad0 < 0.0), "White", "Red"))
            rep.grid.points[sel1].set('Color', Color.Switch(ok & (ad1 < 0.0), "White", "Red"))
            
            
        grid = Mesh(rep.grid)
        grid.faces.shade_smooth = True
        grid.faces.material = "Gradient"
        
        with Layout("Curve"):
            mesh_curve = curve.to_mesh(profile_curve=Curve.Circle(radius=delta*scale_hrz/100, resolution=12))
            mesh_curve.faces.shade_smooth = True
            mesh_curve.faces.material = "Gradient"
            mesh_curve.faces.set('Color', Color("Black"))
            
            #grid += mesh_curve
            
        Geometry.Switch(show, curve, grid).out()
        
    # ====================================================================================================
    # Parabole
    # ====================================================================================================

    with GeoNodes("Parabole"):
        
        speed = Float(1.0, "Speed", 0.0)
        ag = Float.Angle(pi/4, "Direction")
        h = Float(1.0, "H")
        duration = Float(10, "Duration", 0)
        count = Integer(30, "Count", 10)
        
        
        vx = speed*ag.cos()
        vy = speed*ag.sin()
        
        t = duration*nd.index/(count-1)
        
        curve = Curve.Line().resample(count=count)
        curve.position = vx*t, h + vy*t - 5*t**2, 0
        
        curve.out()

def demo_lagrange():

    LAGRANGIAN_SIG = ({'Start': Vector, 'End': Vector}, {'Lagrangian': Float})
    GEO_SIG = {'Lagrangian Function': Closure, 'Duration': Float, 'Action': Float}

    # ====================================================================================================
    # Actions
    # ====================================================================================================

    with GeoNodes("Lagrangian Function", is_group=True):
        
        idx = Integer.MenuSwitch({
                "Null"     : 0,
                "Gravity"  : 1,
                }, menu=Input("Potential"))
                
                
        def get_T():
            P0 = Vector(None, "Start")
            P1 = Vector(None, "End")
            
            dx, dy, dt = (P1 - P0).xyz
            l2 = dx**2 + dy**2
            
            T = l2/(2*(dt**2))
            
            #length = gnmath.sqrt(l2)
            return P0, P1, T, dt
                
        with Closure.IndexSwitch(index=idx) as lagrangien_func:
            
            # null
            with Closure() as cl:
                _, _, T, dt = get_T()
                (T*dt).out("Lagrangian")
                
            cl.out()
            
            # Gravity
            with Closure() as cl:
                P0, P1, T, dt = get_T()
                V = (P0.y + P1.y)*(9.81/2)
                ((T - V)*dt).out("Lagrangian")
                
            cl.out()
            
        lagrangien_func.out("Lagrangian")
        
    # ====================================================================================================
    # Store action
    # ====================================================================================================

    with GeoNodes("Lagrangian Store"):
        
        geo = Geometry()
        lagrangian_func = G().lagrangian_function().link_inputs()
        duration = Float(1.0, "Duration", 0.01)
        geo.set_bundle(Bundle.Combine({
            "Lagrangian Function": lagrangian_func,
            "Duration": duration,
            "Action": 0.0}))
        geo.out()
        
    def get_lagrangian_func(curve=None, object=None):
        
        with Layout("Get Lagrangian and duration"):
            if curve is not None:
                bundle = curve.get_bundle().separate(signature=GEO_SIG)
                return bundle.lagrangian_function, bundle.duration

            if object is None:
                object = Object(None, "Lagrangian Object")
                
            bundle = object.info().geometry.get_bundle().separate(signature=GEO_SIG)
            return bundle.lagrangian_function, bundle.duration

    def get_lagrangian(lagrangian_func, start, end):
        return lagrangian_func.evaluate(start=start, end=end, signature=LAGRANGIAN_SIG).lagrangian
        
    # ====================================================================================================
    # Prepare Curve
    # ====================================================================================================

    with GeoNodes("Lagrangian Prepare"):
        
        curve = Curve()
        use_resample = Boolean(False, "Resample")
        count = Integer(10, "Count")
        lagrangian_func = Closure(None, "Lagrangian Function")
        duration = Float(1.0, "Duration", 0.1)
        
        with Layout("Prepare"):
            timed = Curve(curve).resample(count=count)
            x, y, _ = nd.position.xyz
            timed.position = x, y, (nd.index*duration)/(count - 1)
            curve.switch(use_resample, timed)
            
            count.switch_false(use_resample, curve.points.count)._lc("Count")
            last_index = (count - 1)._lc("Last Index")
            ext_sel = ((nd.index == 0) | (nd.index == last_index))._lc("Extremities")
            
        with Layout("Segment Weights"):
            end = curve.points.sample_index(nd.position, index=nd.index + 1)._lc("After")
            w = get_lagrangian(lagrangian_func, nd.position, end)
            weight_attr = curve.points.set('Weight', w)
            curve.points[nd.index == last_index].set(weight_attr, 0.0)
            
        with Layout("Perp"):
            P0 = curve.points.sample_index(nd.position, index=nd.index - 1)
            P1 = curve.points.sample_index(nd.position, index=nd.index + 1)
            tg = P1 - P0
            x, y, _ = tg.xyz
            a = curve.points.set('Perp', (-y, x, 0))
            curve.points[ext_sel].set(a, (0.0, 0.0, 0.0))
            
        with Layout("Action"):
            action = curve.points.attribute_statistic(weight_attr.value).sum
            curve.set_bundle(Bundle.Combine({
                "Lagrangian Function": lagrangian_func,
                "Duration": duration,
                "Action": action}))
        
        curve.out()
        
    # ====================================================================================================
    # Compute displacements
    # ====================================================================================================

    with GeoNodes("Lagrangian Displacements"):
        
        curve = Curve()
        delta = Float(0.1, "Delta")
        direction = Vector((0.0, 1.0, 0.0), "Direction")
        lagrangian_func, _ = get_lagrangian_func(curve=curve)
        
        with Layout("Prepare"):
            count = curve.points.count._lc("Count")
            last_index = (count - 1)._lc("Last Index")
            
            # Unlike the Maupertuis action, the Lagrangian action is not invariant
            # under a spatial reparametrization at fixed time. Explore independent
            # spatial degrees of freedom rather than only the curve normal.
            disp = direction.scale(delta)._lc("Displacement")
            x, y, _ = disp.xyz
            disp = Vector((x, y, 0.0))

            idx  = nd.index
            idx0 = idx - 1
            idx1 = idx + 1
            
            weight = Attribute('Weight', Float).value
            weight0 = curve.points.sample_index(weight, index=idx0)
            old_weight = weight0 + weight
            
            P0 = curve.points.sample_index(nd.position, index=idx0)._lc("P0")
            P1 = curve.points.sample_index(nd.position, index=idx1)._lc("P1")
            
        
        for first in (True, False):
            with Layout("First Side" if first else "Second Side"):
                new_pos = (nd.position + disp) if first else (nd.position - disp)
                
                weight0 = get_lagrangian(lagrangian_func, P0, new_pos)
                weight1 = get_lagrangian(lagrangian_func, new_pos, P1)
                action_delta = weight0 + weight1 - old_weight
                
                if first:
                    adelta0 = curve.points.set("Action Delta 0", action_delta)
                    curve.points.set("Pos 0", new_pos)
                else:
                    adelta1 = curve.points.set("Action Delta 1", action_delta)
                    curve.points.set("Pos 1", new_pos)
                
        with Layout("Finalize"):
            is_fix = (nd.index == 0) | (nd.index == last_index)
            curve.points[is_fix].set(adelta0, 0.0)
            curve.points[is_fix].set(adelta1, 0.0)

            MIN_ALGO = True
            if MIN_ALGO:
                move = gnmath.min(adelta0.value, adelta1.value) < 0.0
            else:
                move = (adelta0.value*adelta1.value) < 0.0
            
            a = curve.points.set('Move', move)
            curve.points[is_fix].set(a, False)
            
            pos0 = curve.points.get('Pos 0', Vector).value
            pos1 = curve.points.get('Pos 1', Vector).value

            if MIN_ALGO:
                move_to = pos0.switch(adelta0.value > adelta1.value, pos1)
            else:
                move_to = pos0.switch(adelta0.value > 0.0, pos1)
                
            curve.points.set('Move To', move_to)
                
        curve.out()
        
    # ====================================================================================================
    # Algorithm
    # ====================================================================================================

    with GeoNodes("Lagrangian Least Action"):
        
        curve = Curve()
        lagrangian_func, duration = get_lagrangian_func()
        count = Integer(30, "Count")
        delta = Float(1.0, "Delta")/1000
        time_scale = Integer(1, "Time Scale", 1)
        delta_fac = Float.Factor(0.995, "Delta Factor", 0, 1)
        sub_steps = Integer(100, "Sub Steps", 1)
        
        curve = G().lagrangian_prepare(curve, resample=True, count=count, lagrangian_function=lagrangian_func, duration=duration)
        
        for sim in simulation(curve=curve, delta=delta):
            
            for rep_time in repeat(time_scale, curve=sim.curve, delta=sim.delta):
            
                for rep in repeat(sub_steps, curve=rep_time.curve):
                
                    length = rep.curve.length()
                    d = length/count*rep_time.delta
                    
                    cur_curve = rep.curve

                    # At fixed time, x and y are two independent degrees of
                    # freedom. Recompute the action after every checkerboard pass
                    # so the following pass sees the geometry just produced.
                    for direction in ((1.0, 0.0, 0.0), (0.0, 1.0, 0.0)):
                        for peer in (True, False):
                            cur_curve = G().lagrangian_prepare(
                                cur_curve,
                                resample=False,
                                lagrangian_function=lagrangian_func,
                                duration=duration,
                            )
                            cur_curve = G().lagrangian_displacements(
                                cur_curve,
                                delta=d,
                                direction=direction,
                            )
                            ok = cur_curve.points.get('Move', Boolean).value
                            if peer:
                                ok &= nd.index % 2 == 0
                            else:
                                ok &= nd.index % 2 == 1
                                
                            move_to = cur_curve.points.get('Move To', Vector).value
                            cur_curve.points[ok].position = move_to
                        
                    rep.curve = cur_curve
                    
                with Layout("Decrease Delta if no point to move"):
                    cur_curve = rep.curve

                    ok_move = Attribute('Move', Boolean).value
                    n_move = cur_curve.points.attribute_statistic(Float(ok_move)).sum
                    new_delta = rep_time.delta
                    new_delta.switch(n_move == 0, new_delta * delta_fac)

                    rep_time.delta = new_delta
                    
                with Layout("Resample Curve"):  
                    rep_time.curve = rep.curve #.resample(count=count)
                    
            sim.curve = rep_time.curve
            sim.delta = rep_time.delta
            
        curve = G().lagrangian_prepare(
            sim.curve,
            resample=False,
            lagrangian_function=lagrangian_func,
            duration=duration,
        )
            
            
        Boolean(True).info("Delta: " + sim.delta.to_string(decimals=3))
            
        curve.out()
            
    # ====================================================================================================
    # Show stress
    # ====================================================================================================
        
    with GeoNodes("Lagrangian Show Stress"):
        
        NX = 10
        
        curve = Curve()
        show = Boolean(True, "Show")
        delta = Float(0.1, "Delta", 0.0, 1.0)
        scale = Vector((1.0, 1.0, 1.0), "Scale", dimensions=2)
        
        ny = curve.points.count
        
        with Layout("Base grid"):
            nx = 2*NX + 1
            grid = Mesh.Grid(vertices_x = nx, vertices_y = ny)
            
            grid_j = nd.index % ny 
            grid_i = nd.index // ny
            
            
        grid.points.position = curve.points.sample_index(nd.position, index=grid_j)
            
        scale_hrz, scale_vrt, _ = scale.xyz
            
        # Loop on parallels
        for rep in repeat(NX, grid=grid):
            
            idx = rep.iteration + 1
            
            d = idx*delta/NX
            
            c = G().lagrangian_displacements(curve, delta=d, direction=(0.0, 1.0, 0.0))
            pos = c.points.sample_index(nd.position, index=grid_j)
            pos0 = c.points.sample_index(c.points.get('Pos 0', Vector).value, index=grid_j)
            pos1 = c.points.sample_index(c.points.get('Pos 1', Vector).value, index=grid_j)
            tr0 = (pos0 - pos).scale(scale_hrz)
            tr1 = (pos1 - pos).scale(scale_hrz)
            
            ad0 = c.points.sample_index(c.points.get('Action Delta 0', Float).value, index=grid_j)
            ad1 = c.points.sample_index(c.points.get('Action Delta 1', Float).value, index=grid_j)
            ok = c.points.sample_index(c.points.get('Move', Boolean).value, index=grid_j)
            
            sel0 = grid_i == NX + idx 
            sel1 = grid_i == NX - idx 

            rep.grid.points[sel0].offset = tr0 + (0, 0, ad0*scale_vrt)
            rep.grid.points[sel1].offset = tr1 + (0, 0, ad1*scale_vrt)
            
            rep.grid.points[sel0].set('Color', Color.Switch(ok & (ad0 < 0.0), "White", "Red"))
            rep.grid.points[sel1].set('Color', Color.Switch(ok & (ad1 < 0.0), "White", "Red"))
            
            
        grid = Mesh(rep.grid)
        grid.faces.shade_smooth = True
        grid.faces.material = "Gradient"
        
        with Layout("Curve"):
            mesh_curve = curve.to_mesh(profile_curve=Curve.Circle(radius=delta*scale_hrz/100, resolution=12))
            mesh_curve.faces.shade_smooth = True
            mesh_curve.faces.material = "Gradient"
            mesh_curve.faces.set('Color', Color("Black"))
            
            #grid += mesh_curve
            
        Geometry.Switch(show, curve, grid).out()
        


            
