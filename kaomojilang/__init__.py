"""kaomojilang: draw SVG / Grease Pencil shapes with numbers and symbols.

    from geonodes.kaomojilang import run

    prog = run(open("face.kmj", encoding="utf-8").read())
    face = prog.call("smooth_face_example")       # a Shape
    face.save_svg("face.svg")
    face.to_grease_pencil(gp, frame=1)

Two stages: `stage1` translates the text line by line into valid Python,
`stage2` parses it with `ast`, validates it and runs it. See SPEC.md.
"""

from .errors import LangError, RunError, Stage1Error, Stage2Error
from .runtime import Shape, frames_to_grease_pencil
from .stage1 import demangle, translate
from .stage2 import Program, run, run_file

__all__ = ["run", "run_file", "translate", "demangle", "Program", "Shape", "frames_to_grease_pencil",
           "LangError", "Stage1Error", "Stage2Error", "RunError"]
