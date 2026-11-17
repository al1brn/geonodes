"""Errors raised by the kaomojilang stages. They carry the line of the ORIGINAL source."""


class LangError(Exception):
    """Base class: `line` is the 1-based line in the original source, `text` that line."""

    stage = "?"

    def __init__(self, message, line=None, text=None, filename="<kaomoji>"):
        self.message = message
        self.line = line
        self.text = text
        self.filename = filename
        super().__init__(self._format())

    def _format(self):
        where = f"{self.filename}:{self.line}" if self.line else self.filename
        s = f"[{self.stage}] {where}: {self.message}"
        if self.text is not None:
            s += f"\n    {self.text.strip()}"
        return s


class Stage1Error(LangError):
    stage = "stage 1 (line translator)"


class Stage2Error(LangError):
    stage = "stage 2 (ast)"


class RunError(LangError):
    stage = "run"
