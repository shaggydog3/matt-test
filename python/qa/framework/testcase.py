#!/bin/python

"""Classes and methods for controlling test cases."""

import os
import time

from qa.framework import harness
from unittest import TestCase


class ComponentTestCase(TestCase):
    """base class for testing a component.

    This class will contain test methods common to all the components under test.
    """

    def setUp(self):
        super(ComponentTestCase, self).setUp()
        self.test_path_name = self.id()
        self.test_name = self.test_path_name.split('.')[-1:][0]
        self.framework_dir = os.path.dirname(__file__)
        self.reporoot = '/{0}'.format(os.path.join(*self.framework_dir.split('/')[:-3]))

    def printlog(self, message, logtype='DEBUG'):
        """A simple method to output a log message to standard out during the test.

        TODO: This is a temporary measure.  This will be replaced by a more detailed
        log system.
        """

        print '\n{0} {1}: {2}'.format(time.asctime(), logtype, message)


class TestAppTestCase(ComponentTestCase):
    """This class contains methods for testing test_app

    TODO: a template for now.  As more functionality develops that needs specific test
    methods, this class will contain those methods.
    """

    def setUp(self):
        super(TestAppTestCase, self).setUp()
        self.testapp = None

    def run_app(self):
        """Run the teset app."""

        self.testapp = harness.TestAppHarness(os.path.join(self.reporoot, 'python', 'app'
                                                           , 'test_app.py'))
