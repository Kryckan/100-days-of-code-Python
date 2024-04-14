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


class PomodoroApp(QWidget):
    PINK = "#e2979c"
    RED = "#e7305b"
    GREEN = "rgba(100, 200, 140, 1)"
    YELLOW = "#f7f5dd"
    FONT_NAMES = ["poppins", "Courier", "Arial", "Helvetica", "Times New Roman"]
    WORK_MIN = 1
    SHORT_BREAK_MIN = 5
    LONG_BREAK_MIN = 20
    SESSIONS_BEFORE_LONG_BREAK = 4

    def __init__(self):
        super().__init__()
        self.countdown_on = False
        self.timer_seconds = 0
        self.session_count = 0
        self.check_fonts_availability()
        self.setup_ui()
        self.current_dir = os.path.dirname(os.path.abspath(__file__))
        self.big_tomato_image = os.path.join(self.current_dir, "tomato.png")
        self.small_tomato_icon = os.path.join(self.current_dir, "small_tomato_icon.png")
        self.countdown_timer = QTimer()
        self.countdown_timer.timeout.connect(self.update_timer)

    def check_fonts_availability(self):
        font_db = QFontDatabase()
        available_fonts = font_db.families()
        self.font_name = next(
            (font for font in self.FONT_NAMES if font in available_fonts), "Arial"
        )

    def reset_timer(self):
        self.countdown_on = False
        self.timer_seconds = 0
        self.timer_label.setText("25:00")
        self.countdown_timer.stop()
        self.start_button.setText("Start")
        self.session_count = 0

    def start_timer(self):
        if self.countdown_on:
            self.reset_timer()
        else:
            self.countdown_on = True
            if self.session_count == self.SESSIONS_BEFORE_LONG_BREAK:
                self.timer_seconds = self.LONG_BREAK_MIN * 60 - 1
                self.session_count = 0  # Reset session count after long break
            elif self.session_count % 2 == 0:
                self.timer_seconds = self.WORK_MIN * 60 - 1
            else:
                self.timer_seconds = self.SHORT_BREAK_MIN * 60 - 1
            self.start_button.setText("Stop")
            self.countdown_timer.start(1000)

    def update_timer(self):
        if self.countdown_on and self.timer_seconds > 0:
            mins, secs = divmod(self.timer_seconds, 60)
            self.timer_label.setText(f"{mins:02d}:{secs:02d}")
            self.timer_seconds -= 1
        elif self.countdown_on and self.timer_seconds == 0:
            self.session_count += 1
            self.reset_timer()
            self.update_tomato_icons()

    def update_tomato_icons(self):
        for i in reversed(range(self.tomatoes_layout.count())):
            widget = self.tomatoes_layout.itemAt(i).widget()
            if (
                widget is not None
            ):  # Ensure the widget is not None before calling deleteLater
                widget.deleteLater()  # Properly delete the widget
        for _ in range(self.session_count):
            label = QLabel()
            pixmap = QPixmap(self.small_tomato_icon)
            if pixmap.isNull():
                print(f"Failed to load image at {self.small_tomato_icon}")
            else:
                label.setPixmap(pixmap.scaled(32, 32))
            self.tomatoes_layout.addWidget(label)

    def setup_ui(self):
        self.setWindowTitle("Pomodoro")
        self.setFixedSize(300, 330)
        self.setObjectName("MainWindow")
        self.setStyleSheet(f"#MainWindow {{background-color: {self.YELLOW};}}")

        main_layout = QVBoxLayout()
        main_layout.setContentsMargins(0, 0, 0, 0)
        main_layout.setSpacing(0)

        header_label = QLabel("Pomodoro Timer")
        header_label.setAlignment(Qt.AlignHCenter)
        header_label.setStyleSheet(
            f"color: {self.GREEN}; font-size: 28px; font-family: {self.font_name}; font-weight: 700; padding-top: 15px;"
        )
        main_layout.addWidget(header_label)

        self.timer_label = QLabel("25:00")
        self.timer_label.setAlignment(Qt.AlignHCenter)
        self.timer_label.setStyleSheet(
            "color: #222222; font-size: 42px; font-family: 'Poppins';"
        )
        main_layout.addWidget(self.timer_label)

        self.tomatoes_layout = QHBoxLayout()
        self.tomatoes_layout.setAlignment(Qt.AlignCenter)
        main_layout.addLayout(self.tomatoes_layout)

        buttons_layout = QHBoxLayout()
        self.start_button = QPushButton("Start")
        self.start_button.setStyleSheet(
            """
QPushButton {
background-color: #9bdeac;
margin: 10px;
padding: 5px;
border-radius: 3px;
}
QPushButton:hover {
background-color: #a6e4b9;
}
QPushButton:pressed {
background-color: #89c99e;
}
"""
        )
        buttons_layout.addWidget(self.start_button)
        self.start_button.clicked.connect(self.start_timer)

        reset_button = QPushButton("Reset")
        reset_button.setStyleSheet(
            """
QPushButton {
background-color: #e2979c;
margin: 10px;
padding: 5px;
border-radius: 3px;
}
QPushButton:hover {
background-color: #e7a6b3;
}
QPushButton:pressed {
background-color: #cb8290;
}
"""
        )
        buttons_layout.addWidget(reset_button)
        reset_button.clicked.connect(self.reset_timer)

        main_layout.addLayout(buttons_layout)
        self.setLayout(main_layout)


def main():
    app = QApplication([])
    window = PomodoroApp()
    window.show()
    app.exec_()


if __name__ == "__main__":
    main()
