# snake-game
This Snake Game is a classic arcade game where you control a snake to eat food and grow longer without running into the walls or yourself. The game features a graphical user interface created using the Turtle graphics library.

---

# Snake Game - Python

A simple Snake Game implemented in Python using the Turtle graphics library.

## Table of Contents

- [Introduction](#introduction)
- [Installation](#installation)
- [How to Play](#how-to-play)
- [Game Controls](#game-controls)
- [Game Rules](#game-rules)
- [Scoring](#scoring)
- [Files](#files)
- [Contributing](#contributing)
- [License](#license)

## Introduction

This Snake Game is a classic arcade game where you control a snake to eat food and grow longer without running into the walls or yourself. The game features a graphical user interface created using the Turtle graphics library.

## Installation

1. Clone the repository to your local machine:

   ```bash
   git clone https://github.com/akhila-kudrethaya/snake-game.git
   ```

2. Change into the game directory:

   ```bash
   cd snake-game
   ```

3. Run the game:

   ```bash
   python main.py
   ```

## How to Play

- The game starts with a snake of length 1 and a piece of food on the screen.
- Use the arrow keys to control the snake's direction: Up, Down, Left, and Right.
- Your goal is to eat the food to grow the snake while avoiding collisions with the wall and yourself.
- The game ends when the snake collides with the wall or itself.

## Game Controls

- **Up Arrow**: Move the snake up.
- **Down Arrow**: Move the snake down.
- **Left Arrow**: Move the snake left.
- **Right Arrow**: Move the snake right.

## Game Rules

- The snake cannot move in the opposite direction of its current movement (e.g., if it's moving up, it cannot immediately turn down).
- The game ends if the snake collides with the wall or itself.

## Scoring

- Each time the snake eats food, the player's score increases.
- The game keeps track of the highest score achieved during the session, which is stored in the `high_score.txt` file.

## Files

- `main.py`: The main Python script that runs the Snake Game.
- `high_score.txt`: A text file that stores the highest score achieved in the game.
- `snake.py`: Python script containing the Snake class.
- `food.py`: Python script containing the Food class.
- `scoreboard.py`: Python script containing the ScoreBoard class.

## Contributing

Contributions to this Snake Game project are welcome. If you have any ideas for improvements or bug fixes, please open an issue or create a pull request.

## License

This Snake Game project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

