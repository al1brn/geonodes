"""python -m geonodes.kaomojilang FILE [--python] [--list] [--svg DIR] [--cell N]

  --python   print the valid Python produced by stage 1
  --list     list drawings and kaomoji lines
  --svg DIR  render every drawing (grid defs, Shape variables, lists of Shapes) to DIR
"""

import argparse
import sys

from . import LangError, run_file, translate


def main(argv=None):
    ap = argparse.ArgumentParser(prog="kaomojilang", description=__doc__, formatter_class=argparse.RawTextHelpFormatter)
    ap.add_argument("file")
    ap.add_argument("--python", action="store_true")
    ap.add_argument("--list", action="store_true")
    ap.add_argument("--svg", metavar="DIR")
    ap.add_argument("--cell", type=float, default=10.0, help="pixels per grid column (default 10)")
    args = ap.parse_args(argv)
    try:
        if args.python:
            with open(args.file, encoding="utf-8") as f:
                print(translate(f.read(), args.file).source, end="")
            return 0
        prog = run_file(args.file)
        if args.list or not args.svg:
            print("drawings:", ", ".join(prog.shape_names) or "-")
            print(f"kaomoji: {len(prog.kaomoji)} lines")
            for k in prog.kaomoji[:10]:
                print(f"  {k.text}   {k.label}")
            if len(prog.kaomoji) > 10:
                print(f"  ... {len(prog.kaomoji) - 10} more")
        if args.svg:
            for path in prog.render_svgs(args.svg, cell=args.cell):
                print("wrote", path)
        return 0
    except LangError as e:
        print(e, file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main())
