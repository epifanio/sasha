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


import sys
import os
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from sashaGui import GuiWidget
from VectorOp import VectorOperation

try:
    _fromUtf8 = QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class PlanetSasha(QObject):
    def init(self,arg1):
        self.w = GuiWidget()
        self.vectoroperation = VectorOperation()
        self.slstep = 1
        self.connect(self.w.actionVectorOp, SIGNAL("triggered()"), self.Geom) 
        self.connect(self.w.actionExit, SIGNAL("triggered()"), self.quitAll)        
        self.w.show()
            
    def quitAll(self):
        qApp.quit()

    def Geom(self):
        self.vectoroperation.show()
    
if __name__ == "__main__":
    import sys
    import time
    app = QApplication(sys.argv)
    arg1 = ''
    if len(sys.argv) > 1:
        arg1 = sys.argv[1]
    time.sleep(1)
    app.processEvents()
    p = PlanetSasha()
    p.init(arg1)
    sys.exit(app.exec_())





