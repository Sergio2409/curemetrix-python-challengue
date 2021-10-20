#!/usr/bin/env python
# -*- coding: utf-8 -*-
# -----------------------------------------------
# Copyright (c) ░s░e░r░g░i░o░v░a░l░d░e░s░2░4░0░9░
# Mail: sergiovaldes2409@gmail.com
#
# All rights reserved.
#
#
"""
Module description goes here

"""

from __future__ import (division as _py3_division,
                        print_function as _py3_print,
                        absolute_import as _py3_abs_import)

from players import Human, Computer
from icon import IconO, IconX


class GameMode(object):

    def restart(self):
        self.player1.moves = []
        self.player2.moves = []

    def __new__(cls, *args, **kw):
        orig = super(GameMode, cls)
        instance = orig.__new__(cls, *args, **kw)
        instance.draws = 0
        return instance


class HumanVSComputer(GameMode):

    def __init__(self, knowledge_base=None):
        self.player1 = Human()
        self.player2 = Computer(name='MLComputer')


class HumanVSHuman(GameMode):
    def __init__(self, player1='Human Player1', player2='Human Player2'):
        self.player1 = Human(name=player1, icon=IconX())
        self.player2 = Human(name=player2, icon=IconO())


class ComputerVSComputer(GameMode):
    def __init__(self, player1='Novice', player2='MLComputer', knowledge_base=None):
        self.player1 = Computer(name='Random', icon=IconX(), knowledge_base=knowledge_base, level='smart')
        self.player2 = Computer(name='SergioML', icon=IconO(), level='expert',
                                knowledge_base=knowledge_base)
