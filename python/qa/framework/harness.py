"""Contains a set of classes for manipulating test applications."""

import subprocess


class ProcessHarness(object):
    """This is the base class for a process harness."""

    def __init__(self, cmd):
        """Initialize and launch the process.

        Args:
            cmd: The full path/filename of the process to run.
        """

        self.cmd = cmd
        self.launch()

    def launch(self):
        """Launch the process."""

        subprocess.call(self.cmd)


class TestAppHarness(ProcessHarness):
    """Harness for running the test_app.

    TODO: This is a template for now.  This will be expanded as the functionality of
    the test_app develops."""

    def __init__(self, cmd):
        super(TestAppHarness, self).__init__(cmd)
