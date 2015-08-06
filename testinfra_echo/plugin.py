# -*- coding: utf8 -*-

import pytest


@pytest.fixture(scope="session")
def Echo(Command):

    def f(arg):
        return Command.check_output("echo %s", arg)

    return f
