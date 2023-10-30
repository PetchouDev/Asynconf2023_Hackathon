from PySide2 import QtGui, QtWidgets

from ui.mainWidget import MainWidget

class ApplicationWindow(QtWidgets.QMainWindow):
    def __init__(self, path):
        super().__init__()

        # set app title
        self.setWindowTitle("Green Bank - Simulateur d'emprunt")


        # load interface
        self.setCentralWidget(MainWidget(path))

        # set name (more convenient to apply styles)
        self.setObjectName("mainWindow")

        # load stylesheet
        self.setStyleSheet(open("ui/assets/style.qss", "r").read())




