from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QLabel, QPushButton, QVBoxLayout, QWidget

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

# ---------------------------- TIMER RESET ------------------------------- #


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    print("Start")


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #


# ---------------------------- UI SETUP ------------------------------- #
def app():
    app = QApplication([])
    window = QWidget()
    window.setWindowTitle("Pomodoro")
    window.setFixedSize(400, 400)
    window.setObjectName("MainWindow")
    window.setStyleSheet(
        """
        #MainWindow {
            background-image: url('Days/028-pomodoro/tomato.png');
            background-repeat: no-repeat;
            background-position: center;
            background-color: #f7f5dd;
        }
    """
    )

    layout = QVBoxLayout()

    timer = QLabel("00:00")
    timer.setObjectName("timer")
    timer.setAlignment(Qt.AlignCenter)
    timer.setStyleSheet(
        """
        #timer {
            color: #aaaa; font-size: 42px; font-family: 'Roboto';
        }
    """
    )
    layout.addWidget(timer)

    start_button = QPushButton("Start")
    start_button.setStyleSheet(
        """
    QPushButton {
        background-color: #9bdeac;
        background-image: none;
    }
"""
    )
    layout.addWidget(start_button)
    start_button.clicked.connect(start_timer)

    window.setLayout(layout)
    window.show()
    app.exec_()


if __name__ == "__main__":
    app()
