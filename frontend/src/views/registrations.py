import customtkinter as ctk
from src.components.tabview import Tabview

class Registrations(Tabview):
    def __init__(self, master, width = 300, height = 250, bg_color = "transparent", fg_color = None, border_color = None, command=None, anchor = "center", state = "normal", **kwargs):
      super().__init__(master, width, height, bg_color, fg_color, border_color, command, anchor, state, **kwargs)

    def load_items_registrations(self):
        self.list_registrations = ['Setor','Cargo']

        for item in self.list_registrations:
            self.add(item)
    


