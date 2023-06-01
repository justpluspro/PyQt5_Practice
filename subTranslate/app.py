import sys

from PyQt5.QtWidgets import QApplication

from subTranslate.ui.MainForm import MainForm

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainForm()
    sys.exit(app.exec_())
