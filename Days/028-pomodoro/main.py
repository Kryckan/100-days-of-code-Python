import time

from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import (
    QApplication,
    QHBoxLayout,
    QLabel,
    QPushButton,
    QVBoxLayout,
    QWidget,
)

# Constants
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

# Global variables
countdown_on = False
timer_seconds = 0
timer_label = None
countdown_timer = None


# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    global countdown_on, timer_seconds
    countdown_on = False
    timer_seconds = 0
    if timer_label is not None:  # Ensure timer_label is initialized
        timer_label.setText("25:00")
    if countdown_timer is not None:  # Ensure countdown_timer is initialized
        countdown_timer.stop()


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global countdown_on, timer_seconds, countdown_timer
    countdown_on = True
    timer_seconds = WORK_MIN * 60 - 1
    countdown_timer = QTimer()
    countdown_timer.timeout.connect(update_timer)
    countdown_timer.start(1000)


def update_timer():
    global timer_seconds
    if countdown_on and timer_seconds > 0:
        mins, secs = divmod(timer_seconds, 60)
        time_format = "{:02d}:{:02d}".format(mins, secs)
        if timer_label is not None:
            timer_label.setText(time_format)
        timer_seconds -= 1
    else:
        if countdown_timer is not None:  # Check if countdown_timer is initialized
            countdown_timer.stop()


# ---------------------------- UI SETUP ------------------------------- #
def setup_ui(window):
    global timer_label
    window.setWindowTitle("Pomodoro")
    window.setFixedSize(300, 330)
    window.setObjectName("MainWindow")
    window.setStyleSheet(
        f"""
        #MainWindow {{
            background-image: url('Days/028-pomodoro/tomato.png');
            background-repeat: no-repeat;
            background-position: center;
            background-color: {YELLOW};
        }}
    """
    )

    main_layout = QVBoxLayout()
    main_layout.setContentsMargins(0, 0, 0, 0)
    main_layout.setSpacing(0)

    header_label = QLabel("Pomodoro Timer")
    header_label.setObjectName("header")
    header_label.setAlignment(Qt.AlignHCenter)
    header_label.setStyleSheet(
        f"""
        #header {{
            color: {GREEN}; font-size: 28px; font-family: {FONT_NAME}; font-weight: 700; padding-top: 15px;
        }}
    """
    )
    main_layout.addWidget(header_label)

    timer_label = QLabel("25:00")
    timer_label.setObjectName("timer")
    timer_label.setAlignment(Qt.AlignHCenter)
    timer_label.setStyleSheet(
        """
        #timer {
            color: #ffffff; font-size: 42px; font-family: 'Poppins';
        }
    """
    )
    main_layout.addWidget(timer_label)

    buttons_layout = QHBoxLayout()

    start_button = QPushButton("Start")
    start_button.setStyleSheet(
        """
        QPushButton {
            background-color: #9bdeac;
            background-image: none;
        }
        """
    )
    buttons_layout.addWidget(start_button)
    start_button.clicked.connect(start_timer)

    reset_button = QPushButton("Reset")
    reset_button.setStyleSheet(
        """
        QPushButton {
            background-color: #e2979c;
            background-image: none;
        }
        """
    )
    buttons_layout.addWidget(reset_button)
    reset_button.clicked.connect(reset_timer)

    main_layout.addLayout(buttons_layout)

    window.setLayout(main_layout)


# ---------------------------- MAIN ------------------------------- #
def main():
    app = QApplication([])
    window = QWidget()
    setup_ui(window)
    window.show()
    app.exec_()


if __name__ == "__main__":
    main()
