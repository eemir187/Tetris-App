# 🎮 Tetris 

A classic Tetris game 

## 🚀 Overview

This project is a fully functional Tetris game built in **Python** using **Pygame**.  
It was **developed on top of a custom provided framework (`framework.py`)**  which handles rendering, game board setup, and other foundational elements. All gameplay logic has been implemented in `tetris.py`.

## 🛠️ Framework Usage

The base game infrastructure—such as drawing the board, handling the game window, and rendering blocks—comes from the provided `BaseGame` class in `framework.py`. The gameplay logic and game mechanics is developed inside `tetris.py`.

## 🕹️ Controls

| Key(s)         | Action                        |
|----------------|-------------------------------|
| A / Left Arrow | Move block left               |
| D / Right Arrow| Move block right              |
| S / Down Arrow | Move block down faster        |
| Q              | Rotate block counter-clockwise|
| E              | Rotate block clockwise        |
| P              | Pause the game                |
| ESC            | Quit the game                 |

## 📦 Features

- Real-time block movement and rotation
- Blocks lock in place when they can no longer move
- Line clearing and scoring system
- Dynamic level and speed increases
- Preview of the next block
- 7 classic Tetris block types with full rotation support

## 🧱 Block Types

- **smashBoy** (Square)
- **hero** (Line)
- **teewee** (T-Block)
- **clevelandZ**, **rhodeIslandZ** (Z-Shapes)
- **blueRicky**, **orangeRicky** (L-Shapes)

## 📥 How to Run

1. Switch in the command-line/terminal to your project’s root folder … `\Tetris-App`
2. Create a virtual environment (venv). Use the command:  
   ```bash
   python3 -m venv .venv
3. Activate the `venv` by running:  
- **Linux/MacOS**:  
  ```
  source .venv/bin/activate
  ```
- **Windows**:  
  ```
  .\.venv\Scripts\activate
  ```
4. Run the following command to install the required library:  


  
