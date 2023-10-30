from PySide2 import QtWidgets, QtCore, QtGui
from PySide2.QtCore import Qt

from PySide2extn.RoundProgressBar import roundProgressBar


class Selector(QtWidgets.QWidget):
    def __init__(self, name, data: dict, parent=None):
        super().__init__(parent)
        self.data = data
        self.name = name
        self.setMinimumSize(325, 275)

        self.initUI()

    def initUI(self):
        # add a vertical layout
        self.rows = QtWidgets.QVBoxLayout(self)
        self.setLayout(self.rows)

        # add a horizontal layout for the name of the selector
        self.nameRow = QtWidgets.QHBoxLayout()

        # add a label to the name row
        self.nameLabel = QtWidgets.QLabel(self.name)

        self.nameLabel.setObjectName('selectorLabel')
        self.nameLabel.setAlignment(Qt.AlignCenter)
        self.nameRow.addWidget(self.nameLabel)

        # add a horizontal layout for the score circular bar
        self.selectorRow = QtWidgets.QHBoxLayout()

        # add a circular bar to the selector row
        self.bar = roundProgressBar()
        self.bar.rpb_setBarStyle('Donet')
        self.bar.rpb_setTextFormat('Value')
        if self.name != "Passagers":
            self.bar.rpb_setRange(0, 10)
        else:
            self.bar.rpb_setRange(0, 4)
        self.bar.rpb_setTextRatio(2)
        self.bar.rpb_setTextFont('Comic Sans')
        self.bar.rpb_setPathWidth(10)
        self.bar.rpb_setPathColor((123, 123, 123))
        self.bar.rpb_setValue(3)
        self.bar.rpb_setLineWidth(20)
        self.bar.rpb_setLineCap('RoundCap')

        # add a stretch to the left and right of the bar (since QtCore.Qt.AlignCenter seeems to not work)
        self.selectorRow.addStretch(1)
        self.selectorRow.addWidget(self.bar)
        self.selectorRow.addStretch(1)

        # make the bar take the max space
        self.nameLabel.setSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        self.bar.setSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)

        # add a horizontal layout for the combo box
        self.comboBoxRow = QtWidgets.QHBoxLayout()

        # add a combo box to the combo box row
        self.comboBox = QtWidgets.QComboBox()
        self.comboBoxRow.addWidget(self.comboBox)

        # add items to combo box (inculde a default item)
        self.comboBox.addItems(["Sélectionnez une option"] + list(self.data.keys()))

        # make 'Sélectionnez une option' the default item
        self.comboBox.setCurrentIndex(0)

        # center text in the combo box
        self.comboBox.setLineEdit(QtWidgets.QLineEdit(self))
        self.comboBox.lineEdit().setAlignment(Qt.AlignCenter)

        # disable interaction with the combo box line edit
        self.comboBox.lineEdit().setReadOnly(True)

        # trigger the combo box when the user clicks on the widget
        self.mousePressEvent = lambda event: self.comboBox.showPopup()


        # center the combo box in the row
        self.comboBoxRow.setAlignment(Qt.AlignCenter)

        # allow combo box to take max space, with 250px max width
        self.comboBox.setSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)


        # add the 3 rows to the layout
        self.rows.addLayout(self.nameRow)
        self.rows.addStretch(1)
        self.rows.addLayout(self.selectorRow)
        self.rows.addStretch(1)
        self.rows.addLayout(self.comboBoxRow)


    def set_color(self, color):
        self.bar.rpb_setLineColor(color)
        self.bar.rpb_setTextColor(color)
