#!/usr/bin/env python

"""python-ipset setup script"""

from distutils.core import setup, Extension

# make pyflakes happy
__pkgname__ = "ipset"
__version__ = None

# build/install 
setup(
    name=__pkgname__,
    version=__version__,
    description="Python bindings for adding/removing to an ipset",
    py_modules = ['ipset'],
    ext_modules=[Extension("_ipset",
                           ["ipset.c", "ipset.i"])],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'License :: OSI Approved :: Apache License',
        'Operating System :: Linux',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    license="Apache License, Version 2.0",
)
