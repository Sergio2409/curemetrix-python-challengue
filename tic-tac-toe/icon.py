#!/usr/bin/env python
# -*- coding: utf-8 -*-
# -----------------------------------------------
# Copyright (c) ░s░e░r░g░i░o░v░a░l░d░e░s░2░4░0░9░
# Mail: sergiovaldes2409@gmail.com
#
# All rights reserved.
#
#
from __future__ import (division as _py3_division,
                        print_function as _py3_print,
                        absolute_import as _py3_abs_import)


class Icon(object):

    def __init__(self):
        raise NotImplementedError("You can't create instances of "
                                  "an abstract class.")

    def __repr__(self):
        return self.icon

# The icons must be implemented as Singleton pattern.


class IconX(Icon):

    def __init__(self):
        self.icon = 'X'

    def __eq__(self, other):
        if isinstance(other, IconX):
            return self.icon == other.icon
        return False


class IconO(Icon):

    def __init__(self):
        self.icon = 'O'

    def __eq__(self, other):
        if isinstance(other, IconO):
            return self.icon == other.icon
        return False
