import sys
from PyQt5.QtWidgets import QMainWindow,QAction,QApplication,qApp

class Example (QMainWindow):

        def __init__(self):
                super().__init__()
                self.initUI()
        
        def initUI(self):

                exit1=QAction('&Exit',self)
                exit1.triggered.connect(qApp.quit)

                self.statusBar()
                menubar=self.menuBar()
                filemenu=menubar.addMenu('File')
                filemenu.addAction(exit1)

                self.setGeometry(300,300,300,200)
                self.setWindowTitle('sijui hii')
                self.show()


if __name__ == '__main__':

        app=QApplication(sys.argv)
        ex=Example()
        sys.exit(app.exec_())