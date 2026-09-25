import customtkinter as ctk
from src.components.base_screen import BaseScreen
from src.components.button import Button
from src.components.switch import Switch
from src.components.label import Label
from src.views.registrations import Registrations

class LayoutSystem(BaseScreen):
    def __init__(self, titulo='RH', min_width = 800, min_height = 600):
        super().__init__(titulo, min_width, min_height)

        # Configuração do Grid principal da janela
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        # Menu lateral (coluna 0)
        self.lateral_menu = ctk.CTkFrame(self, width=200)
        self.lateral_menu.grid(row=0, column=0, sticky='nsew', pady=10, padx=(10,0))

        self.load_itens_lateral_menu()

        # Area de conteudo
        self.main_data = ctk.CTkFrame(self)
        self.main_data.grid(row=0, column=1, sticky='nsew', pady=10, padx=10)

        self.load_main_data()

    def load_itens_lateral_menu(self):
        # Titulo e subtitulo do menu lateral
        Label(self.lateral_menu, text="RH").pack(pady=(10,0), padx=5)
        Label(self.lateral_menu, text="Gestão de Colaboradores", font=("Arial", 10)).pack(pady=(0,20))

        # Lista de itens do menu lateral
        self.list_items = [{'name':'Cadastros','page':Registrations},
                           {'name':'Holerites','page':''},
                           {'name': 'Relatórios', 'page': ''}]
        # Execução da lista do menu lateral
        for item in self.list_items:
            Button(self.lateral_menu, text=item['name'], command=self.load_data_item(item['page'])).pack(pady=10, padx=5)

        # Carregar o botão switch (modo escuro) no menu lateral
        self.load_switch_lateral_menu()

    def load_switch_lateral_menu(self):
        self.switch_modo_screen = Switch(self.lateral_menu, text='Modo escuro', command=self.change_mode_screen)
        self.switch_modo_screen.pack(pady=(0,10), padx=10, side='bottom')
        self.switch_modo_screen.set(True)

    def change_mode_screen(self):
        actual_mode = ctk.get_appearance_mode()
        if actual_mode == "Dark":

            ctk.set_appearance_mode("Light")
        else:
            ctk.set_appearance_mode("Dark")

    def load_main_data(self):
        Label(self.main_data, text="Colaboradores", font=("Arial", 30)).pack(pady=10)

    def limpar_area_dados(self):
        # Destrói tudo o que estiver atualmente na área da direita
        for widget in self.data_area.winfo_children():
            widget.destroy()

    def load_data_item(self, tab):
        self.limpar_area_dados()

        self.main_data = tab
