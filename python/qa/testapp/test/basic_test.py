"""Tests validating the basic functionality of testapp."""

from qa.framework.testcase import TestAppTestCase

class BasicTest(TestAppTestCase):
    """Basics tests of the test_app functionality."""

    def test_run_app(self):
        """Test the basic running of the app with no options, or input."""

        self.run_app()
