import customtkinter as app
from lib import calculate

root = app.CTk()
root.geometry("300x505")
root.resizable(False, False)
root.title("Calculator")

header = app.CTkFrame(root)
header.grid(padx=10, pady=10)

entry = app.CTkEntry(header, width=270, height=40)
entry.grid(column=0, row=0, padx=5, pady=5)

methods = app.CTkFrame(root)
methods.grid(padx=10, pady=10)

app.CTkButton(
    methods,
    text="+",
    width=60,
    height=50,
    fg_color="orange",
    hover_color="yellow",
    text_color="black",
    command=lambda: entry.insert(app.END, "+"),
).grid(column=0, row=0, padx=5, pady=5)

app.CTkButton(
    methods,
    text="-",
    width=60,
    height=50,
    fg_color="orange",
    hover_color="yellow",
    text_color="black",
    command=lambda: entry.insert(app.END, "-"),
).grid(column=1, row=0, padx=5, pady=5)

app.CTkButton(
    methods,
    text="*",
    width=60,
    height=50,
    fg_color="orange",
    hover_color="yellow",
    text_color="black",
    command=lambda: entry.insert(app.END, "*"),
).grid(column=2, row=0, padx=5, pady=5)

app.CTkButton(
    methods,
    text="/",
    width=60,
    height=50,
    fg_color="orange",
    hover_color="yellow",
    text_color="black",
    command=lambda: entry.insert(app.END, "/"),
).grid(column=3, row=0, padx=5, pady=5)

body = app.CTkFrame(root)
body.grid(padx=10, pady=10)

app.CTkButton(
    body,
    text="1",
    width=80,
    height=50,
    fg_color="#1e1e1e",
    hover_color="#000",
    command=lambda: entry.insert(app.END, "1"),
).grid(column=0, row=1, padx=6.5, pady=6.5)

app.CTkButton(
    body,
    text="2",
    width=80,
    height=50,
    fg_color="#1e1e1e",
    hover_color="#000",
    command=lambda: entry.insert(app.END, "2"),
).grid(column=1, row=1, padx=6.5, pady=6.5)

app.CTkButton(
    body,
    text="3",
    width=80,
    height=50,
    fg_color="#1e1e1e",
    hover_color="#000",
    command=lambda: entry.insert(app.END, "3"),
).grid(column=2, row=1, padx=6.5, pady=6.5)

app.CTkButton(
    body,
    text="4",
    width=80,
    height=50,
    fg_color="#1e1e1e",
    hover_color="#000",
    command=lambda: entry.insert(app.END, "4"),
).grid(column=0, row=2, padx=6.5, pady=6.5)

app.CTkButton(
    body,
    text="5",
    width=80,
    height=50,
    fg_color="#1e1e1e",
    hover_color="#000",
    command=lambda: entry.insert(app.END, "5"),
).grid(column=1, row=2, padx=6.5, pady=6.5)

app.CTkButton(
    body,
    text="6",
    width=80,
    height=50,
    fg_color="#1e1e1e",
    hover_color="#000",
    command=lambda: entry.insert(app.END, "6"),
).grid(column=2, row=2, padx=6.5, pady=6.5)

app.CTkButton(
    body,
    text="7",
    width=80,
    height=50,
    fg_color="#1e1e1e",
    hover_color="#000",
    command=lambda: entry.insert(app.END, "7"),
).grid(column=0, row=3, padx=6.5, pady=6.5)

app.CTkButton(
    body,
    text="8",
    width=80,
    height=50,
    fg_color="#1e1e1e",
    hover_color="#000",
    command=lambda: entry.insert(app.END, "8"),
).grid(column=1, row=3, padx=6.5, pady=6.5)

app.CTkButton(
    body,
    text="9",
    width=80,
    height=50,
    fg_color="#1e1e1e",
    hover_color="#000",
    command=lambda: entry.insert(app.END, "9"),
).grid(column=2, row=3, padx=6.5, pady=6.5)

app.CTkButton(
    body,
    text="0",
    width=80,
    height=50,
    fg_color="#1e1e1e",
    hover_color="#000",
    command=lambda: entry.insert(app.END, "0"),
).grid(column=1, row=4, padx=6.5, pady=6.5)

footer = app.CTkFrame(root)
footer.grid(padx=10, pady=10)

app.CTkButton(
    footer,
    text="calculate",
    width=270,
    height=50,
    fg_color="orange",
    hover_color="yellow",
    text_color="black",
    command=lambda: calculate(entry),
).grid(column=0, row=4, padx=6.5, pady=6.5)

root.mainloop()
