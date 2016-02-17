# -*- coding: utf-8 -*-
import warnings
import functools


class DeprecationDecorator(object):
    def __init__(self, category=DeprecationWarning, message=None):
        self.category = category
        self.message = message

    def _message_for_func(self, func):
        if self.message:
            return self.message
        else:
            return "Call to deprecated function " + func.__name__

    def __call__(self, func):

        return _wrap_with_deprecation(func, self.category,
                                      self._message_for_func(func))


def _wrap_with_deprecation(func, category, message, stacklevel=2):
    @functools.wraps(func)
    def new_func(*args, **kwargs):
        warnings.warn(message, category=category, stacklevel=stacklevel)
        return func(*args, **kwargs)

    # work around a bug in functools.wraps thats fixed in python 3.2
    if getattr(new_func, '__wrapped__', None) is None:
        new_func.__wrapped__ = func
    return new_func


def deprecated(func=None, **kw):
    """Mark deprecated functions with this decorator.

    Attention! Use it as the closest one to the function you decorate.
    """
    decorator = DeprecationDecorator(**kw)
    return decorator(func) if func else decorator
