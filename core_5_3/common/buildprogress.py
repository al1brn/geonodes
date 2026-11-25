"""Console progress for a build, preserving any intervening output."""
import logging
import sys


class _BuildStream:
    def __init__(self, stream, progress):
        self.stream = stream
        self.progress = progress

    def write(self, text):
        if text:
            self.progress.interrupt()
        return self.stream.write(text)

    def writelines(self, lines):
        for line in lines:
            self.write(line)

    def __getattr__(self, name):
        return getattr(self.stream, name)


class BuildProgress(logging.Filter):
    def __init__(self, label):
        super().__init__()
        self.stdout = sys.stdout
        self.stderr = sys.stderr
        self.live = self.stdout.isatty()
        self.interrupted = False
        self.closed = False
        self.label = label
        self.stdout.write(label + ('' if self.live else '\n'))
        self.stdout.flush()
        self.output = _BuildStream(self.stdout, self)
        self.errors = _BuildStream(self.stderr, self)
        sys.stdout = self.output
        sys.stderr = self.errors
        self.logger = logging.getLogger('geonodes')
        self.logger.addFilter(self)

    def interrupt(self):
        if not self.interrupted:
            self.interrupted = True
            if self.live:
                self.stdout.write('\n')
                self.stdout.flush()

    def filter(self, record):
        # A preconfigured logging handler may hold the original stderr stream.
        if record.levelno >= logging.WARNING:
            self.interrupt()
        return True

    def close(self):
        if self.closed:
            return
        self.logger.removeFilter(self)
        sys.stdout = self.stdout
        sys.stderr = self.stderr
        self.closed = True

    def finish(self, message, preserve=False):
        if preserve:
            self.interrupt()
        self.close()
        if self.live and not self.interrupted:
            self.stdout.write('\r' + ' ' * len(self.label) + '\r')
        self.stdout.write(message + '\n')
        self.stdout.flush()

    def abort(self):
        self.interrupt()
        self.close()
