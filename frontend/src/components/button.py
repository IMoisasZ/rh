import customtkinter as ctk

class Button(ctk.CTkButton):
    def __init__(self, master, width: int=140, height: int=28, bg_color: str = "transparent", fg_color: str = None, hover_color: str=None, text_color: str = None, text_color_disabled: str = None, text = "btn_name", font: str = ("Arial",12), image: str = None, state: str = "normal", hover = True, command = None, anchor: str = "center", **kwargs):
        super().__init__(master, width=width, height=height, bg_color=bg_color, fg_color=fg_color, hover_color=hover_color, text_color=text_color, text_color_disabled=text_color_disabled, text=text, font=font, image=image, state=state, hover=hover, command=command, anchor=anchor, **kwargs)
        self.width = width
        self.height = height
        self.bg_color = bg_color
        self.fg_color = fg_color
        self.hover_color = hover_color
        self.text_color = text_color
        self.text_color_disabled = text_color_disabled
        self.text = text
        self.font = font
        self.image = image
        self.state = state
        self.hover = hover
        self.command = command
        self.anchor = anchor

