#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Originally from the PsychoPy library
# Copyright (C) 2002-2018 Jonathan Peirce (C) 2019-2022 Open Science Tools Ltd.
# Distributed under the terms of the GNU General Public License (GPL).

"""Interfaces for serial and parallel devices.
"""

__version__ = '0.0.1'

# ------------------------------------------------------------------------------
# Generic serial and parallel interfaces
#

from .serialdevice import SerialDevice
from .parallel import setPortAddress, setPin, setData

# ------------------------------------------------------------------------------
# Components for Builder
#

from .components import SerialOutComponent, ParallelOutComponent
