#!/usr/bin/env python2
# -*- encoding: utf-8 -*-
#   Author(s): Milan Falesnik   <milan@falesnik.net>
#                               <mfalesni@redhat.com>
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

from setuptools import setup


setup(
    name="deprecate",
    version="1.0.1",
    author="Milan Falešník",
    author_email="milan@falesnik.net",
    description="Python function kwargifier",
    license="GPLv3",
    keywords="kwargs",
    url="https://github.com/mfalesni/python-deprecate",
    py_modules=["deprecate"],
    install_requires=[],
    classifiers=[
        "Topic :: Utilities",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
    ]
)
