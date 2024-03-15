# Snake Game

This project is a Python implementation of the classic Snake game.

## Description

This version of the Snake game includes the main functionalities of the original game. The player controls a snake, which moves around the screen. The objective is to eat food that randomly appears, which causes the snake to grow. The game ends if the snake collides with itself or with the boundaries of the screen.

## Files

This project consists of the following Python files:

- `main.py`: The main entry point of the program. This is where the game loop is defined and all the other components are put together.
- `snake.py`: Defines the Snake object and its behavior. This includes how it moves, grows, and interacts with the environment.
- `score.py`: Handles the scoring system of the game. This includes increasing the score when the snake eats food and potentially saving and displaying high scores.
- `food.py`: Defines the Food object and its placement within the game area.

## Usage

To start the game, run the following command in your terminal:

```bash
python main.py
