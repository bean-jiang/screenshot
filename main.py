import gc
import math
import os
import sys
import time
import cv2

from PyQt5.QtWidgets import QWidget,QApplication
from pp.TestWin import TestWin


app = QApplication(sys.argv)
s = TestWin()
s.show()

sys.exit(app.exec_())
