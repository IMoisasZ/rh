import customtkinter as ctk


class Input(ctk.CTkEntry):
    def __init__(self, master, width:int = 140, height:int = 28, bg_color:str = "transparent", fg_color:str = None, border_color:str = None, text_color:str = None, placeholder_text_color:str = None, placeholder_text:str = None, font = ("Arial", 12), state:str = "normal", **kwargs):
        super().__init__(master, width = width, height = height, bg_color = bg_color, fg_color = fg_color, border_color = border_color, text_color = text_color, placeholder_text_color = placeholder_text_color, placeholder_text = placeholder_text, font = font, state = state, **kwargs)
        self.width = width
        self.height = height
        self.bg_color = bg_color
        self.fg_color = fg_color
        self.border_color = border_color
        self.text_color = text_color
        self.placeholder_text_color = placeholder_text_color
        self.placeholder_text = placeholder_text
        self.font = font
        self.state = state
