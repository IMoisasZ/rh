import customtkinter as ctk

class BaseScreen(ctk.CTk):
    def __init__(self, titulo: str = "RH", min_width: int = 800, min_height: int = 600):
        super().__init__()
        # construtor
        self.title(titulo)
        self.min_width = min_width
        self.min_height = min_height

        # definindo  tamanho da tela
        self.default_screen = f'{self.min_width}x{self.min_height}'
        self.geometry(self.default_screen)
        self.after(1, lambda: self.state("zoomed"))

