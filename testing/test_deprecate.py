# -*- coding: utf-8 -*-
import warnings

from deprecate import deprecated


@deprecated
def deprecated_function():
    pass


def test_warns(recwarn):
    warnings.simplefilter("always")
    deprecated_function()
    assert len(recwarn) == 1
    w = recwarn.pop(DeprecationWarning)
    assert issubclass(w.category, DeprecationWarning)
    assert str(w.message) == "Call to deprecated function {}".format(
        deprecated_function.__name__)
