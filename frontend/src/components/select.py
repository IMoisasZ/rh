from tkinter.constants import NORMAL

import customtkinter as ctk

class Select(ctk.CTkOptionMenu):
    def __init__(self, master, width:int = 140, height:int = 28, bg_color:str = "transparent", fg_color:str = None, text_color:str = None, font = ("Arial", 12), values:str = None, state:str = "normal", anchor:str = "w", **kwargs):
        super().__init__(master, width = width, height = height, bg_color = bg_color, fg_color = fg_color, text_color = text_color, font = font, values = values, state = state, anchor = anchor, **kwargs)
        self.width = width
        self.height = height
        self.bg_color = bg_color
        self.fg_color = fg_color
        self.text_color = text_color
        self.font = font
        self.values = values
        self.state = state
        self.anchor = anchor