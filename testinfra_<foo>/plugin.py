# -*- coding: utf8 -*-

import pytest


@pytest.fixture()
def <foo>(Command):

    def f(arg):
        return Command.check_output("<foo> %s", arg)

    return f
