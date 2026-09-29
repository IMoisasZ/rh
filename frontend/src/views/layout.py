import customtkinter as ctk
from src.components.base_screen import BaseScreen
from src.components.button import Button
from src.components.switch import Switch
from src.components.label import Label
from src.components.tabview import Tabview
from src.views.pages.colaborador import EmployeePage

class LayoutSystem(BaseScreen):
    def __init__(self, titulo='RH', min_width = 800, min_height = 600):
        super().__init__(titulo, min_width, min_height)
        
        self.tabs_config = {
            "Cadastros": [('Setor', None),('Cargo', None),('Colaborador', EmployeePage), ('Diretoria', None)],
            "Holerites": [('Enviar holerites', None)],
            "Relatórios": [('Setores', None), ('Cargos', None), ('Colaboradores', None)]
        }

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
        self.list_items = ['Cadastros','Holerites','Relatórios']
        # Execução da lista do menu lateral
        for item in self.list_items:
            Button(self.lateral_menu, text=item, command=lambda valor=item: self.load_tab(valor)).pack(pady=10, padx=5)

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
        
    def clear_main_area(self):
        for widget in self.main_data.winfo_children():
            widget.destroy()
        
    def load_tab(self, item):
        # Limpa área principal antes de desenhar o novo painel
        self.clear_main_area()

        # Pega a lista de abas correspondente ao botão clicado
        tabs_to_create = self.tabs_config.get(item, [])

        if not tabs_to_create:
            return

        # Cria o CTkTabview dentro da área principal
        self.current_tabview = Tabview(self.main_data)
        self.current_tabview.pack(fill="both", expand=True, padx=10, pady=10)

        # 4. Adiciona cada aba dinamicamente usando um loop
        for tab_name, PageClass in tabs_to_create:
            # Cria a aba e retorna o frame dela
            self.tab_frame = self.current_tabview.add(tab_name)
            
            # Colocar um título dentro de cada aba criada
            Label(
                self.tab_frame, 
                text=f"Painel de {tab_name}", 
                font=("Arial", 20, "bold")
            ).pack(pady=20, padx=20)
            
            # Instancia a página passando a aba como master (pai)
            if PageClass:
                instance_page = PageClass(master=self.tab_frame)
                instance_page.pack(fill="both", expand=True)
            

