"""Default console formatting for geonodes diagnostics."""
import logging
import os
import re
import sys


class ConsoleFormatter(logging.Formatter):
    def format(self, record):
        color = (sys.stderr.isatty() and os.environ.get('TERM') != 'dumb'
                 and 'NO_COLOR' not in os.environ)
        label = 'CAUTION' if record.levelno == logging.WARNING else record.levelname
        if color and record.levelno == logging.WARNING:
            label = '\033[38;5;208m' + label + '\033[0m'
        lines = [f'{label}: {record.getMessage()}']
        origin = getattr(record, 'geonodes_origin', None)
        if origin:
            location = origin[0]
            match = re.fullmatch(r"File '(.*)', line (\d+)", location)
            if match:
                location = f'{match[1]}:{match[2]}'
            if color:
                location = '\033[90m' + location + '\033[0m'
            lines.append(location)
            for source in origin[1:]:
                number, separator, code = source.partition('>')
                lines.append(f'{number}> {code.strip()}' if separator else source)
        if record.exc_info:
            lines.append(self.formatException(record.exc_info))
        return '\n'.join(lines)


class ConsoleHandler(logging.StreamHandler):
    def emit(self, record):
        # Follow Blender redirection and the temporary build-progress streams.
        self.stream = sys.stderr
        super().emit(record)


def get_logger():
    logger = logging.getLogger('geonodes')
    if not logger.handlers:
        handler = ConsoleHandler()
        handler.setFormatter(ConsoleFormatter())
        logger.addHandler(handler)
        logger.propagate = False
    return logger
