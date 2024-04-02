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

PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
countdown_on = False
timer_seconds = 0  # Added global variable to keep track of the time in seconds
global timer_label, countdown_timer  # Declare timer and countdown_timer as global variables


# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    countdown_on = False
    timer_seconds = 0
    timer_label.setText("25:00")
    countdown_timer.stop()  # Stop the timer when resetting


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global countdown_on, timer_seconds, countdown_timer  # Include countdown_timer in the global declaration
    countdown_on = True
    timer_seconds = WORK_MIN * 60 - 1
    countdown_timer = QTimer()
    countdown_timer.timeout.connect(update_timer)
    countdown_timer.start(1000)  # Timer updates every 1000 milliseconds (1 second)


def update_timer():
    global timer_seconds, timer_label, countdown_timer  # Include countdown_timer in the global declaration
    if countdown_on and timer_seconds > 0:
        mins, secs = divmod(timer_seconds, 60)
        time_format = "{:02d}:{:02d}".format(mins, secs)
        timer_label.setText(time_format)
        timer_seconds -= 1
    else:
        countdown_timer.stop()  # Stop the timer when countdown is finished or not active


# ---------------------------- UI SETUP ------------------------------- #
def app():
    global timer_label  # Declare timer as global within the function scope
    app = QApplication([])
    window = QWidget()
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

    # Create a horizontal layout for the buttons
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

    # Add another button if needed, for example, a stop button
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
    # stop_button.clicked.connect(stop_timer)  # Assuming you have or will create a stop_timer function

    # Add the buttons layout to the main layout
    main_layout.addLayout(buttons_layout)

    window.setLayout(main_layout)
    window.show()
    app.exec_()


if __name__ == "__main__":
    app()
