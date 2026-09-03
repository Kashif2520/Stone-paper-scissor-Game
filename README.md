# 🐍 Rock, Paper, Scissors Game 🎮

A simple **Rock, Paper, Scissors game** built using Python.  
This project uses a **2D Matrix** to determine the result of the game based on the user's and computer's choices.

## 🎯 Features

- 🎮 Choose between Rock, Paper, and Scissors
- 🤖 Computer makes a random choice
- 🧮 Uses a 2D Matrix for result calculation
- 🏆 Displays Win, Lose, or Draw
- 🚪 Includes an Exit option
- 🔄 Game continues until the user exits

## 🧠 Concepts Used

- Python Functions
- 2D Lists / Matrix
- List Indexing
- `random` Module
- `while` Loop
- `if` Conditions
- User Input
- Basic Game Logic

## 🎮 Game Options

```text
0. Rock
1. Paper
2. Scissor
3. Exit
````

## 🧮 Matrix Logic

The game result is stored in a 2D matrix:

```python
matrix = [
    ["Draw", "you Lose", "You won"],
    ["You Won", "Draw", "you lose"],
    ["you lose", "You won", "Draw"]
]
```

The user's choice is used as the **row index**, while the computer's choice is used as the **column index**.

```python
result = matrix[user][comp]
```

## ▶️ How to Run

Make sure Python is installed, then run:

```bash
python main.py
```

Select a number from `0` to `3` and play the game.

## 📚 What I Learned

Through this project, I practiced using **2D lists, indexing, random selection, loops, functions, and conditional statements**.

The main idea I learned was how a **matrix can be used to simplify game-result logic**.

### 👨‍💻 Author

**Sayyed Kashif**
CSE (AI/ML) Student | Python Learner

## 🔗 Connect With Me

- 💼 LinkedIn: www.linkedin.com/in/kashif-sayyed-a983a9431

```
```