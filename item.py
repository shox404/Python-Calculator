def sign(app, entry, frame, sign, c, r):
    app.CTkButton(
        frame,
        text=sign,
        width=60,
        height=50,
        fg_color="orange",
        hover_color="yellow",
        text_color="black",
        command=lambda: entry.insert(app.END, sign),
    ).grid(column=c, row=r, padx=5, pady=5)
