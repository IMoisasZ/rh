import customtkinter as ctk
from src.components.tabview import Tabview
from src.components.label import Label
from src.components.input import Input
from src.components.select import Select
from src.components.button import Button

class EmployeePage(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        
        self.tab_view_employee = Tabview(self)
        self.tab_view_employee.pack(fill='both', expand=True, pady=10, padx=15)
        self.list_data_employee = ['Dados principais', 'Endereço', 'Contatos', 'Contatos de emergencia', 'Remuneração', 'Observações']
        
        self.created_tabs = {}

        for tab_name in self.list_data_employee:
            tab_frame = self.tab_view_employee.add(tab_name)
            self.created_tabs[tab_name] = tab_frame

            if tab_name == 'Dados principais':
                # Configura o peso para todas as colunas de 0 a 4 para distribuírem o espaço
                for col in range(5):
                    tab_frame.grid_columnconfigure(col, weight=1)
                
                # --- LINHA 0 e 1: Status (Canto Superior Direito) ---
                self.label_status = Label(tab_frame, text="Status")
                self.label_status.grid(row=0, column=4, sticky='w', padx=5, pady=(5,0))
                
                self.status = Input(tab_frame, placeholder_text="Status do colaborador", state="disabled")
                self.status.grid(row=1, column=4, sticky='ew', padx=5, pady=(0,15))
                
                # --- LINHA 2 e 3: Nome, Regime, Nascimento, CPF, RG ---
                # Nome (Coluna 0)
                self.label_name = Label(tab_frame, text="Nome")
                self.label_name.grid(row=2, column=0, sticky='w', padx=5, pady=(5,0))
                
                self.name = Input(tab_frame, placeholder_text="Informe o nome do colaborador")
                self.name.grid(row=3, column=0, sticky='ew', padx=5, pady=(0,15))
                
                # Regime (Coluna 1)
                self.regime_label = Label(tab_frame, text="Regime")
                self.regime_label.grid(row=2, column=1, sticky='w', padx=5, pady=(5,0))
                                
                self.regime_values = ['CLT','PJ','Diretoria']
                self.regime = Select(tab_frame, values=self.regime_values)
                self.regime.grid(row=3, column=1, sticky='ew', padx=5, pady=(0,15))
                
                # Data de Nascimento (Coluna 2)
                self.birthday_label = Label(tab_frame, text="Data de nascimento")
                self.birthday_label.grid(row=2, column=2, sticky='w', padx=5, pady=(5,0))
                
                self.birthday = Input(tab_frame, placeholder_text="DD/MM/AAAA")
                self.birthday.grid(row=3, column=2, sticky='ew', padx=5, pady=(0,15))
                self.birthday._entry.bind("<KeyRelease>", lambda event: self.aplicar_mascara_data(self.birthday))
                
                # CPF (Coluna 3)
                self.cpf_label = Label(tab_frame, text="CPF")
                self.cpf_label.grid(row=2, column=3, sticky='w', padx=5, pady=(5,0))
                
                self.cpf = Input(tab_frame, placeholder_text="Informe o CPF")
                self.cpf.grid(row=3, column=3, sticky='ew', padx=5, pady=(0,15))
                
                # RG (Coluna 4)
                self.rg_label = Label(tab_frame, text="RG")
                self.rg_label.grid(row=2, column=4, sticky='w', padx=5, pady=(5,0))
                
                self.rg = Input(tab_frame, placeholder_text="Informe o RG")
                self.rg.grid(row=3, column=4, sticky='ew', padx=5, pady=(0,15))
                
                # --- LINHA 4 e 5: Setor, Cargo, Gestor ---
                # Setor (Coluna 0)
                self.setor_label = Label(tab_frame, text="Setor")
                self.setor_label.grid(row=4, column=0, sticky='w', padx=5, pady=(5,0))
                
                self.setor_values = ["1","2","3","4","5","6","7","8","9","10"]
                self.setor = Select(tab_frame, values=self.setor_values)
                self.setor.grid(row=5, column=0, sticky='ew', padx=5, pady=(0,15))
                
                # Cargo (Coluna 1)
                self.cargo_label = Label(tab_frame, text="Cargo/Função")
                self.cargo_label.grid(row=4, column=1, sticky='w', padx=5, pady=(5,0))
                
                self.cargo_values = ['1','2','3','4','5','6','7']
                self.cargo = Select(tab_frame, values=self.cargo_values)
                self.cargo.grid(row=5, column=1, sticky='ew', padx=5, pady=(0,15))
                
                # Gestor (Coluna 2)
                self.gestor_label = Label(tab_frame, text="Gestor")
                self.gestor_label.grid(row=4, column=2, sticky='w', padx=5, pady=(5,0))
                
                self.gestor_values = ['1','2','3','4','5','6','7','8','9','10']
                self.gestor = Select(tab_frame, values=self.gestor_values)
                self.gestor.grid(row=5, column=2, sticky='ew', padx=5, pady=(0,15))
                
                # --- LINHA 6 e 7: Datas de Início e Término ---
                # Data Início (Coluna 0)
                self.initial_date_label = Label(tab_frame, text="Data início")
                self.initial_date_label.grid(row=6, column=0, sticky='w', padx=5, pady=(5,0))
                
                self.initial_date = Input(tab_frame, placeholder_text="DD/MM/AAAA")
                self.initial_date.grid(row=7, column=0, sticky='ew', padx=5, pady=(0,15))
                self.initial_date._entry.bind("<KeyRelease>", lambda event: self.aplicar_mascara_data(self.initial_date))
                
                # Data Término (Coluna 1)
                self.final_date_label = Label(tab_frame, text="Data término")
                self.final_date_label.grid(row=6, column=1, sticky='w', padx=5, pady=(5,0))
                
                self.final_date = Input(tab_frame, placeholder_text="Desligamento", state="disabled")
                self.final_date.grid(row=7, column=1, sticky='ew', padx=5, pady=(0,15))
                
                # --- LINHA 8: Container para centralizar múltiplos botões ---
                # Cria um mini frame invisível para agrupar os botões lado a lado
                frame_btn = ctk.CTkFrame(tab_frame, fg_color="transparent")
                frame_btn.grid(row=8, column=0, columnspan=5, pady=(35, 20))

                # Botão Salvar (dentro do mini frame)
                self.btn_save = Button(frame_btn, text="Salvar Colaborador", width=180, cursor='hand2')
                self.btn_save.pack(side="left", padx=10)

                # Botão Cancelar/Voltar ao lado (dentro do mini frame)
                self.btn_cancel = Button(frame_btn, text="Cancelar", width=180, fg_color="gray", cursor='hand2') # Exemplo de cor diferente
                self.btn_cancel.pack(side="left", padx=10)
                
    def aplicar_mascara_data(self, input_field):
        texto = input_field.get()
        numeros = "".join(filter(str.isdigit, texto))
        numeros = numeros[:8]
        
        nova_string = ""
        if len(numeros) > 0:
            nova_string += numeros[:2]
        if len(numeros) >= 3:
            nova_string += "/" + numeros[2:4]
        if len(numeros) >= 5:
            nova_string += "/" + numeros[4:8]
            
        input_field.delete(0, "end")
        input_field.insert(0, nova_string)