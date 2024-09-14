import tkinter as tk

methods = list(["+", "-", "*", "/"])


def calculate(entry):
    value = entry.get()
    for method in methods:
        if method in value:
            numbers = str(value).split(method)
            if method in value:
                entry.delete(0, tk.END)
                number = [int(numbers[0]), int(numbers[1])]
                match method:
                    case "+":
                        entry.insert(0, max(number) + min(number))
                    case "-":
                        entry.insert(0, max(number) - min(number))
                    case "*":
                        entry.insert(0, max(number) * min(number))
                    case "/":
                        entry.insert(0, max(number) // min(number))
