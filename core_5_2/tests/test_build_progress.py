"""Run without Blender: python3 core_5_2/tests/test_build_progress.py."""
from contextlib import redirect_stderr, redirect_stdout
import io
import logging
from pathlib import Path
import runpy
import sys
import unittest

BuildProgress = runpy.run_path(str(Path(__file__).resolve().parents[1]
                                 / 'common/buildprogress.py'))['BuildProgress']


class Terminal(io.StringIO):
    def isatty(self):
        return True


class BuildProgressTest(unittest.TestCase):
    def test_success_replaces_the_pending_line_in_a_terminal(self):
        stream = Terminal()
        with redirect_stdout(stream):
            progress = BuildProgress("Build Tree 'Test'")
            progress.finish('Test built')
            self.assertIs(sys.stdout, stream)
        self.assertIn('\r', stream.getvalue())
        self.assertTrue(stream.getvalue().endswith('Test built\n'))

    def test_printed_warning_is_preserved(self):
        stream = Terminal()
        with redirect_stdout(stream):
            progress = BuildProgress('Build Test')
            print('Caution: invalid link')
            progress.finish('Test built')
        self.assertEqual(stream.getvalue(), 'Build Test\nCaution: invalid link\nTest built\n')

    def test_preconfigured_logging_handler_is_preserved(self):
        stream = Terminal()
        logger = logging.getLogger('geonodes')
        handler = logging.StreamHandler(stream)
        logger.addHandler(handler)
        try:
            with redirect_stdout(stream):
                progress = BuildProgress('Build Test')
                logger.warning('Deprecated syntax')
                progress.finish('Test built')
            self.assertEqual(stream.getvalue(), 'Build Test\nDeprecated syntax\nTest built\n')
            self.assertNotIn(progress, logger.filters)
        finally:
            logger.removeHandler(handler)

    def test_error_keeps_start_line_and_restores_streams(self):
        stream = Terminal()
        errors = io.StringIO()
        with redirect_stdout(stream), redirect_stderr(errors):
            progress = BuildProgress('Build Test')
            progress.finish('Test built', preserve=True)
            self.assertIs(sys.stderr, errors)
        self.assertEqual(stream.getvalue(), 'Build Test\nTest built\n')

    def test_redirected_output_contains_two_plain_lines(self):
        stream = io.StringIO()
        with redirect_stdout(stream):
            progress = BuildProgress('Build Test')
            progress.finish('Test built')
        self.assertEqual(stream.getvalue(), 'Build Test\nTest built\n')

    def test_nested_builds_preserve_parent_and_restore_streams(self):
        stream = Terminal()
        with redirect_stdout(stream):
            outer = BuildProgress('Build Outer')
            inner = BuildProgress('Build Inner')
            inner.finish('Inner built')
            self.assertIs(sys.stdout, outer.output)
            self.assertTrue(outer.interrupted)
            outer.finish('Outer built')
            self.assertIs(sys.stdout, stream)
        self.assertTrue(stream.getvalue().endswith('Inner built\nOuter built\n'))

    def test_abort_restores_streams_even_without_a_summary(self):
        stream = Terminal()
        with redirect_stdout(stream):
            progress = BuildProgress('Build Test')
            progress.abort()
            self.assertIs(sys.stdout, stream)
        self.assertEqual(stream.getvalue(), 'Build Test\n')


if __name__ == '__main__':
    unittest.main()
