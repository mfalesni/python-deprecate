# -*- coding: utf-8 -*-
"""Based on https://wiki.python.org/moin/PythonDecoratorLibrary#Generating_Deprecation_Warnings"""
import warnings
import functools


def deprecated(func):
    """Mark deprecated functions with this decorator.

    Attention! Use it as the closest one to the function you decorate.
    """
    @functools.wraps(func)
    def new_func(*args, **kwargs):
        code = func.func_code if hasattr(func, "func_code") else func.__code__
        warnings.warn_explicit(
            "Call to deprecated function {}.".format(func.__name__),
            category=DeprecationWarning,
            filename=code.co_filename,
            lineno=code.co_firstlineno + 1
        )
        return func(*args, **kwargs)
    return new_func
