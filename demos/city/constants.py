from geonodes import *

# Linteau = lintel
# jambage, piédroit, montant = jamb, pier
# meneau = mullion
# appui = sill, windowsill


__all__ = (
    'IS_GROUP',
    'MIN_SIZE', 'MIN_LOD', 'MIN_HEIGHT',
    'PROF_RECT', 'PROF_CUT_CORNERS', 'PROF_ROUNDED_CORNERS', 'PROF_CIRCLE', 'PROF_ELLIPSIS', 'PROF_CIRCLE_X', 'PROF_CIRCLE_Y',
    'render_input', 'cseed')

IS_GROUP = False

MIN_SIZE = 0.07
MIN_LOD  = 0.01
MIN_HEIGHT = 1.0


PROF_RECT               = 0
PROF_CUT_CORNERS        = 1
PROF_ROUNDED_CORNERS    = 2
PROF_CIRCLE             = 3
PROF_ELLIPSIS           = 4
PROF_CIRCLE_X           = 5
PROF_CIRCLE_Y           = 6

def render_input(with_seed=True):
    with Panel("Render"):
        preview = Boolean(False, "Preview")
        lod     = Float.Distance(MIN_LOD, "LOD", MIN_LOD)

    if with_seed:
        seed = Integer(0, "Seed")
        return preview, lod, seed
    
    else:
        return preview, lod

def cseed(seed):
    ref = seed
    seed += 1
    return ref



