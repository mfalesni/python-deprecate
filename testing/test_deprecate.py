# -*- coding: utf-8 -*-
import pytest
import warnings

from deprecate import deprecated


@pytest.fixture(scope="module")
def deprecated_f():
    @deprecated
    def function():
        pass
    return function


def test_warns(deprecated_f):
    with warnings.catch_warnings(record=True) as w:
        warnings.simplefilter("always")
        deprecated_f()
        assert len(w) == 1
        assert issubclass(w[-1].category, DeprecationWarning)
        assert str(w[-1].message) == "Call to deprecated function {}.".format(deprecated_f.__name__)
