import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from Design3 import Ui_MainWindow
from Converter import Converter


class MainWindow(QMainWindow):

    def __init__(self, converter):
        super().__init__()

        self.initUI()
        self.converter = converter

        self.ui.pushButton_2.clicked.connect(self.convertButtonClicked)

        self.ui.pushButton.clicked.connect(self.copyButtonClicked)

        self.ui.checkBox.clicked.connect(self.converter.ChangeRegisterSensitivity)

    def initUI(self):
        self.ui = Ui_MainWindow()

        self.ui.setupUi(self)

    def convertButtonClicked(self):
        newText = self.converter.GetCursedString(self.ui.lineEdit.text())
        self.ui.lineEdit_2.setText(newText)

    def copyButtonClicked(self):
        self.converter.copyTextToClipboard(self.ui.lineEdit_2.text())


if __name__ == '__main__':
    cnvrt = Converter()
    app = QApplication([])
    Window = MainWindow(cnvrt)
    Window.show()
    sys.exit(app.exec_())
