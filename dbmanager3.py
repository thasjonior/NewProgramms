
import dbsource2
import sys
import os
import re
import time
from PyQt5.QtCore import QTimer
from PyQt5.QtWidgets import QMainWindow,QAction,QDialog,QFileDialog,QFormLayout,QTextEdit,QListWidget,QLabel,QMenu,QWidget,QHBoxLayout,QLineEdit,QApplication,QVBoxLayout,QPushButton,qApp,QMenu,QGroupBox,QGridLayout

class db_source(QWidget ):
        def __init__(self):

            super().__init__()
            self.initUI()
        def initUI(self):
            self.main_layout=QVBoxLayout(self)
            self.Main_window()
            self.setGeometry(500,500,500,300)
            self.setWindowTitle('Students_Data')
            self.show()

        def get_data(self):
            self.main_layout.removeWidget(self.sub_widget1)
            self.sub_widget1.hide()
            self.sub_widget2=QWidget(self)
            self.main_layout.addWidget(self.sub_widget2)
            Glayout=QGridLayout(self)

            LMname=QLabel("Enter name:",self)
            Glayout.addWidget(LMname, 0,0)
            self.SSname=QLineEdit(self)
            Glayout.addWidget(self.SSname, 0,1)
            Searchbtn=QPushButton("Search",self)
            Searchbtn.clicked.connect(self.retrive_data)
            Glayout.addWidget(Searchbtn, 0,2)

            self.Notice=QLineEdit(self)
            Glayout.addWidget(self.Notice, 1,1)

            Lname=QLabel("Name:",self)
            Glayout.addWidget(Lname, 2,0)
            self.SName=QLineEdit(self)
            Glayout.addWidget(self.SName, 2,1)

            Lid=QLabel("ID:",self)
            Glayout.addWidget(Lid, 3,0)
            self.SId=QLineEdit(self)
            Glayout.addWidget(self.SId, 3,1)

            Lage=QLabel("Age",self)  
            Glayout.addWidget(Lage, 4,0)  
            self.SAge=QLineEdit(self)
            Glayout.addWidget(self.SAge ,4,1)

            Lmajor=QLabel("Major:", self)
            Glayout.addWidget(Lmajor, 5,0)
            self.SMajor=QLineEdit(self)
            Glayout.addWidget(self.SMajor, 5,1)

            self.Submitbtn=QPushButton("Submit",self)
            self.Submitbtn.clicked.connect(self.get_new_data)
            Glayout.addWidget(self.Submitbtn, 6,0)
            Deletebtn=QPushButton("Delete",self)
            Deletebtn.clicked.connect(self.delete_all_data)
            Glayout.addWidget(Deletebtn, 6,1)
            Cancelbtn=QPushButton("Cancel",self)
            Cancelbtn.clicked.connect(self.cancel_operation)
            Glayout.addWidget(Cancelbtn, 6,2)

            self.sub_widget2.setLayout(Glayout)
            self.sub_widget2.show()



        def Main_window(self):
            self.sub_widget1=QWidget(self)
            self.main_layout.addWidget(self.sub_widget1)

            grid=QGridLayout(self)

            srch_bar=QLineEdit(self)
            grid.addWidget(srch_bar, 0,0)
            self.pick_db_file()
            srch_btn=QPushButton("Search",self)
            grid.addWidget(srch_btn, 0,1)

            self.results=QListWidget(self)
            grid.addWidget(self.results, 1,0,1,2)

            view_btn=QPushButton("View Table",self)
            view_btn.clicked.connect( self.Present_Table)
            grid.addWidget(view_btn, 2,0)
            
            self.open_btn=QPushButton("Open",self)
            self.open_btn.setMenu(self.menu)
            self.open_btn.clicked.connect(self.pick_db_file)
            grid.addWidget(self.open_btn, 2,1)

            crt_btn=QPushButton("Create Table",self)
            crt_btn.clicked.connect(self.get_data)
            grid.addWidget(crt_btn, 3,0)

            self.sub_widget1.setLayout(grid)
            

        def pick_db_file(self):
            self.menu=QMenu(self)
            for file in  os.scandir(r'/home/judethaddeus/Documents/My_projects/py_projects/backups'):
                partten=r'(\.db)$'
                matches=re.findall(partten,file.name)
                for _ in  range(len(matches)):
                    action=self.menu.addAction(file.name)
                    action.triggered.connect( self.trial)
        def trial(self):
            source=self.sender()
            dbsource2.conn=dbsource2.get_dbFile(source.text())
            dbsource2.c=dbsource2.conn.cursor()
            print(source.text()) 
            self.Present_Table()

        def get_new_data(self):
            print(self.SName.text())
            Sdata=dbsource2.Student(self.SName.text(),self.SId.text(),self.SAge.text(),self.SMajor.text())
            dbsource2.Insert_data_tuple(Sdata)
            self.SName.clear()
            self.SId.clear()
            self.SAge.clear()
            self.SMajor.clear()

        def retrive_data(self):
            dbsource2.container
            dbsource2.Select_allData(self.SSname.text())
            if not dbsource2.container:
                self.Notice.clear()
                self.Notice.setText(f"No results found for : {self.SSname.text()}")
                self.Notice.setStyleSheet("color:red")                
                return
            self.SName.setText(dbsource2.container[0])
            self.SId.setText(dbsource2.container[1])
            self.SAge.setText(str(dbsource2.container[2]))
            self.SMajor.setText(dbsource2.container[3])
            try:
                self.Submitbtn.clicked.disconnect(self.get_new_data)
                self.Submitbtn.setText("Update")
                self.Submitbtn.clicked.connect(self.Update_chages)
            except :
                pass
            dbsource2.container.clear()



        def Update_chages(self):
            self.Submitbtn.setText("Submit")
            self.Submitbtn.clicked.disconnect(self.Update_chages)
            self.Submitbtn.clicked.connect(self.get_new_data)
            Modified_data=dbsource2.Student(self.SName.text(),self.SId.text(),self.SAge.text(),self.SMajor.text())
            print(Modified_data)
            dbsource2.Update_data(Modified_data,self.SSname.text())
            self.SSname.clear()
            self.SName.clear()
            self.SId.clear()
            self.SAge.clear()
            self.SMajor.clear()

        def delete_all_data(self):
            dbsource2.Delete_data_Name(self.SSname.text())
            self.SSname.clear()
            self.SName.clear()
            self.SId.clear()
            self.SAge.clear()
            self.SMajor.clear()

        def Present_Table(self):
            self.results.clear()
            dbsource2.ss.clear()
            dbsource2.Read_all_contents()
            for row in dbsource2.ss:
                self.results.addItem(str(row))
            print("Table presented")
            
            
        

        
        def cancel_operation(self):
            self.main_layout.removeWidget(self.sub_widget2)
            self.sub_widget2.hide()
            self.Main_window()
                    


            # dbsource2.get_dbFile(self.Name)
                

                    





if __name__=='__main__':
        app=QApplication(sys.argv)
        db=db_source()
        sys.exit(app.exec_())



