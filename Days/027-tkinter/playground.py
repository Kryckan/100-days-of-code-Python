from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
    QApplication,
    QLabel,
    QLineEdit,
    QPushButton,
    QSizePolicy,
    QSpacerItem,
    QVBoxLayout,
    QWidget,
)


def miles_to_kilometers(miles):
    try:
        return round(float(miles) * 1.60934, 2)
    except ValueError:
        return "Invalid input"


def app():
    app = QApplication([])
    window = QWidget()
    window.setWindowTitle("Miles to Kilometers Converter")
    layout = QVBoxLayout()

    label = QLabel("How many miles?")
    layout.addWidget(label, alignment=Qt.AlignLeft)
    layout.addSpacerItem(QSpacerItem(0, 0, QSizePolicy.Minimum, QSizePolicy.Expanding))

    entry = QLineEdit()
    entry.setPlaceholderText("Enter miles...")
    layout.addWidget(entry)
    layout.addSpacerItem(
        QSpacerItem(10, 10, QSizePolicy.Minimum, QSizePolicy.Expanding)
    )

    converted_label = QLabel("0" + " km")
    layout.addWidget(converted_label)

    button = QPushButton("Convert")
    button.clicked.connect(
        lambda: converted_label.setText(str(miles_to_kilometers(entry.text())) + " km")
    )
    layout.addWidget(button)
    layout.addSpacerItem(
        QSpacerItem(10, 10, QSizePolicy.Minimum, QSizePolicy.Expanding)
    )

    window.setLayout(layout)
    window.show()
    app.exec_()


if __name__ == "__main__":
    app()
