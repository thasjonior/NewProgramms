# this example shows  a tooltip on a window and a button 
import  sys 
from PyQt5.QtWidgets import (QWidget , QToolTip,QPushButton,QApplication)
from PyQt5.QtGui import QFont

class Example(QWidget):
    def __init__ (self):
        super().__init__()
        self.initUI()
    def initUI(self):
        QToolTip.setFont(QFont('SansSerif',10))

        self.setToolTip('This is a <b>Widget</b> widget')

        btn=QPushButton('Buttton',self)
        btn.setToolTip('this is a <b>PushButton</b> widget')
        btn.move(50,50)

        self.setGeometry(300,300,300,220)
        self.setWindowTitle('Tooltips')
        self.show()
    
if __name__=='__main__':
    app=QApplication(sys.argv)
    ex=Example()
    sys.exit(app.exec_())