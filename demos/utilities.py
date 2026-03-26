from geonodes import Closure, Float, Integer, Boolean, GeoNodes, Group, repeat

# ====================================================================================================
# Dichotomy
# ====================================================================================================

def dichotomy(f: Closure=None, t0: Float=None, t1: Float=None, count: Integer=None):
    """ Solve a closure function

    Solve f(t) = 0. by dichotomy

    Arguments
    ---------
    - f (Closure) : function to solve, signature is (t: Float -> Value : Float)
    - t0 (Float) : min t value
    - t1 (Float) : max t value
    - Count (Integer) : number of loops
    
    Returns
    -------
    - Float t sich as f(t) = 0
    """

    # Store arguments which are used by Group creation
    f_ = f
    t0_ = t0
    t1_ = t1
    count_= count

    with GeoNodes("Dichotomy", is_group=True) as g:

        f  = Closure(None, "f")
        t0 = Float(0., "t0")
        t1 = Float(1., "t1")
        count = Integer(10, "Count", 1, 100)
        
        signature = ({"t":0.0}, {"Value": 0.0})

        v0 = f.evaluate(signature=signature, t=t0).value
        v1 = f.evaluate(signature=signature, t=t1).value
        
        growing = v1.greater_than(v0)
        
        for rep in repeat(count, t0=t0, t1=t1):
            
            t = (rep.t0 + rep.t1)/2
            v = f.evaluate(signature=signature, t=t).value
            
            plus = v.greater_than(0)
            minus = Boolean(plus).bnot()
            
            t0_a = Float(rep.t0).switch(minus, t)
            t1_a = Float(rep.t1).switch(plus, t)
            
            t0_b = rep.t0.switch(plus, t)
            t1_b = rep.t1.switch(minus, t)
            
            rep.t0 = t0_b.switch(growing, t0_a)
            rep.t1 = t1_b.switch(growing, t1_a)
            
        t = (rep.t0
              + rep.t1)/2
        t.out("Value")

    return Group("Dichotomy", f=f_, t0=t0_, t1=t1_, count=count_).value