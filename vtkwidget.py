from vtk.qt.QVTKRenderWindowInteractor import QVTKRenderWindowInteractor
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMenu
import vtk


class VtkWidget(QVTKRenderWindowInteractor):
    """
    VtkWidget that controls the interface
    """
    def __init__(self, parent):
        super().__init__(parent)
        self.right_click = False
        self.moved = False
        self.last_mouse_point = [0, 0]
        self.ren = vtk.vtkRenderer()
        self.GetRenderWindow().AddRenderer(self.ren)
        self.iren = self.GetRenderWindow().GetInteractor()
        self.iren.Initialize()

    def mousePressEvent(self, ev):
        ctrl, shift = self._GetCtrlShift(ev)
        if ev.button() == Qt.LeftButton:
            print("left button")
            print(ev.x(), ev.y())
            picker = vtk.vtkPropPicker()
            picker.Pick(ev.x(), ev.y(), 0, self.ren)
            last_act = picker.GetActor()

            print(last_act)
        if ev.button() == Qt.RightButton:
            self.right_click = True

    def mouseMoveEvent(self, ev):
        self.moved = True
        if self.right_click:
            print("right move")

        self.last_mouse_point[0] = ev.x()
        self.last_mouse_point[1] = ev.y()

    def mouseReleaseEvent(self, ev):
        if ev.button() == Qt.RightButton:
            if self.moved:
                print("right moved")
            else:
                print("context menu")
                menu = QMenu(self)
                temp_action = menu.addAction("temp")
                action = menu.exec_(ev.globalPos())

            self.right_click = False

        self.moved = False

    def loadFile(self, filename):
        reader = vtk.vtkSTLReader()
        reader.SetFileName(filename)

        mapper = vtk.vtkPolyDataMapper()
        # Create a mapper
        mapper.SetInputConnection(reader.GetOutputPort())

        # Create an actor
        actor = vtk.vtkActor()
        actor.SetMapper(mapper)

        transform = vtk.vtkTransform()
        transform.Translate(0.0, 0.0, 0.0)

        axes = vtk.vtkAxesActor()
        axes.SetXAxisLabelText("asd")
        axes.SetTotalLength([4.0,4.0,4.0])
        #  The axes are positioned with a user transform
        axes.SetUserTransform(transform)
        actor.SetUserTransform(transform)
        self.ren.AddActor(axes)
        self.ren.AddActor(actor)
        self.ren.ResetCamera()
