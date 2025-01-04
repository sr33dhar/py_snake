# Snake Game 🐍

This is a modern take on the classic Snake game, implemented using **Python** and **Pygame**. The project serves as a sandbox for learning about object-oriented programming (OOP), game development, and exploring advanced techniques such as **automated gameplay** using machine learning (e.g., reinforcement learning) and non-ML approaches.

---

## Features
- **Classic Gameplay:** Navigate the snake, collect rewards, and avoid collisions.
- **Object-Oriented Design:** Clean and modular codebase using OOP principles.
- **Dynamic Grid Management:** The snake moves within a dynamically sized grid.
- **Responsive Controls:** Smooth handling for direction changes and pausing.
- **Score Tracking:**
  - Real-time display of the current and high scores.
  - Persistent high score storage in a local file.
- **Modular UI Components:**
  - Buttons for game options.
  - Dynamic UI rendering for game states like "Paused" and "Game Over."

---

## Purpose
This project was created as:
1. A **learning exercise** for mastering Python, Pygame, and OOP principles.
2. A **sandbox environment** for experimenting with automated gameplay:
   - **Reinforcement Learning (RL):** Train an AI agent to play the game efficiently.
   - **Non-ML Techniques:** Use rule-based systems or other heuristics for automation.

---

## Getting Started

### Prerequisites
- **Python 3.8+**
- **Pygame 2.0+**

### Installation
1. Clone the repository:
   ```bash
   git clone git@github.com:sr33dhar/py_snake.git
   cd py_snake
   ```

2. Install dependencies:
   ```bash
   pip install pygame
   ```

3. Run the game:
   ```bash
   python main.py
   ```

---

## How to Play
- **Arrow Keys (or W/A/S/D):** Control the direction of the snake.
- **Spacebar:** Pause or resume the game.
- **ESC:** Quit the game.

### Rules:
- Collect rewards to grow the snake and increase your score.
- Avoid collisions with the snake's body to keep playing.
- The snake wraps around the edges of the grid, allowing continuous play.

---

## File Structure
- **`main.py`**: Entry point and game loop.
- **`settings.py`**: Configurations for colors, screen size, and game settings.
- **`sprites.py`**: Core classes for Snake, Reward, and UI components.

---

## Future Goals
1. **Automated Gameplay:**
   - Train agents using reinforcement learning to optimize gameplay.
   - Implement heuristic-based strategies for snake movement.

2. **Advanced Features:**
   - Add multiple difficulty levels.
   - Implement obstacles and power-ups.
   - Introduce a multiplayer mode.

3. **AI Integration:**
   - Explore AI-driven gameplay using non-ML techniques.
   - Compare ML and non-ML approaches for solving the game.

---

## Contributing
This project is primarily for personal learning and experimentation, but contributions are welcome! Feel free to:
- Submit bug reports or suggestions via [Issues](https://github.com/sr33dhar/py_snake/issues).
- Create pull requests for enhancements or fixes.

---

## License
This project is licensed under the **MIT License**. See the [LICENSE](LICENSE) file for details.

---

## Acknowledgments
- Inspired by classic snake games and various tutorials on Python and Pygame.
- Special thanks to the Python and Pygame communities for their excellent resources and documentation.
