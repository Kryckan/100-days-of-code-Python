import json
import os
import random

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont, QFontDatabase
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


class MyPass(QWidget):
    FONT_NAMES = ["poppins", "Courier", "Arial", "Helvetica", "Times New Roman"]
    PASSWORD_CHARACTERS = (
        "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()_+"
    )

    def __init__(self):
        super().__init__()
        font_db = QFontDatabase()
        available_fonts = font_db.families()
        self.font_name = next(
            (font for font in self.FONT_NAMES if font in available_fonts), "Arial"
        )
        self.setFont(QFont(self.font_name, 12))
        self.current_dir = os.path.dirname(os.path.abspath(__file__))
        self.password_file = os.path.join(self.current_dir, "passwords.json")
        self.email_address = "yourmail@mail.com"
        self.setup_ui()

    def setup_ui(self):
        self.setWindowTitle("MyPass")
        self.setObjectName("MyPass")
        self.resize(500, 00)
        self.password_length = 15
        self.main_layout = QVBoxLayout()
        self.setLayout(self.main_layout)

        website_layout = QHBoxLayout()
        website_label = QLabel("Website:")
        website_layout.addWidget(website_label)

        self.website_name = QLineEdit(self)
        self.website_name.setObjectName("website_name")
        self.website_name.setPlaceholderText("Website")
        self.website_name.setAlignment(Qt.AlignmentFlag.AlignCenter)
        website_layout.addWidget(self.website_name)

        self.search_button = QPushButton("Search")
        self.search_button.setObjectName("search_button")
        self.search_button.setContentsMargins(10, 10, 10, 10)
        self.search_button.setCursor(Qt.CursorShape.PointingHandCursor)
        self.search_button.clicked.connect(self.search_password)
        website_layout.addWidget(self.search_button)

        self.main_layout.addLayout(website_layout)

        # Email input field
        email_layout = QHBoxLayout()
        email_label = QLabel("Email:")
        email_layout.addWidget(email_label)

        self.email_input = QLineEdit(self)
        self.email_input.setObjectName("email_input")
        self.email_input.setText(self.email_address)
        self.email_input.setAlignment(Qt.AlignmentFlag.AlignCenter)
        email_layout.addWidget(self.email_input)

        self.main_layout.addLayout(email_layout)

        # Password input field
        password_layout = QHBoxLayout()
        password_label = QLabel("Password:")
        password_layout.addWidget(password_label)

        self.password_input = QLineEdit(self)
        self.password_input.setObjectName("password_input")
        self.password_input.setAlignment(Qt.AlignmentFlag.AlignCenter)
        password_layout.addWidget(self.password_input)

        self.generate_password_button = QPushButton("Generate Password")
        self.generate_password_button.setObjectName("generate_password_button")
        self.generate_password_button.setContentsMargins(50, 10, 10, 10)
        self.generate_password_button.setCursor(Qt.CursorShape.PointingHandCursor)
        self.generate_password_button.clicked.connect(self.generate_password)
        password_layout.addWidget(self.generate_password_button)

        self.main_layout.addLayout(password_layout)

        # Save button
        self.save_button = QPushButton("Save")
        self.save_button.setObjectName("save_button")
        self.save_button.setContentsMargins(10, 10, 10, 10)
        self.save_button.setCursor(Qt.CursorShape.PointingHandCursor)
        self.save_button.clicked.connect(self.write_to_file)

        self.main_layout.addWidget(self.save_button)

    def generate_password(self) -> None:
        password: list[str] = []
        for i in range(self.password_length):
            password.append(random.choice(self.PASSWORD_CHARACTERS))
        clipboard = QApplication.clipboard()
        clipboard.setText("".join(password))
        self.password_input.setText("".join(password))

    def save_popup(self):
        msg_box = QMessageBox()
        msg_box.setWindowTitle("Save Password")
        msg_box.setText("Do you want to save the password to file?")
        msg_box.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        msg_box.setDefaultButton(QMessageBox.Yes)
        return msg_box.exec_()

    def write_to_file(self):
        # Check if all fields are filled
        if (
            not self.website_name.text()
            or not self.email_input.text()
            or not self.password_input.text()
        ):
            QMessageBox.critical(self, "Empty Fields", "All fields are required.")
            return

        # Prepare the data to be saved
        new_data = {
            self.website_name.text(): {
                "email": self.email_input.text(),
                "password": self.password_input.text(),
            }
        }

        # Confirm before saving
        if self.save_popup() != QMessageBox.Yes:
            return

        try:
            old_data = {}
            # Attempt to read existing data
            try:
                with open(self.password_file, "r") as data_file:
                    old_data = json.load(data_file)
            except (FileNotFoundError, json.JSONDecodeError):
                # If the file doesn't exist or is empty/corrupt, start with an empty dict
                pass

            # Merge new data with old data
            old_data.update(new_data)

            # Write the merged data back to the file
            with open(self.password_file, "w") as data_file:
                json.dump(old_data, data_file, indent=4)

            QMessageBox.information(self, "Success", "Password saved successfully.")
            self.website_name.clear()
            self.password_input.clear()

        except Exception as e:
            QMessageBox.critical(self, "Error", f"An error occurred: {e}")

    def search_password(self):
        with open(self.password_file, "r") as data_file:
            data = json.load(data_file)
            website_name = self.website_name.text()
            if website_name in data:
                website = data[website_name]
                email = website["email"]
                password = website["password"]
                QMessageBox.information(
                    self,
                    "Password Information",
                    f"Website: {website_name}\nEmail: {email}\nPassword: {password}",
                )
            else:
                QMessageBox.warning(
                    self, "Password", "No password found for the given website name."
                )


def main():
    app = QApplication([])
    window = MyPass()
    window.show()
    app.exec()


if __name__ == "__main__":
    main()
