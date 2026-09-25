import customtkinter as ctk

class Tabview(ctk.CTkTabview):
    def __init__(self, master, width: int = 300, height: int = 250, bg_color: str = "transparent", fg_color: str = None, border_color: str = None, command = None, anchor: str = "center", state: str = "normal", **kwargs):
        super().__init__(master, width = width, height = height, bg_color = bg_color, fg_color = fg_color, border_color = border_color, command = command, anchor = anchor, state = state, **kwargs)
        self.width = width
        self.width = width
        self.height = height
        self.height = height
        self.bg_color = bg_color
        self.bg_color = bg_color
        self.fg_color = fg_color
        self.fg_color = fg_color
        self.border_color = border_color
        self.border_color = border_color
        self.command = command
        self.command = command
        self.anchor = anchor
        self.anchor = anchor
        self.state = state
        self.state = state

