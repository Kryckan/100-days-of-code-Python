import os

from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtGui import QFontDatabase, QPixmap
from PyQt5.QtWidgets import (
    QApplication,
    QHBoxLayout,
    QLabel,
    QPushButton,
    QVBoxLayout,
    QWidget,
)


class MyPass(QWidget):
    FONT_NAMES = ["poppins", "Courier", "Arial", "Helvetica", "Times New Roman"]

    def __init__(self):
        super().__init__()
        # self.check_fonts_availability()
        self.setup_ui()
        self.current_dir = os.path.dirname(os.path.abspath(__file__))
        self.emmail_address = "kryckan@gmail.com"

    def setup_ui(self):
        self.setWindowTitle("MyPass")
        self.setObjectName("MyPass")
        self.setFixedSize(400, 200)
        self.setStyleSheet("background-color: white;")
        self.main_layout = QVBoxLayout()
        self.setLayout(self.main_layout)

        header_label = QLabel("MyPass")
        header_label.setObjectName("header_label")
        header_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.main_layout.addWidget(header_label)

        self.setLayout(self.main_layout)

    # def check_fonts_availability(self):
    #     font_db = QFontDatabase()
    #     available_fonts = font_db.families()
    #     self.font_name = next(
    #         (font for font in self.FONT_NAMES if font in available_fonts), "Arial"
    #     )


def main():
    app = QApplication([])
    window = MyPass()
    window.show()
    app.exec()


if __name__ == "__main__":
    main()
