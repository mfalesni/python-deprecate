# -*- coding: utf-8 -*-
import warnings

from deprecate import deprecated, DeprecationDecorator

import pytest


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


class TestDeprecationDecorator:
    @pytest.mark.parametrize('message, expected', [
        (None, 'Call to deprecated function deprecated_function'),
        ("Test", "Test"),
    ])
    def test_make_message(self, message, expected):
        decorator = DeprecationDecorator(message=message)
        computed_message = decorator._message_for_func(deprecated_function)
        assert computed_message == expected
