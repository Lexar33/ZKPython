
from PyQt5.QtWidgets import QApplication,QLabel
from PyQt5.QtCore import Qt

import ctypes
dll= ctypes.cdll.LoadLibrary('zkemkeeper.dll') 


app= QApplication([])

lbl=QLabel('Hello World')
lbl.setStyleSheet('font-size:20pt')
lbl.setMinimumSize(400,400)
lbl.setWindowTitle('Hello World')
lbl.setAlignment(Qt.AlignCenter)
lbl.show()

app.exec_()