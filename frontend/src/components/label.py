import customtkinter as ctk

class Label(ctk.CTkLabel):
    def __init__(self, master, width: int = 0, height: int = 28, bg_color: str = "transparent", fg_color: str = None, border_color: str = None, text_color: str = None, text: str = "label_name", font = ("Arial", 16), anchor: str = "center", **kwargs):
        super().__init__(master, width = width, height = height, bg_color = bg_color, fg_color = fg_color, border_color = border_color, text_color = text_color, text = text, font = font, anchor = anchor, **kwargs)
        self.width = width
        self.height = height
        self.bg_color = bg_color
        self.fg_color = fg_color
        self.border_color = border_color
        self.text_color = text_color
        self.text = text
        self.font = font
        self.anchor = anchor
