from PySide2 import QtWidgets, QtCore

class ResultWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setObjectName('result')
        self.initUI()

    def initUI(self):
        # set max width to 350px
        self.setMaximumWidth(350)

        self.rows = QtWidgets.QVBoxLayout()
        self.setLayout(self.rows)

        # create a label to show the ratio
        self.ratio = QtWidgets.QLabel("Taux : 0% (23/40)")
        self.ratio.setAlignment(QtCore.Qt.AlignCenter)
        self.ratio.setStyleSheet("font-size: 30px; font-weight: bold;")

        # create a label for the total
        self.total = QtWidgets.QLabel("Total : 0%")
        self.total.setAlignment(QtCore.Qt.AlignCenter)
        self.total.setStyleSheet("font-size: 55px; color: #309fb3; font-weight: bold; ")

        # create a label for the malus
        self.malus = QtWidgets.QLabel("Malus : 0%")
        self.malus.setAlignment(QtCore.Qt.AlignCenter)
        self.malus.setStyleSheet("font-size: 35px; color: #9c1902; font-weight: bold; ")

        # add labels to the layout
        self.rows.addStretch(1)
        self.rows.addWidget(self.ratio)
        self.rows.addStretch(1)
        self.rows.addWidget(self.total)
        self.rows.addStretch(1)
        self.rows.addWidget(self.malus)
        self.rows.addStretch(1)






