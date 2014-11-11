#!/usr/bin/env python

"""python-ipset setup script"""

from distutils.core import setup, Extension

# make pyflakes happy
__pkgname__ = None
__version__ = None

# build/install python-iptables
setup(
    name=__pkgname__,
    version=__version__,
    description="Python bindings for ipset",
    py_modules = ['ipset'],
    ext_modules=[Extension("_ipset",
                           ["ipset.c", "ipset.i"])],
    
    license="Apache License, Version 2.0",
)