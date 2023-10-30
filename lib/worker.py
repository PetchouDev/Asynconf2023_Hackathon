from PySide2.QtCore import QThread, QObject, Signal


class Worker(QThread, QObject):
    trigger_update = Signal()
    def __init__(self, parent=None):
        self.parent = parent
        super().__init__(parent)


    def run(self):
        while True:
            self.trigger_update.emit()
            self.msleep(500)
