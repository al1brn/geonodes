# kaomojilang (prototype)

Draw SVG / Grease Pencil shapes by *placing numbers and symbols* in text.

```
colors = {0:yellow, 10:white, 20:white, 30:black, 40:black}
sizes  = {30:large, 40:large}
def smooth_face_example(fill=colors, sizes=sizes):
         0
                   1
  7                  2
      10  11  20  21
         30      40
  ...
```

## Pipeline

```
source text ──stage 1──▶ valid Python ──ast.parse──▶ validated tree ──exec──▶ Shapes ──▶ SVG / Grease Pencil
            (line by line)     (stage 2)              (stage 2)
```

* **Stage 1** (`stage1.py`) is a line translator. It never evaluates anything. It keeps a line map, so every
  error points at the *original* line.
* **Stage 2** (`stage2.py`) parses stage 1's output with Python's `ast`, rejects everything outside a small
  safe subset (no imports, attributes, classes, lambdas, `while`, dunder names), and executes it with a
  fixed namespace (colors, sizes, `random()`, `sin`, `cos`, `pi`, `sqrt`, `range` capped at 100 000).
* **Runtime** (`runtime.py`) turns grids into `Shape`s and renders them with the `drawing` package
  (drawsvg), so the same shape gives an SVG file or Grease Pencil strokes.

`python -m geonodes.kaomojilang FILE --python` prints what stage 1 produced.

## Stage 1 rules

| Input | Becomes |
|---|---|
| a non-ASCII character Python cannot use in a name (`▢`, `‿`, fullwidth parens) in code | `_uXXXX_`, so `def ▢(...)` and `▢(smooth=1)` are valid Python. Strings and comments are left alone |
| the body of a `def` made only of integers | a function returning `__shape__([(number, x, row), ...], name, params, defaults)` |
| a column-0 line that is not Python (not def, assignment, comment, `import`, `for`, ...) | `__kaomoji__(text, label)`; the label is the comment on the next line |
| anything else | Python, passed through (after symbol mangling) |

Triple-quoted strings and bracketed continuations are tracked, so kaomoji inside docstrings are ignored and an
unclosed `(` is reported on the line where it was opened.

### Grid geometry

* `x` = column of the *center* of the number (`10` spans two columns), `y` = row, both relative to the block.
* Rows are multiplied by `ASPECT = 2` (a text row is about twice as tall as a column is wide), so
  four columns by two rows is a square.
* A number used twice in a drawing is an error.

## Shape rules

Numbers form **runs of consecutive values** (`0 1 2 3`, then `10 11`, ...). The first number of a run is
the **id** of the part.

| Run | Part |
|---|---|
| 1 number | dot, or a stamped glyph (below) |
| 2 numbers | line |
| 3+ numbers, odd id | closed polygon (can be filled) |
| 3+ numbers, even id | smooth closed curve (can be filled) |

`smooth` (0..1, default 0.5): every corner is replaced by a cubic going from a point `smooth/2` of the way toward the
previous corner to a point `smooth/2` toward the next one, the corner being the control polygon.
`smooth=1` on a square is a circle, `smooth=0` is the polygon.

### Parameters

`fill`, `stroke` (default black), `width` (default 0.15 columns), `sizes` (dot size, default 1.5 columns),
`smooth`. Each is either a value or a dict `{part id: value, '*': default}`.

* Predefined names: CSS color names (`red`, `yellow`, `none`, ...) and sizes `tiny 0.7`, `small 1`,
  `medium 1.5`, `large 2.5`, `huge 4`.
* A dict passed to a parameter whose *default* is a dict is **overlaid** on it, so
  `face({30: ▢(smooth=random())})` changes the pupils and keeps the other colors.
  A scalar replaces the default.
* A drawing used as a `fill` value of a **single point** is stamped there, stretched to a `size x size`
  box. `▢(...)` is therefore a unit square whose `smooth` goes from square to circle.
* Calling a drawing returns a `Shape`. `shape.to_svg()`, `shape.save_svg(path)`,
  `shape.to_grease_pencil(gp, frame=n)`, and `frames_to_grease_pencil(list_of_shapes, gp)`
  (one keyframe per shape, same framing for all).

### Grease Pencil layers

One layer per part, named `p<id>` (`p0`, `p10`, ...). Smooth shapes become Bezier strokes (4+ anchors, handles),
polygons and lines stay polylines.

## Decisions taken where the example was open

1. Run detection by consecutive numbers (`7` then `10` starts a new part).
2. Dot fill defaults to the stroke color. A dot with a `fill` that is a color is a circle.
3. Overlay semantics for dict arguments (so the pupil animation keeps the face colors).
4. Glyph stamping stretches to a square box (so `▢` is square regardless of its grid aspect).
5. Any column-0 non-Python line is a kaomoji line; bare call statements at top level are therefore not valid
   (use assignments).
6. Line 39 of the original example had an unclosed `(` (`▢(smooth=random(),`); `examples/example.kmj` is the
   corrected version. The unclosed bracket is reported as an error on line 39.

## Not done yet (proposals)

* **Kaomoji to shapes.** The 105 kaomoji lines are parsed (`prog.kaomoji`, text + label) but not drawn. A natural
  next step is the same idea as `▢`: a table of eye / mouth / cheek glyphs, each a small numbered drawing, composed
  left to right (`ʘ‿ʘ` = eye `ʘ` + mouth `‿` + eye `ʘ`).
* **Open smooth lines** with 3+ points (today only 2-point lines are open). Proposal: a trailing symbol on the last
  number, e.g. `5~`, or an id range reserved for open shapes.
* Per-point attributes (width taper), animation keyframes in the language (`anim_frames` is plain Python today).
* Nested defs and drawing composition (`place(shape, at=12, size=large)`).

## Additions (face / bear experiments)

- **Parameters** `shift`, `rotate`, `scale` join `fill stroke width sizes smooth`. Each is a value or a dict
  `{id: value, '*': default}`. `shift=(cols, rows)`; `rotate` is clockwise degrees about the part centroid
  (for a stamped point: the glyph's rotation); `scale` is a number or `(sx, sy)`, and `0` hides the part.
- All standard parameters are implicit: a grid shape accepts them even when its `def` doesn't declare them.
- **Sizes** accept a number or `(w, h)`; a one-point part with `(w, h)` is an ellipse.
- **Stamping**: a Shape used as the `fill` of a single point is drawn at its natural size (or `sizes`), with
  stroke width compensated. Hidden parts leave empty keyframes in Grease Pencil so layers don't hold stale drawings.
- **Open runs**: a `~` right after the last number of a run (`2~`) leaves 3+ points open. Odd id: open polyline;
  even id: open smooth curve whose ends are not rounded (smile / frown). `~` anywhere else is an error.
  Ids in a run must be consecutive, so two separate parts need non-consecutive ids (e.g. 11 and 15, not 11 and 12).
- A `def` header must be on one line.
- More CSS colors: tan, wheat, beige, coral, salmon, tomato, crimson, hotpink, violet, indigo, skyblue, ...
- Examples: `face_anim.kmj` (talk, blink, look, mood, emotes), `bear.kmj`.
