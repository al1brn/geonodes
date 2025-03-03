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

module : demo formula_latex
---------------------------

Simple LaTeX interpretor

IN PROGRESS

updates
-------
- creation :   2025/02/22

$ DOC START

[Source Code](../demos/forest.py)

Animated formula

IN PROGRESS

``` python
from geonodes.demos import formula

formula.demo()
```
"""

from .formula_data import SYMBOLS

from geonodes import *

# =============================================================================================================================
# LaTeX simple interpreter

SUB0 = "{{"
SUB1 = "}}"

class Tex:

    alpha    = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
    blocks   = {'(': ')', '[': ']', '{': '}', SUB0: SUB1}
    commands = ['int', 'sqrt', 'frac', 'vec', 'overrightarrow']

    def __init__(self, s):
        self.s = s
        self.index = 0

    @property
    def eof(self):
        return self.index >= len(self.s)

    # -----------------------------------------------------------------------------------------------------------------------------
    # Next Char
    #
    # Translate symbols into unicode: \alpha -> α

    @property
    def next(self):
        """ Get the next char

        > [!CAUTION]
        > Single symbols '{' and '}' are returned as '{{' and '}}' when '\{' and '\}'
        > are returned as '{' and '}'
        """
        if self.index >= len(self.s):
            return None

        c = self.s[self.index]
        self.index += 1

        ret = None

        if c == '{':
            ret = SUB0

        elif c == '}':
            ret = SUB1

        elif c == "\\":

            # Next char can be { or | for instance
            word = self.s[self.index]
            self.index += 1

            # Complete with alpha if is alpha
            if word in Tex.alpha:
                for i in range(self.index, len(self.s)):
                    if self.s[i] in Tex.alpha:
                        word += self.s[i]
                    else:
                        break

            self.index += len(word)

            ret = SYMBOLS.get(word, "\\" + word)

        else:
            ret = c

        print("NEXT", ret)
        return ret

    @property
    def get_next(self):
        index = self.index
        next = self.next
        self.index = index
        return next

    @property
    def next_is_word(self):
        n = self.get_next
        if n is None:
            return False
        else:
            return (len(n) == 1) and (n not in ['_', '^', '\\', '{', '(', '[', ' '])

    # ----------------------------------------------------------------------------------------------------
    # Token:
    # - block : {s}, (s), [s]
    # - \command
    # - word

    @property
    def token(self):

        c = self.next

        # ----- End of string

        if c is None:
            return None

        # ----- Token separator

        if c == ' ':
            return self.token

        # ----- Block { ( [

        elif c in Tex.blocks:
            index = self.index

            target = Tex.blocks[c]

            depth = 1
            while depth != 0:
                if self.eof:
                    raise Exception(f"Unbalanced '{c}' @ {index-1}: {self.s[index-1:]}")

                nc = self.next

                if nc == target:
                    depth -= 1
                elif nc == c:
                    depth += 1

            return c + self.s[index:self.index-1] + target

        # ----- End of block: syntax error

        elif c == Tex.blocks.values():
            raise Exception(f"Unbalanced '{c}' @ {self.index-1}: {self.s[self.index-1:]}")

        # ----- A Command

        elif c.startswith("\\"):
            return c

        # ----- A control char

        elif c in ['^', '_']:
            return c

        # ----- Series of chars

        else:
            word = c
            while self.next_is_word:
                word += self.next

            return word

    # ----------------------------------------------------------------------------------------------------
    # Formula from next token

    def token_formula(self):
        tex = Tex(self.token)
        return tex.parse(None)

    @property
    def token_formula_OLD(self):
        tex = Tex(self.token)
        return tex.parse()

    # ----------------------------------------------------------------------------------------------------
    # Parser

    def parse(self, formula):

        token = self.token

        # ----------------------------------------------------------------------------------------------------
        # Done

        if token is None:
            return None

        # ----------------------------------------------------------------------------------------------------
        # Block

        elif token[0] in Tex.blocks:
            n = len(SUB0) if token.startswith(SUB0) else 1
            sub_tex = Tex(token[n:-n])

            codes = {'(': 'Parenthesis',
                     '[': 'Brackets',
                     '|': 'Absolute',
                     '{': 'Braces',
                     '‖': 'Norm'}
            code = codes.get(token[0], "Parenthesis")

            with Layout("Brackets"):
                cur_id = G().node_get_id(formula)
                new_id = cur_id + 1

                formula = sub_tex.parse(formula)
                formula = Mesh(formula)
                formula.faces[Integer("Item ID") > cur_id]._Item_ID = new_id

                return G().brackets(formula, id=new_id, brackets=code)

        # ----------------------------------------------------------------------------------------------------
        # Subscript or exponent

        elif token in ['_', '^']:

            item = self.token_formula()

            if token == '_':
                return G().node_add(formula, item, link_id=0, location='Indice')

            elif token == '^':
                return G().node_add(formula, item, link_id=0, location='Exponent')

            else:
                assert(False)

        # ----------------------------------------------------------------------------------------------------
        # Special

        elif token[0] == "\\":
            kw = token[1:]

            if kw == "frac":
                top = self.token_formula
                bot = self.token_formula
                frm = FractionFormula(top, bot)
                formula.append(frm)

            elif kw == "sum":
                formula.append(SumFormula())

            elif kw in ['vec', 'overrightarrow']:
                frm = self.token_formula
                frm.set_vector(kw)
                formula.append(frm)

            elif kw == 'sqrt':
                frm = self.token_formula
                frm.set_sqrt(2)
                formula.append(frm)

            else:
                raise Exception(f"Sorry: keyword '{token}' not yet supported")

        # ----------------------------------------------------------------------------------------------------
        # Series of chars

        else:
            return G().characters(formula, chars=token)

    # ----------------------------------------------------------------------------------------------------
    # Parser

    def parse_OLD(self):

        formula = Formula()

        while True:

            token = self.token

            # ----------------------------------------------------------------------------------------------------
            # Done

            if token is None:
                break

            # ----------------------------------------------------------------------------------------------------
            # Block

            elif token[0] in tex.blocks:
                n = len(SUB0) if token.startswith(SUB0) else 1
                sub_tex = Tex(token[n:-n])
                frm = sub_tex.parse()
                frm.block = token[0]
                formula.append(frm)

            # ----------------------------------------------------------------------------------------------------
            # Subscript or exponent

            elif token in ['_', '^']:

                frm = self.token_formula

                print("IND EXP", frm)

                if token == '_':
                    formula[-1].indice = frm

                elif token == '^':
                    formula[-1].exponent = frm

                else:
                    assert(False)

            # ----------------------------------------------------------------------------------------------------
            # Special

            elif token[0] == "\\":
                kw = token[1:]

                if kw == "frac":
                    top = self.token_formula
                    bot = self.token_formula
                    frm = FractionFormula(top, bot)
                    formula.append(frm)

                elif kw == "sum":
                    formula.append(SumFormula())

                elif kw in ['vec', 'overrightarrow']:
                    frm = self.token_formula
                    frm.set_vector(kw)
                    formula.append(frm)

                elif kw == 'sqrt':
                    frm = self.token_formula
                    frm.set_sqrt(2)
                    formula.append(frm)

                else:
                    raise Exception(f"Sorry: keyword '{token}' not yet supported")

            # ----------------------------------------------------------------------------------------------------
            # Series of chars

            else:
                formula.append(Formula.Word(token))

        if len(formula) == 1:
            return formula[0]
        else:
            return formula


def build_from_latex(latex_string, group_name):

    tex = Tex(latex_string)

    with GeoNodes(group_name):

        formula = None
        while True:
            new_formula = tex.parse(formula)
            if new_formula is None:
                break

            formula = new_formula

        formula.out()



"""
    # =============================================================================================================================
    # A base formula item

    class FormItem(list):
        def __init__(self, *content):
            super().__init__()
            self.extend(content)

            # ----- decorators

            self.word     = None # Body
            self.italic   = None
            self.bold     = None

            self.block    = None # ( [ { or function name or sqrt
            self.indice   = None # Formula at indice position
            self.exponent = None # Formula at exponent position

            self.top      = None # Something above, arrow for instance
            self.bot      = None # Something below, dot for instance

        @classmethod
        def Word(cls, word):
            frm = cls()
            frm.word = word
            return frm


        def str_body(self):
            s = "" if self.word is None else self.word
            for item in self:
                s += str(item)
            return s

        def str_decos(self):
            s = ""
            if self.indice is not None:
                s += "_" + str(self.indice)
            if self.exponent is not None:
                s += "^" + str(self.exponent)

            if self.top is not None:
                s += "TOP(" + str(self.top) + ')'
            if self.bot is not None:
                s += "BOT(" + str(self.bot) + ')'

            return s

        def __str__(self):

            s = self.str_body()

            if self.block is None:
                pass

            elif self.block == '{':
                s = '{' + s + '}'

            elif self.block == '(':
                s = '(' + s + ')'

            elif self.block == '{':
                s = '[' + s + ']'

            elif self.block == 'sqrt':
                s = f"\\sqrt({s})"

            else:
                s = f"{self.block}({s})"

            s += self.str_decos()
            return s

        def __repr__(self):

            s = f"<{type(self).__name__} [{len(self)}]: '{self}' :"

            for i, frm in enumerate(self):
                sub = repr(frm)
                lines = sub.split("\n")
                s += f"\n {i:3d}: " + "\n      ".join(lines)

            if self.indice is not None:
                sub = repr(self.indice)
                lines = sub.split("\n")
                s += f"\n ind: " + "\n      ".join(lines)

            if self.exponent is not None:
                sub = repr(self.exponent)
                lines = sub.split("\n")
                s += f"\n exp: " + "\n      ".join(lines)

            return s + ">"

        # =============================================================================================================================
        # Add things around the formula

        def set_block(self, symbol="{"):
            self.block = symbol

        def set_vector(self, kw = 'vec'):
            self.top = 'kw'

        def set_sqrt(self, n=2):
            self.block = SQRT
            self.sqrt_n = n

        def set_function(self, name="sin"):
            self.block = name


        # =============================================================================================================================
        # To Geometry nodes

        def body_curves(self):

            with Layout(f"Body of {self}"):

                curves = None
                width = 0.

                if self.word is not None:
                    s = self.str_body()
                    curves = G().formula_string(s)
                    width = curves.width_

                for frm in self:
                    cs, w = frm.curves()
                    if curves is None:
                        curves = cs
                        width = w
                    else:
                        curves += cs.transform((w + X_SPACE, 0, 0))
                        width += X_SPACE + w

            return curves, width

        def curves(self):
            with Layout(f"Curves of {self}"):

                curves, width = self.body_curves()

                # ----------------------------------------------------------------------------------------------------
                # Block

                if self.block in ['(', '[']:
                    open = self.block
                    close = ')' if open == '(' else ']'

                    curves = G().formula_block(curves, open=open, close=close)
                    width = curves.width_

                elif self.block == SQRT:
                    curves = G().formula_sqrt(curves, n=self.sqrt_n)
                    width = curves.width_

                # ----------------------------------------------------------------------------------------------------
                # Indice and exponent

                ie_width = 0.
                ie_scale = .4
                for i, (frm, dy) in enumerate([(self.indice, -Y_IND), (self.exponent, Y_EXP)]):

                    if frm is None:
                        continue

                    with Layout("{['Indice', 'Exponent'][i]} {str(frm)}"):
                        sub_curves, w = frm.curves()
                        sub_curves.transform(scale=ie_scale, translation=(width + X_IND, dy, 0))
                        if curves is None:
                            curves = sub_curves
                        else:
                            curves += sub_curves

                        ie_width = gnmath.max(ie_width, (X_IND + w)*ie_scale)

            return curves, width + ie_width

    class FractionFormula(Formula):
        def __init__(self, num=None, den=None):
            super().__init__(num, den)

        def str_body(self):
            s = "\\frac"
            if len(self) >= 1:
                s += str(self[0])
            if len(self) >= 2:
                s += str(self[1])

            return s

    class SumFormula(Formula):
        def str_body(self):
            return "\\sum"



    s = r"\sum_{n=1}^{+\infty} \frac{1}{n^2} = \frac{\pi^2}{6}"
    #s = "(∂^2 (B^' ) ⃗)/(∂〖t^'〗^2 )=γ^2 β^2 c^2  (∂B ⃗)/(∂x^2 )"

    s = r"A\sqrt{sin(a)^2} .\partial_{k,l,m}\alpha\varphi\pi"

    tex = Tex(s)

    print("STRING", s)

    frm = tex.parse()
    print(repr(frm))

    with GeoNodes("Test"):

        curves = None
        x = 0.

        for i, f in enumerate(frm):
            cs, w = f.curves()
            if curves is None:
                curves = cs
                x = w
            else:
                curves += cs.transform(translation=(x + .1, 0, 0))
                x += .1 + w

            #if i == 1:
            #    break

        curves = Curve(curves)

        mesh = curves.fill()

        mesh.out()

    class FormulaItem:
        ID = 0

        def __init__(self, name):
            self.name = name
            FormulaItem.ID += 1
            self.id = FormulaItem.ID

            self.node = None

        @property
        def group_name(self):
            return f"{self.name} {self.id}"

"""





# =============================================================================================================================
# =============================================================================================================================
# Animation
# =============================================================================================================================
# =============================================================================================================================

# =============================================================================================================================
# Animation curves

class Key:
    def __init__(self, time: float, value: float, interpolation='SMOOTH'):
        self.time          = time
        self.value         = value
        self.interpolation = interpolation

# -----------------------------------------------------------------------------------------------------------------------------
# Animation curve builder

class AnimationCurve(list):

    def __init__(self, name: str, value: float):
        super().__init__()
        self.name = name
        self.append(Key(0., value))

    def build_curve(self):

        with Layout(f"Curve - {self.name}"):

            line = Curve.Line().resample(len(self))
            line.splines.type = 'BEZIER'

            for i, kf in enumerate(self):
                line.points[i].position=(kf.time, kf.value, 0)

            return line

            #line.out(self.name)

    @property
    def time(self):
        return self[-1].time

    @property
    def value(self):
        return self[-1].value

    def add(self, time, value, interpolation='SMOOTH'):
        self[-1].interpolation = interpolation
        self.append(Key(time, value))

    def mark(self, time: float):
        self.add(time, self.value)

    def change(self, time: float, duration: float, value: float, interpolation='SMOOTH'):
        self.mark(time)
        self.add(time + duration, value, interpolation)

    def pingpong(self, time: float, duration: float, value: float, interpolation='SMOOTH'):
        old = self.value
        self.mark(time)
        self.add(time + duration/2, value, interpolation)
        self.add(time + duration, old, interpolation)

# -----------------------------------------------------------------------------------------------------------------------------
# Animation group builder

class AnimationCurves(list):

    def new(self, name: str, value: float):
        ac = AnimationCurve(name, value)
        self.append(ac)
        return ac

    def build_node(self, name, to_node):

        with GeoNodes(name, is_group=True):

            for ac in self:
                line = ac.build_curve()
                value = G().time_line_curve(line)
                value.out(ac.name)

        anim_node = Group(name)
        for ac in self:
            setattr(to_node, ac.name.lower(), getattr(anim_node, ac.name.lower()))

# -----------------------------------------------------------------------------------------------------------------------------
# Build a block animator

def build_item_animator(name):

    with GeoNodes(f"{name} Animator"):

        with Panel(name):

            x            = Float(0, "X")
            y            = Float(0, "Y")
            scale        = Float(1, "Scale")
            width_offset = Float(0, "Width Offset")

        node = Group(name, sockets=parameters, link_from='TREE')

        geo = node._out
        geo = geo.transform(translation=(x + width_offset/2, y, 0), scale=scale)

        geo.out()

# =============================================================================================================================
# groups

def build_anim():

    with GeoNodes("Time Line Curve", is_group=True):
        curve = Curve()
        t = nd.scene_time().seconds

        x_max = curve.points.attribute_statistic(nd.position.x).max
        x = gnmath.max(0, gnmath.min(t, x_max))

        factor = x/x_max

        v = curve.sample_factor(nd.position.y, factor=factor)
        v.out("Value")

    with GeoNodes("Write"):

        content = Mesh(Geometry())
        factor  = Float.Factor(1, "Factor", 0, 1)

        cur_fade = content.faces.sample_index(Float("Fade"), index=0)

        dims = G().dimensions(content).node
        x = factor.map_range_linear(to_min=dims.left, to_max=dims.right)
        content.faces._Fade = nd.position.x.map_range_linear(x-.2, x, 0, cur_fade)

        content.out()

    with GeoNodes("Animator"):

        content = Geometry()

        # Location
        x            = Float(0, "X")
        y            = Float(0, "Y")
        scale        = Float(1, "Scale")
        width_offset = Float(0, "Width Offset")

        # Aspect
        color        = Color('black', "Color")
        fade         = Float.Factor(0, "Fade", 0, 1)

        # Sign
        plus         = Float.Factor(0, "Sign Plus")
        sign_fade    = Float.Factor(1, "Sign Fade")

        # Write
        write        = Float.Factor(1, "Write", 0, 1)

        # Show
        show         = Boolean(True, "Show")

        geo = G().sign(content, plus=plus, fade=sign_fade, color=color)
        geo = G().set_aspect(G().sign(geo, plus=plus, fade=sign_fade), fade=fade, color=color)
        geo = geo.transform(translation=(x + width_offset/2, y, 0), scale=scale)

        geo = G().write(geo, factor=write)

        geo.switch_false(show).out()
