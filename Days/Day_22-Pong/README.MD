# Day 22 - Pong

Pong is a classic arcade game where two players control paddles to hit a ball back and forth. This project aims to create a simple Pong game using Python.

## Features

- **Screen Creation**: Set up a game window with appropriate dimensions and background.
- **Paddles**: Create and control two paddles that players can move up and down.
- **Ball**: Create a ball that moves across the screen, bouncing off paddles and walls.
- **Collisions**: Detect collisions with paddles and walls to accurately reflect the ball's movement.
- **Miss Detection**: Detect when a paddle misses the ball, awarding a point to the other player.
- **Score Board**: Keep track of and display the scores for both players.

## Files

- `main.py`: The main entry point for the game, controlling the game loop and overall flow.
- `paddle.py`: Contains code related to the paddle objects, including their creation, movement, and rendering.
- `ball.py`: Contains code related to the ball object, including its creation, movement, and rendering.

## Usage

To play the game, run the following command:

\```bash
python main.py
\```

Ensure that you have the required dependencies installed, which can be found within the Python files.

## Todo

- [x] Create the screen
- [x] Create and move two paddles
- [x] Create the ball and make it move
- [x] Detect collisions with paddles and walls
- [x] Detect paddle miss
- [ ] Score Board

## Contributing

If you'd like to contribute to this project, please feel free to fork the repository and submit a pull request, or open an issue with your suggestions or bug reports.

## License

This project is open-source and available under the MIT License. See the LICENSE file for more details.
