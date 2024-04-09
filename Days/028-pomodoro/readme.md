# Pomodoro Timer Application - Technical Documentation

This document provides a technical overview of the Pomodoro Timer application developed in Python using the PyQt5 framework. The application implements the Pomodoro Technique for time management, dividing work into fixed intervals (25 minutes by default) separated by shorter breaks.

## Application Structure

The application is structured around a main Python script (`main.py`) that utilizes the PyQt5 library to create a graphical user interface (GUI) for the timer. Key components of the application include:

- **Timer Mechanism:** Utilizes `QTimer` from PyQt5 to manage countdown functionality. The timer supports starting, stopping, and resetting operations.
- **Font Management:** Dynamically selects an available font from a predefined list of preferred fonts using `QFontDatabase`.
- **UI Components:** The GUI is built using PyQt5's `QWidget`, `QLabel`, `QPushButton`, and layout classes (`QHBoxLayout`, `QVBoxLayout`).

## Key Variables and Constants

- `FONT_NAMES`: A list of preferred font names.
- `WORK_MIN`, `SHORT_BREAK_MIN`, `LONG_BREAK_MIN`: Constants defining the duration (in minutes) of work sessions and breaks.
- `countdown_on`, `timer_seconds`, `timer_label`, `countdown_timer`, `start_button`: Global variables managing the state of the timer and UI elements.

## Functions

- `check_fonts_availability()`: Checks and selects the first available font from the `FONT_NAMES` list.
- `reset_timer()`: Resets the timer to its initial state.
- `start_timer()`: Toggles the timer between its active and inactive states, updating the UI accordingly.
- `update_timer()`: Called every second when the timer is active; updates the remaining time display and stops the timer when it reaches zero.

## Running the Application

To run the application, ensure you have Python and PyQt5 installed. Execute `main.py` from a terminal or command prompt. The application window will display a timer set to 25:00 by default, with a start/stop button to control the timer.

## Dependencies

- Python 3.x
- PyQt5

This technical documentation aims to provide developers and contributors with a clear understanding of the application's structure and functionality.

*Note: The app was originally intended to be written with tkinter but changed to QT since tkinter was too buggy on MacOS at the time.*
