import os, json

from PySide2 import QtWidgets, QtCore, QtGui

from ui.selectorWidget import Selector
from ui.resultWidget import  ResultWidget
from ui.colors import COLORS, GOOD, BAD
from lib.worker import Worker


class MainWidget(QtWidgets.QWidget):
    def __init__(self, path):
        super().__init__()
        self.path = path
        self.load_data()
        self.initUI()

        self.initWorker()

    def initUI(self):
        self.setObjectName("mainWidget")
        # add a vertical layout to the main widget
        self.main_layout = QtWidgets.QVBoxLayout(self)
        self.setLayout(self.main_layout)

        # add a horizontal layout for the title
        self.titleRow = QtWidgets.QHBoxLayout()
        self.main_layout.addLayout(self.titleRow)

        # add a label to the title row
        self.title = QtWidgets.QLabel("Green Bank - Simulateur d'emprunt")
        self.titleRow.addWidget(self.title)
        self.title.setAlignment(QtCore.Qt.AlignCenter)
        self.title.setObjectName("title")

        # add a vertical layout for the 2 rows
        self.rows = QtWidgets.QVBoxLayout()
        self.main_layout.addLayout(self.rows)

        # make the title row take the minimal height possible to allow the 2 rows to take the max space
        self.main_layout.setStretch(0, 0)
        self.main_layout.setStretch(1, 1)

        # create the 2 rows
        self.row1 = QtWidgets.QHBoxLayout()
        self.row2 = QtWidgets.QHBoxLayout()

        # create a dictionary for the selectors
        self.selectors = {
            key: Selector(key, value) for key, value in self.data.items()
        }

        keys = list(self.selectors.keys())
        i = -1  # Used an icrement variable to get the key from the dictionary (and to try walrus operator)

        # add the selectors to the first row
        self.row1.addStretch(2)
        self.row1.addWidget(self.selectors[keys[(i := i + 1)]])
        self.row1.addStretch(1)
        self.row1.addWidget(self.selectors[keys[(i := i + 1)]])
        self.row1.addStretch(1)
        self.row1.addWidget(self.selectors[keys[(i := i + 1)]])
        self.row1.addStretch(2)

        # create result widget for the second row
        self.result = ResultWidget()
        # add widgets to the second row
        self.row2.addStretch(2)
        self.row2.addWidget(self.selectors[keys[(i := i + 1)]])
        self.row2.addStretch(1)
        self.row2.addWidget(self.result)
        self.row2.addStretch(1)
        self.row2.addWidget(self.selectors[keys[(i := i + 1)]])
        self.row2.addStretch(2)

        # add the 2 rows to the main layout
        self.rows.addStretch(1)
        self.rows.addLayout(self.row1)
        self.rows.addStretch(1)
        self.rows.addLayout(self.row2)
        self.rows.addStretch(1)

    def initWorker(self):
        self.worker = Worker(self)
        self.worker.trigger_update.connect(self.update)
        self.worker.start()

    def load_data(self):
        with open(self.path / 'data' / 'baremes.json', 'r') as f:
            self.data = json.load(f)

    def update(self):
        score = 0
        passagers = 0
        for name, selector in self.selectors.items():
            if name != "Passagers":
                # update the bar value
                value = self.data[name].get(selector.comboBox.currentText(), 0)
                score += value
                selector.bar.rpb_setValue(value)
                # update the color of the bar and the label
                selector.set_color(COLORS[int(value)])
            else:
                # update the bar value
                value = selector.comboBox.currentText()

                passagers = value
                try:
                    value = int(value)
                except:
                    value = 0  # handles the case where the user selects "Sélectionnez une option"
                selector.bar.rpb_setValue(value)
                # update the color of the bar and the label
                selector.set_color(COLORS[int(value * 2.5)])

        # arrondir le score
        score = round(score)

        taux = 0
        for i in self.data["taux"].keys():
            if int(i.split("-")[0]) <= score <= int(i.split("-")[1]):
                taux = self.data["taux"][i]
                break
        self.result.ratio.setText(f"Taux: {taux}% ({score}/40)")
        self.result.ratio.setStyleSheet(f"color: rgb{COLORS[int(score / 4)]}; font-size: 30px; font-weight: bold;")


        malus = self.data["Passagers"].get(passagers, 0)
        self.result.malus.setText(f"{'Bonus' if malus >= 0 else 'Malus'}: {abs(malus)}")
        self.result.malus.setStyleSheet(f"color: {GOOD if malus >= 0 else BAD}; font-size: 35px; font-weight: bold;")

        self.result.total.setText(f"Total: {taux - malus: .2f}%")

