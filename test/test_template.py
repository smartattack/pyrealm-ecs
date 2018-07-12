import pytest
import sys
import os

PACKAGE_PARENT = '../src'
SCRIPT_DIR = os.path.dirname(os.path.realpath(os.path.join(os.getcwd(), os.path.expanduser(__file__))))
sys.path.append(os.path.normpath(os.path.join(SCRIPT_DIR, PACKAGE_PARENT)))

# Pyrealm includes here

def test_something():
    pass
