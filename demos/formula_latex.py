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
from . import formula as FORM
from geonodes import *

GBuild = G("Build")
GChars = G("Char")
GTerm  = G("Term")
GComp  = G("Compile")

SLASH_AS_FRAC = False


ALPHA_CHARS    = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
BLOCK_CHARS    = {'{': '}', '(': ')', '[': ']', '\\{': '\\}', '⟨': '⟩', '‖': '‖'}
NOT_WORD_CHARS = [' ', '_', '^'] + list(BLOCK_CHARS.keys()) + list(BLOCK_CHARS.values())

if SLASH_AS_FRAC:
    NOT_WORD_CHARS += ['/']

BLOCK_CODES    = {'{'  : FORM.DECO_NOTHING,
                    '('  : FORM.DECO_PARENTHESIS,
                    '['  : FORM.DECO_BRACKETS,
                    '\\{': FORM.DECO_BRACES,
                    '⟨'  : FORM.DECO_ANGLE,
                    '‖'  : FORM.DECO_NORM,}

COMMANDS = ['int', 'sqrt', 'frac', 'vec', 'overrightarrow']

FUNCTIONS = [
    'sin', 'asin', 'arcsin', 'cos', 'acos', 'arscos', 'tan', 'atan', 'arctan', 'cotan', 'acotan', 'arccotan',
    'sinh', 'asinh', 'arcsinh', 'cosh', 'acosh', 'arscosh',  'tanh', 'atanh', 'arctanh', 'cotanh', 'acotanh', 'arccotanh',
    'log', 'ln', 'min', 'max']


def demo():
    FORM.demo()

# =============================================================================================================================
# LaTeX simple interpreter

class Tex:

    def __init__(self, s):
        self.s     = s
        self.index = 0
        self.stack = []

    # ----------------------------------------------------------------------------------------------------
    # End of string

    @property
    def eof(self):
        return self.index >= len(self.s)

    # ----------------------------------------------------------------------------------------------------
    # Stack

    def push(self, pop_char):
        self.stack.append(pop_char)
        #print(f"{self.indent}PUSH : {self.s[self.index-1:]}")

    def pop(self, pop_char):
        #print(f"{self.indent}POP  {pop_char}: {self.s[self.index:]}")

        error = len(self.stack) == 0
        if not error:
            pc = self.stack.pop()
            error = pc != pop_char

        if error:
            raise Exception(f"Unbalanced closing char. Expected: '{pop_char}', actual: '{pc}'. {self.s[self.index:]}")

        return True

    @property
    def indent(self):
        return "   "*len(self.stack)

    # ----------------------------------------------------------------------------------------------------
    # Jump spaces

    def jump_spaces(self):
        while (self.index < len(self.s) - 1) and (self.s[self.index] == ' '):
            self.index += 1

    # ----------------------------------------------------------------------------------------------------
    # Next Char

    def next(self):
        """ Get the next char

        Translate symbols into unicode: \\alpha -> α
        """
        if self.index >= len(self.s):
            return None

        # Single char

        c = self.s[self.index]
        self.index += 1

        # White space

        if c == ' ':
            self.jump_spaces()
            return ' '

        # Escape

        elif c == "\\":

            # Next char can be { or | for instance
            word = self.s[self.index]
            self.index += 1

            # Complete with alpha if is alpha
            if word in ALPHA_CHARS:
                while not self.eof:
                    if self.s[self.index] in ALPHA_CHARS:
                        word += self.s[self.index]
                        self.index += 1
                    else:
                        break
                        # Ignore space after a a keyword

                self.jump_spaces()

            # Return the symbol if exists
            ret = SYMBOLS.get(word, "\\" + word)

        else:
            ret = c

        return ret

    # ----------------------------------------------------------------------------------------------------
    # Get the next character without consuming it

    def get_next(self):
        index = self.index
        next = self.next()
        self.index = index
        return next

    # ----------------------------------------------------------------------------------------------------
    # Is the next character a word char

    def next_is_word(self):
        n = self.get_next()
        if n is None:
            return False
        else:
            if n.startswith('\\'):
                return False

            return n not in NOT_WORD_CHARS

    # ----------------------------------------------------------------------------------------------------
    # Read a single token

    def token(self):

        self.jump_spaces()

        # ----------------------------------------------------------------------------------------------------
        # End of file
        # ----------------------------------------------------------------------------------------------------

        c = self.next()
        if c is None:
            return None

        # ----------------------------------------------------------------------------------------------------
        # Block
        # ----------------------------------------------------------------------------------------------------

        elif c in BLOCK_CHARS:

            target = BLOCK_CHARS[c]
            self.push(target)

            code = BLOCK_CODES[c]

            if c == '{':
                title = "Block"
            else:
                title = f"Block {c} ... {target}"

            with Layout(title):
                content = self.parse()
                if c == '{':
                    return content
                else:
                    return GTerm.join(type=FORM.TYPE_DECO, code=code, content=content, compile=False)

        elif c in BLOCK_CHARS.values():
            self.pop(c)
            return None

        # ----------------------------------------------------------------------------------------------------
        # Controls
        # ----------------------------------------------------------------------------------------------------

        elif c == "\\sqrt":
            content = self.parse()
            return GTerm.join(type=FORM.TYPE_DECO, code=FORM.DECO_SQRT, content=content, compile=False)._lc("Sqrt")

        elif c == '\\sum':
            ind, exp = self.indice_exponent()
            content = self.token()
            return GTerm.join(type=FORM.TYPE_SIGMA, content=content, role_1=ind, role_2=exp, compile=False)._lc("Sigma")

        elif c == '\\int':
            ind, exp = self.indice_exponent()
            content = self.token()
            return GTerm.join(type=FORM.TYPE_INTEGRAL, content=content, role_1=ind, role_2=exp, compile=False)._lc("Integral")

        elif c == "\\frac":
            numerator   = self.token()
            denominator = self.token()

            return GTerm.join(type=FORM.TYPE_FRACTION, content=numerator, role_1=denominator, compile=False)._lc("Fraction")

        elif c == '\\minus':
            content = self.enriched_token(self.token())

            return GTerm.join(type=FORM.TYPE_DECO, content=content, code=FORM.SYMB_SIGN, parameter=0, compile=False)._lc("Minus")

        elif c == '\\plus':
            content = self.enriched_token(self.token())

            return GTerm.join(type=FORM.TYPE_DECO, content=content, code=FORM.SYMB_SIGN, parameter=100, compile=False)._lc("Plus")

        elif c == '\\vec':
            content = self.enriched_token(self.token())

            return GTerm.join(type=FORM.TYPE_DECO, content=content, code=FORM.DECO_ARROW, parameter=0, compile=False)._lc("Plus")

        elif c == '=':
            return GTerm.symbol(symbol='=', compile=False)._lc("Equal")

        elif c == '+':
            return GTerm.symbol(symbol='Sign', parameter=100, compile=False)._lc("Equal")

        elif c == '-':
            return GTerm.symbol(symbol='Sign', parameter=0, compile=False)._lc("Equal")


        # ----------------------------------------------------------------------------------------------------
        # Characters
        # ----------------------------------------------------------------------------------------------------

        else:
            word = c
            while self.next_is_word():
                word += self.next()

            italic = word not in FUNCTIONS
            return GTerm.characters(characters=word, italic=italic, compile=False)

    # ----------------------------------------------------------------------------------------------------
    # Indice and exponent

    def indice_exponent(self):

        ind = None
        exp = None
        for i in range(2):
            c = self.get_next()
            if c == '_':
                if ind is None:
                    c = self.next()
                    ind = self.token()
                else:
                    return ind, exp
            elif c == '^':
                if exp is None:
                    c = self.next()
                    exp = self.token()
                else:
                    return ind, exp
            else:
                return ind, exp

        return ind, exp

    # ----------------------------------------------------------------------------------------------------
    # Enriched token
    #
    # With indices and exponent and divided by other token

    def enriched_token(self, token):

        def denominator():

            if (not SLASH_AS_FRAC) and (self.get_next() != '/'):
                return None

            _ = self.next()
            den = self.token()

            while True:
                ind, exp = self.indice_exponent()
                if (ind is None) and (exp is None):
                    break

                den = GTerm.join(type=FORM.TYPE_IND_EXP, content=den, role_1=ind, role_2=exp, compile=False)

            return den

        go_on = True
        while go_on:

            go_on = False

            while True:
                ind, exp = self.indice_exponent()
                if (ind is None) and (exp is None):
                    break
                token = GTerm.join(type=FORM.TYPE_IND_EXP, content=token, role_1=ind, role_2=exp, compile=False)
                go_on = True

            while True:
                den = denominator()
                if den is None:
                    break

                token = GTerm.join(type=FORM.TYPE_FRACTION, content=token, role_1=den, compile=False)
                go_on = True

        return token

    # ----------------------------------------------------------------------------------------------------
    # Parse : read the tokens and append them in the formula

    def parse(self):

        formula     = None

        while not self.eof:

            # ----- Read the next token

            token = self.token()
            if token is None:
                break

            # ----- Enrich with indice, exponent and denominator

            token = self.enriched_token(token)

            # ----- Append to the formula

            formula = token if formula is None else GTerm.append(formula, token, compile=False)


        return formula

# ====================================================================================================
# Build from LaTeX

def latex_nodes(latex_string, group_name):

    tex = Tex(latex_string)

    with GeoNodes(group_name):

        print("Main")
        formula = tex.parse()

        with Layout("Compile"):

            GComp.main(formula, link_from='TREE').out("Formula")
