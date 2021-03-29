import sys

from PySide2 import QtWidgets

from app.UI.window.mainWindow import MainWindow

from app.assets.config.settings import icon


def create_app():
    app = QtWidgets.QApplication(sys.argv)

    x = MainWindow()
    app.setStyleSheet("QCheckBox::indicator {"
                      " border : none;}"
                      "QCheckBox::indicator:checked {"
                      f"image: url({icon.CHECKMARK_I()});"
                      "width:16px;"
                      "height:16px;"
                      "}"
                      "QCheckBox::indicator:unchecked {"
                      f"image: url({icon.DELETE_I()});"
                      "width:16px;"
                      "height:16px;"
                      "}"
                      )

    sys.exit(app.exec_())
