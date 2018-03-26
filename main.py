import sys

from PyQt5 import QtGui
from PyQt5.QtWidgets import QMainWindow, QApplication, QFrame
from PyQt5.uic import loadUi
from vtkwidget import VtkWidget
import vtk

mainwindow_File = 'mainwindow.ui'


class MainWindow(QMainWindow):
    def __init__(self, *args):
        super(MainWindow, self).__init__(*args)
        loadUi(mainwindow_File, self)

        self.actionImportSTL.triggered.connect(self.import_stl)

        self.vtkWidget = VtkWidget(self.vtk_frame)
        self.setCentralWidget(self.vtkWidget)

        # self.ren = vtk.vtkRenderer()
        # self.vtkWidget.GetRenderWindow().AddRenderer(self.ren)
        # self.iren = self.vtkWidget.GetRenderWindow().GetInteractor()
        # self.iren.Initialize()


    def import_stl(self):
        print("importing stl")
        #sh7
        # ow dialog
        self.vtkWidget.loadFile("sample_files/beau_modele_normal.stl")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainwindow = MainWindow()
    mainwindow.show()
    sys.exit(app.exec_())
