# 🧮 Smart Calculator

A Python-based GUI calculator built using **Tkinter**.

This project started as a basic command-line calculator and was developed into a graphical calculator that can evaluate mathematical expressions while following normal operator precedence.

## ✨ Features

* ➕ Addition
* ➖ Subtraction
* ✖️ Multiplication
* ➗ Division
* `%` Remainder operation
* 🔢 Decimal numbers
* 🧮 Mathematical expressions
* `()` Parentheses
* 📐 Operator precedence
* 🚫 Division-by-zero error handling
* ⚠️ Invalid-expression handling
* ⌫ Backspace
* 🗑️ Clear button
* ⌨️ Keyboard input
* 🖥️ Graphical User Interface (GUI)

## 🛠️ Technologies Used

* **Python 3**
* **Tkinter**
* Python functions
* Lists
* Loops
* Conditional statements
* String processing
* Basic expression parsing

## 📂 Project Structure

```text
Smart-Calculator/
│
├── GUI_Smart_calcultor.py
└── README.md
```

## ▶️ How to Run

### 1. Install Python

Download Python from the official Python website if it is not already installed.

### 2. Clone the repository

```bash
git clone https://github.com/Cyber-Chaithanya/Smart-Calculator.git
```

### 3. Open the project

```bash
cd Smart-Calculator
```

### 4. Run the calculator

```bash
python GUI_Smart_calcultor.py
```

The calculator window will open.

## 🧠 How It Works

The calculator does not rely on unrestricted Python `eval()` to calculate expressions.

Instead, the program:

1. Reads the mathematical expression.
2. Breaks the expression into numbers and operators.
3. Handles parentheses.
4. Performs multiplication, division, and remainder operations first.
5. Performs addition and subtraction.
6. Displays the final result in the GUI.

This helped me understand how a simple expression parser works.

## 🧪 Example

Input:

```text
30 + 10 * 18 + 10 % 20 * 99
```

Output:

```text
1200
```

Another example:

```text
(10 + 20) * 3
```

Output:

```text
90
```

## 🎯 What I Learned

Through this project, I practiced:

* Python functions
* Variables and data types
* Loops
* Conditional statements
* String handling
* Lists
* Exception handling
* Expression parsing
* Tkinter GUI development
* Git and GitHub
* Testing and debugging

## 🚀 Future Improvements

Planned upgrades include:

* Scientific calculator functions
* Trigonometric functions such as `sin`, `cos`, and `tan`
* Square root and power functions
* `π` and `e`
* Degree/Radian mode
* Calculation history
* Improved scientific-calculator interface

## 👨‍💻 Author

**Naga Chaithanya**

CSE Diploma Student
Aspiring Cybersecurity Professional

GitHub: [Cyber-Chaithanya](https://github.com/Cyber-Chaithanya)

---

⭐ This project is part of my journey of learning Python, software development, and cybersecurity.
