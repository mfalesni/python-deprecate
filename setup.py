#!/usr/bin/env python2
# -*- encoding: utf-8 -*-
#   Author(s): Milan Falesnik   <milan@falesnik.net>
#                               <mfalesni@redhat.com>
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

from setuptools import setup


setup(
    name="deprecate",
    version="1.0.4",
    author="Milan Falešník",
    author_email="milan@falesnik.net",
    description="Python deprecating solution.",
    license="GPLv3,MPLv2",
    keywords="deprecate",
    url="https://github.com/mfalesni/python-deprecate",
    packages=["deprecate"],
    package_dir={'': 'src'},
    install_requires=[],
    classifiers=[
        "Topic :: Utilities",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "License :: OSI Approved :: Mozilla Public License 2.0 (MPL 2.0)",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3.3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Intended Audience :: Developers",
        "Development Status :: 4 - Beta",
    ]
)
