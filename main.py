import os, sys, pathlib, ctypes

try:
    from PySide2 import QtGui, QtWidgets, QtCore
    import PySide2extn # unused, but present ot trigger an eventual ImportError
except ImportError:
    os.system(f"{sys.executable} -m pip install -r requirements.txt")
    from PySide2 import QtGui, QtWidgets, QtCore

from lib.application import ApplicationWindow



if __name__ == '__main__':
    # get the absolute path of the this file
    absolute_path = pathlib.Path(__file__).parent.absolute()
    # make sure the working directory is the same as the file's directory
    os.chdir(absolute_path)

    # set an AppUserModelID to the app to make the taskbar icon work
    ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID("petchou.greenbank.softaware.0.1")

    # create an application instance
    app = QtWidgets.QApplication(sys.argv)
    # set the app name and icon
    app.setApplicationName("Green Bank Software")
    app_icon = QtGui.QIcon()
    icon_path="ui/assets/icon.png"
    app_icon.addFile(icon_path, QtCore.QSize(16, 16))
    app_icon.addFile(icon_path, QtCore.QSize(24, 24))
    app_icon.addFile(icon_path, QtCore.QSize(32, 32))
    app_icon.addFile(icon_path, QtCore.QSize(48, 48))
    app_icon.addFile(icon_path, QtCore.QSize(256, 256))
    app.setWindowIcon(app_icon)
    window = ApplicationWindow(absolute_path)
    window.show()
    sys.exit(app.exec_())

