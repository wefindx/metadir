"""Tests for our main scanme module."""


from subprocess import PIPE, Popen as popen
from unittest import TestCase

from scanme import __version__ as VERSION


class TestHelp(TestCase):
    def test_returns_usage_information(self):
        output = popen(['scanme', '-h'], stdout=PIPE).communicate()[0]
        self.assertTrue(bytes('Usage:', 'utf-8') in output)

        output = popen(['scanme', '--help'], stdout=PIPE).communicate()[0]
        self.assertTrue(bytes('Usage:', 'utf-8') in output)


class TestVersion(TestCase):
    def test_returns_version_information(self):
        output = popen(['scanme', '--version'], stdout=PIPE).communicate()[0]
        self.assertEqual(output.strip(), bytes(VERSION, 'utf-8'))
