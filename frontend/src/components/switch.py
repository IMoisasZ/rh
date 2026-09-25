import customtkinter as ctk

class Switch(ctk.CTkSwitch):
    def __init__(self, master, text: str = "switch_name", font: str = ("Arial", 12), command = None, **kwargs):
        super().__init__(master, text = text, font = font, command = command, **kwargs)
        self.text = text
        self.font = font
        self.command = command