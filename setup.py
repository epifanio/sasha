#!/usr/bin/env python
###############################################################################
#
#
# Project:
# Purpose:
#
#
# Author:   Massimo Di Stefano , epiesasha@me.com
#
###############################################################################
# Copyright (c) 2009, Massimo Di Stefano <epiesasha@me.com>
#
# Permission is hereby granted, free of charge, to any person obtaining a
# copy of this software and associated documentation files (the "Software"),
# to deal in the Software without restriction, including without limitation
# the rights to use, copy, modify, merge, publish, distribute, sublicense,
# and/or sell copies of the Software, and to permit persons to whom the
# Software is furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included
# in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS
# OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL
# THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
# FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
# DEALINGS IN THE SOFTWARE.
###############################################################################

__author__ = "Massimo Di Stefano"
__copyright__ = "Copyright 2009, gfoss.it"
__credits__ = [""]
__license__ = "GPL V3"
__version__ = "1.0.0"
__maintainer__ = "Massimo Di Stefano"
__email__ = "epiesasha@me.com"
__status__ = "Production"
__date__ = ""

from cx_Freeze import setup, Executable

setup(
        name = "Sasha",
        version = "0.1",
        description = "Sasha",
        executables = [Executable("sasha.py")])