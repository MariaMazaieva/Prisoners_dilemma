#  Prisoner's Dilemma Simulation in Python

This project simulates the **Prisoner's Dilemma**, a fundamental problem in game theory. It pits different strategies against one another over multiple rounds to compare outcomes based on a configurable payoff matrix.

##  Project Structure

```
.
├── game.py              # Handling game logic
├── test_game.py         # Simulate a game between two players
├── player_dilema.py     # Adaptive player, able to detect opponents's strategy
├── Cooperate_player.py  # Always cooperates 
├── Defect_player.py     # Always defects
├── Random_player.py     # Random choice
```

##  Strategies Implemented

- **Cooperate Player**: Always cooperates (`COOPERATE = False`)
- **Defect Player**: Always defects (`DEFECT = True`)
- **Random Player**: Makes random choices each round
- **Adaptive Player** (`player_dilema.py`):
  - Can detect:
    - Copycat players (Tit-for-Tat)
    - Always-cooperate opponents
    - Always-defect opponents
  - Defects on the final round for advantage
  - Uses random moves otherwise

##  How It Works

- Necessary to write main code in `game.py`.
- Both Players have those methods:
  - `select_move()`: Decides the next move.
  - `record_last_moves(my_move, opponent_move)`: Stores round history.
- The game runs for a fixed number of rounds (default 20).
- All analyses works from given matrix (if there was no noise = no matrix given):
  ```python
  payoff_matrix = (
      ((4,4), (1,6)),
      ((6,1), (2,2))
  )
  ```

##  How to Run

1. Make sure all `.py` files are in the same directory.
2. Run the test game:
   ```bash
   python test_game.py
   ```
   
##  Example Output

```
playerA got: 47 
playerB got: 36
```
