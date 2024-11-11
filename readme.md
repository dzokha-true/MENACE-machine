# README for Menace AI Tic-Tac-Toe Implementation

## Overview

This project is an implementation of a simplified version of the **MENACE (Machine Educable Noughts and Crosses Engine)**, a machine learning system that learns to play Tic-Tac-Toe using matchboxes and beads. The program features a basic AI that competes against a human player, making use of the MENACE approach, where each matchbox (game state) contains beads representing different move choices.

MENACE learns by adjusting the beads in the matchboxes based on game outcomes. This project simulates that process, allowing the AI to become better at the game over multiple rounds.

## Features

- Human vs MENACE AI Tic-Tac-Toe game.
- The AI uses a learning mechanism to improve its choices based on previous game results.
- The AI adjusts its strategy after each game, increasing the chance of repeating winning moves and decreasing the chance of repeating losing moves.

## Prerequisites

The script only requires Python (version 3.6 or higher) and does not depend on any external libraries apart from the built-in `random` and `copy` modules.

## How It Works

1. **Matchbox Class**: Represents a game state, holding the current board configuration, beads, parent nodes (previous game states), and child nodes (possible next game states).
2. **Beads**: Represent the probability of choosing a particular move. More beads mean a higher chance of selecting that move.
3. **Game Logic**:
   - The AI places an 'X' for its move, while the player places an 'O'.
   - The AI evaluates the board using the beads and randomly selects a move based on their counts.
   - The AI adjusts the bead count based on the game outcome (winning, losing, or drawing).

## Code Structure

- **`Matchbox` Class**: Contains the core logic of the game, including:
  - `__init__()`: Initializes a matchbox object with the current grid, parent and child nodes, number of beads, and turn information.
  - `next_step()`: Checks if the game is finished, and if not, creates child nodes and places beads.
  - `checking_win()`: Evaluates the current board state to check for winning combinations.
  - `placing_beads()`: Places beads in the empty cells of the grid.
  - `creating_child()`: Generates child nodes (possible next moves) from the current board state.
  - `user_go()`: Handles the player's input for their move.
  - `game()`: Main game loop, where MENACE AI and the player take turns until the game is won or drawn.

## How to Run

1. Save the code in a file named `menace_tictactoe.py`.
2. Run the script using:
   ```bash
   python menace_tictactoe.py
   ```
3. Input the number of games you want to play against the AI when prompted:
   ```
   please input the number of times you want to play a game: [number]
   ```

4. Follow the instructions to play by entering your moves in `(row,column)` format.

## Example

```
please input the number of times you want to play a game: 3
 [8, 8, 8] 
 [8, 8, 8] 
 [8, 8, 8]
Put your move in (row,column) format, with no space: 0,0
Player has won
 [8, 8, 'o']
 [8, 'x', 'o']
 ['x', 'x', 'o']
```

In the example above:
- The player won the game by placing 'O' in the correct positions.

## Game Flow

- The game begins with the AI's turn if `WHOSE_TURN_IS_IT` is set to 1.
- The player inputs their move using `(row,column)` format.
- The AI chooses its move based on the beads in the current matchbox.
- The game continues until a player wins or all cells are filled (draw).

## Learning Mechanism

- If MENACE wins, it reinforces its moves by **increasing the bead count** for the chosen moves.
- If MENACE loses, it **decreases the bead count**, reducing the chance of repeating those moves.
- This simple form of reinforcement learning helps MENACE improve over time as it adapts based on game outcomes.

## Limitations

- The AI does not remember games across different runs since it does not save the matchbox states.
- The use of `eval()` in `user_go()` might pose a security risk if user input is not controlled, but it is acceptable for local use.
- The code is designed for a single player against MENACE; it does not support two AI players or multiplayer games.

## Future Improvements

- Implement persistent storage for the matchboxes to allow MENACE to learn across different sessions.
- Enhance the AI's decision-making process by implementing more complex learning algorithms.
- Add a graphical user interface (GUI) for better user interaction.
- Improve the code's efficiency by optimizing the checking of win conditions.

## References

- [MENACE (Machine Educable Noughts and Crosses Engine) - Wikipedia](https://en.wikipedia.org/wiki/MENACE)

## Author

This project is a simplified and educational implementation of the MENACE concept to demonstrate reinforcement learning in a basic Tic-Tac-Toe game.