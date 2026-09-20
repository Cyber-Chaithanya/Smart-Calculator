
import tkinter as tk


def tokenize(expression):
    tokens = []
    number = ""

    for character in expression:
        if character.isdigit() or character == ".":
            number += character

        elif character in "+-*/%()":
            if number:
                tokens.append(float(number))
                number = ""

            tokens.append(character)

        elif character.isspace():
            continue

        else:
            raise ValueError("Invalid character")

    if number:
        tokens.append(float(number))

    return tokens


def calculate(tokens):

    if not tokens:
        raise ValueError("Empty expression")

    # Handle parentheses first
    while "(" in tokens:

        if ")" not in tokens:
            raise ValueError("Mismatched parentheses")

        close = tokens.index(")")
        open_index = close - 1

        while open_index >= 0 and tokens[open_index] != "(":
            open_index -= 1

        if open_index < 0:
            raise ValueError("Mismatched parentheses")

        result = calculate(tokens[open_index + 1:close])

        tokens[open_index:close + 1] = [result]

    if ")" in tokens:
        raise ValueError("Mismatched parentheses")

    # Multiplication, division and remainder
    i = 0

    while i < len(tokens):

        if tokens[i] in ("*", "/", "%"):

            left = tokens[i - 1]
            operator = tokens[i]
            right = tokens[i + 1]

            if operator == "*":
                result = left * right

            elif operator == "/":
                if right == 0:
                    raise ZeroDivisionError("Cannot divide by zero")

                result = left / right

            elif operator == "%":
                if right == 0:
                    raise ZeroDivisionError("Cannot use zero with %")

                result = left % right

            tokens[i - 1:i + 2] = [result]
            i -= 1

        else:
            i += 1

    # Addition and subtraction
    if len(tokens) == 1:
        return tokens[0]

    result = tokens[0]
    i = 1

    while i < len(tokens):

        operator = tokens[i]
        number = tokens[i + 1]

        if operator == "+":
            result += number

        elif operator == "-":
            result -= number

        else:
            raise ValueError("Invalid expression")

        i += 2

    return result


def calculate_expression():
    expression = display.get()

    try:
        tokens = tokenize(expression)
        result = calculate(tokens)

        if result.is_integer():
            result = int(result)

        display.delete(0, tk.END)
        display.insert(0, str(result))

    except ZeroDivisionError as error:
        display.delete(0, tk.END)
        display.insert(0, str(error))

    except (ValueError, IndexError):
        display.delete(0, tk.END)
        display.insert(0, "Invalid expression")


def add_to_display(value):
    display.insert(tk.END, value)


def clear_display():
    display.delete(0, tk.END)


def backspace():
    current = display.get()
    display.delete(0, tk.END)
    display.insert(0, current[:-1])


def keyboard_input(event):
    allowed = "0123456789.+-*/%()"

    if event.char in allowed:
        return

    if event.keysym == "Return":
        calculate_expression()
        return "break"

    if event.keysym == "BackSpace":
        backspace()
        return "break"

    if event.keysym == "Escape":
        clear_display()
        return "break"

    return "break"


window = tk.Tk()

window.title("Smart Calculator")
window.geometry("400x600")
window.resizable(False, False)

display = tk.Entry(
    window,
    font=("Arial", 28),
    justify="right",
    bd=10
)

display.pack(
    padx=15,
    pady=20,
    fill="x"
)

button_frame = tk.Frame(window)
button_frame.pack(padx=10, pady=10)

buttons = [
    ("7", 0, 0),
    ("8", 0, 1),
    ("9", 0, 2),
    ("/", 0, 3),

    ("4", 1, 0),
    ("5", 1, 1),
    ("6", 1, 2),
    ("*", 1, 3),

    ("1", 2, 0),
    ("2", 2, 1),
    ("3", 2, 2),
    ("-", 2, 3),

    ("0", 3, 0),
    (".", 3, 1),
    ("%", 3, 2),
    ("+", 3, 3),

    ("(", 4, 0),
    (")", 4, 1),
    ("C", 4, 2),
    ("⌫", 4, 3),
]

for text, row, column in buttons:

    if text == "C":
        command = clear_display

    elif text == "⌫":
        command = backspace

    else:
        command = lambda value=text: add_to_display(value)

    button = tk.Button(
        button_frame,
        text=text,
        font=("Arial", 18),
        width=5,
        height=2,
        command=command
    )

    button.grid(
        row=row,
        column=column,
        padx=4,
        pady=4
    )


equal_button = tk.Button(
    window,
    text="=",
    font=("Arial", 20),
    height=2,
    command=calculate_expression
)

equal_button.pack(
    padx=15,
    pady=10,
    fill="x"
)

display.bind("<Key>", keyboard_input)

display.focus()

window.mainloop()

