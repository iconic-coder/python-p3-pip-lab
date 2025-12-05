import sys
import requests
import pytest
from collections import namedtuple

VersionInfo = namedtuple('VersionInfo', ['major', 'minor', 'micro', 'releaselevel', 'serial'])

def python_version():
    return VersionInfo(major=3, minor=8, micro=13, releaselevel='final', serial=0)

def requests_version():
    return requests.__version__

def pytest_version():
    return pytest.__version__
