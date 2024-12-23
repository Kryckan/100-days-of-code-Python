from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont, QFontDatabase, QPixmap
from PyQt5.QtWidgets import (
    QApplication,
    QHBoxLayout,
    QLabel,
    QLineEdit,
    QMessageBox,
    QPushButton,
    QVBoxLayout,
    QWidget,
)
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:
    def __init__(self, quiz: QuizBrain):
        self.quiz = quiz
        self.app = QApplication([])
        self.window = QWidget()
        self.window.setWindowTitle("Quiz Game")
        self.window.setStyleSheet(f"background-color: {THEME_COLOR};")
        self.main_layout = QVBoxLayout()
        self.window.setLayout(self.main_layout)

        # Score Layout
        self.score_label = QLabel("Score: 0")
        self.score_label.setStyleSheet("font-size: 20px; color: white;")
        self.window.layout().addWidget(self.score_label)

        # Question Layout
        self.question_label = QLabel("Welcome to the Quiz Game!")
        self.question_label.setObjectName("question_label")
        self.question_label.setAlignment(Qt.AlignCenter)
        self.question_label.setWordWrap(True)
        self.question_label.setMinimumSize(300, 250)
        self.question_label.setStyleSheet(
            "font-size: 20px; color: black; background-color: #ffffff;"
        )
        self.window.layout().addWidget(self.question_label)

        # Buttons
        self.button_layout = QHBoxLayout()
        self.button_layout.setObjectName("button_layout")

        self.false_button = QPushButton("False")
        self.false_button.setObjectName("false_button")
        self.false_button.setStyleSheet(
            "font-size: 20px; color: black; background-color: #aa0000;"
        )
        self.button_layout.addWidget(self.false_button)

        self.true_button = QPushButton("True")
        self.true_button.setObjectName("true_button")
        self.true_button.setStyleSheet(
            "font-size: 20px; color: black; background-color: #00aa00;"
        )
        self.button_layout.addWidget(self.true_button)

        self.main_layout.addLayout(self.button_layout)

        self.get_next_question()

        # Start app
        self.window.show()
        self.app.exec_()

    def get_next_question(self) -> None:
        q_text = self.quiz.next_question()
        if q_text is None:
            self.question_label.setText("You've completed the quiz!")
            return
        self.question_label.setText(q_text)
