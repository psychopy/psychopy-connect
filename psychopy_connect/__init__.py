#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Originally from the PsychoPy library
# Copyright (C) 2002-2018 Jonathan Peirce (C) 2019-2022 Open Science Tools Ltd.
# Distributed under the terms of the GNU General Public License (GPL).

"""Interfaces for serial and parallel devices.
"""

__version__ = '0.0.2'

# ------------------------------------------------------------------------------
# Generic serial and parallel interfaces
#

from .serialdevice import SerialDevice
from .parallel import (
    ParallelPort,
    setPortAddress,
    setPin,
    setData,
    readPin)

# platform-specific drivers, make them available since need them
from .parallel._linux import PParallelLinux
from .parallel._inpout import PParallelInpOut
from .parallel._dlportio import PParallelDLPortIO

# ------------------------------------------------------------------------------
# Components for Builder
#

from .components import SerialOutComponent, ParallelOutComponent
