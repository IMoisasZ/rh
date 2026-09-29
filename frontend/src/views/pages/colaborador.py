import requests
import customtkinter as ctk
from CTkMessagebox import CTkMessagebox
from src.utils.class_utils import Utils
from src.components.tabview import Tabview
from src.components.label import Label
from src.components.input import Input
from src.components.select import Select
from src.components.button import Button
from src.components.message import Message

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
                self.regime = Select(tab_frame, values=self.regime_values, command=self.ao_mudar_regime)
                self.regime.grid(row=3, column=1, sticky='ew', padx=5, pady=(0,15))
                
                # Data de Nascimento (Coluna 2)
                self.birthday_label = Label(tab_frame, text="Data de nascimento")
                self.birthday_label.grid(row=2, column=2, sticky='w', padx=5, pady=(5,0))
                
                self.birthday = Input(tab_frame, placeholder_text="DD/MM/AAAA")
                self.birthday.grid(row=3, column=2, sticky='ew', padx=5, pady=(0,15))
                self.birthday._entry.bind("<KeyRelease>", lambda event: Utils.aplicar_mascara_data(self.birthday))
                
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
                self.initial_date._entry.bind("<KeyRelease>", lambda event: Utils.aplicar_mascara_data(self.initial_date))
                
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
                self.btn_save = Button(frame_btn, text="Salvar Colaborador", width=180, cursor='hand2', command=self.enviar_dados_api)
                self.btn_save.pack(side="left", padx=10)

                # Botão Cancelar/Voltar ao lado (dentro do mini frame)
                self.btn_cancel = Button(frame_btn, text="Cancelar", width=180, fg_color="gray", cursor='hand2') # Exemplo de cor diferente
                self.btn_cancel.pack(side="left", padx=10)

    def enviar_dados_api(self):
        # Converte as datas antes de enviar para o formato YYYY-MM-DD
        data_nasc_iso = Utils.converter_data_para_iso(self.birthday.get())
        data_inicio_iso = Utils.converter_data_para_iso(self.initial_date.get())
        data_termino_iso = Utils.converter_data_para_iso(self.final_date.get()) if self.final_date.get() else None

        dados_colaborador = {
            "status": "ATIVO",
            "nome": self.name.get(),
            "regime": self.regime.get(),
            "data_nascimento": data_nasc_iso,
            "cpf": self.cpf.get(),
            "rg": self.rg.get(),
            "setor_id": int(self.setor.get()) if self.setor.get() else None,
            "cargo_id": int(self.cargo.get()) if self.cargo.get() else None,
            "gestor_id": int(self.gestor.get()) if self.gestor.get() else None,  # <--- Alterado de 'gestor' para 'gestor_id' e convertido para int
            "data_inicio": data_inicio_iso,
            "data_termino": data_termino_iso
        }

        url_api = "http://127.0.0.1:8000/api/v1/colaboradores/"

        try:
            print("Enviando dados para a API...", dados_colaborador)
            resposta = requests.post(url_api, json=dados_colaborador)

            if resposta.status_code in [200, 201]:
                print("Sucesso! Colaborador cadastrado:", resposta.json())
                Message.show_message(msg="Colaborador cadastro com sucesso!", option_1="Ok", title="Sucesso", icon="success")

                if self.regime.get() == "PJ":
                    self.adicionar_aba_pj()
                    # Opcional: já mudar o foco para a nova aba criada
                    self.tab_view_employee.set("Dados PJ")
            else:
                print(f"Erro da API ({resposta.status_code}):", resposta.text)
                
                try:
                    erro_json = resposta.json()
                    
                    # O FastAPI costuma retornar os erros de validação na chave "detail"
                    detalhe = erro_json.get("detail", "Erro desconhecido")
                    
                    # Se for uma lista de erros (comum no Pydantic/422)
                    if isinstance(detalhe, list) and len(detalhe) > 0:
                        # Pega o primeiro erro da lista e extrai a chave 'msg'
                        mensagem_amigavel = detalhe[0].get("msg", str(detalhe))
                    elif isinstance(detalhe, str):
                        # Se for uma string simples (como os erros 400 customizados)
                        mensagem_amigavel = detalhe
                    else:
                        mensagem_amigavel = str(detalhe)
                        
                except Exception:
                    mensagem_amigavel = resposta.text

                # Exibe a mensagem limpa na caixa de diálogo
                Message.show_message(msg=mensagem_amigavel, title='Atenção', icon='error', option_1='OK')
                
        except requests.exceptions.ConnectionError:
            print("Erro de Conexão: Não foi possível conectar ao FastAPI.")
            Message.show_message(msg="Não foi possível conectar ao servidor da API.\nVerifique se o FastAPI está rodando.",
                                 option_1="OK",
                                 title="Erro de conexão",
                                 icon="warning")

    def ao_mudar_regime(self, escolha):
        """Função chamada sempre que o usuário altera o tipo de regime no combobox"""
        abas_atuais = self.tab_view_employee.get() # Pega a aba ativa atualmente
        
        if escolha == "PJ":
            # Verifica se a aba PJ já existe antes de adicionar para não duplicar
            if "Dados PJ" not in self.tab_view_employee._tab_dict:
                self.tab_view_employee.add("Dados PJ")
                # Aqui você constrói os campos da aba PJ igual fizemos antes
                self.construir_campos_pj()
        else:
            # Se mudou para CLT (ou outro), remove a aba PJ se ela existir
            if "Dados PJ" in self.tab_view_employee._tab_dict:
                # Se o usuário estiver com a aba PJ aberta na hora que mudou, voltamos para 'Dados principais'
                if self.tab_view_employee.get() == "Dados PJ":
                    self.tab_view_employee.set("Dados principais")
                self.tab_view_employee.delete("Dados PJ")

    def construir_campos_pj(self):
        """Constrói os inputs dentro da aba PJ"""
        tab_pj = self.tab_view_employee.tab("Dados PJ")
        
        # Configuração do grid da aba PJ
        for col in range(3):
            tab_pj.grid_columnconfigure(col, weight=1)
            
        # Exemplo de campos PJ
        self.label_cnpj = Label(tab_pj, text="CNPJ")
        self.label_cnpj.grid(row=0, column=0, sticky='w', padx=5, pady=(5,0))
        
        self.cnpj = Input(tab_pj, placeholder_text="00.000.000/0001-00")
        self.cnpj.grid(row=1, column=0, sticky='ew', padx=5, pady=(0,15))
        
        self.label_razao = Label(tab_pj, text="Razão Social")
        self.label_razao.grid(row=0, column=1, sticky='w', padx=5, pady=(5,0))
        
        self.razao_social = Input(tab_pj, placeholder_text="Nome da empresa")
        self.razao_social.grid(row=1, column=1, sticky='ew', padx=5, pady=(0,15))