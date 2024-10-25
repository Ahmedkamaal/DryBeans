import tkinter as tk


class CustomButton:
    def __init__(self, frame, text):
        self.button_border = tk.Frame(frame, bg="white")
        self.btn = tk.Button(
            frame,
            relief=tk.FLAT,
            text=text,
            bg="#262730",
            font=("bold", 16),
            fg="white",
            cursor="hand2",
            activebackground="#262730",
            activeforeground="#dc4343",
        )
        self.btn.bind('<Enter>', lambda event: self.on_enter(self.btn))
        self.btn.bind('<Leave>', lambda event: self.on_leave(self.btn))
        self.btn.bind("<Configure>", self.adjust_border_size)

    def place(self, x, y):
        self.button_border.place(x=x-1, y=y-1)
        self.btn.place(x=x, y=y)

    def on_enter(self, e):
        e.config(foreground="#dc4343")
        self.button_border.config(background="#dc4343")

    def on_leave(self, e):
        e.config(foreground="white")
        self.button_border.config(background="white")

    def adjust_border_size(self, event):
        self.button_border.configure(width=self.btn.winfo_width() + 2, height=self.btn.winfo_height() + 2)
