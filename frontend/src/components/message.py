from CTkMessagebox import CTkMessagebox

class Message(CTkMessagebox):
    def show_message(title:str, msg:str, option_1:str, icon:str):
        """
            <h5>Função para mostrar mensagens para o usuário:</h5>
            <p>Parametros da função:<p>
                <ul>
                    <li>type_msg: Tipo de mensagem:</li>
                    <ul>
                        <li>info = Informação</li>
                        <li>success = Sucesso</li>
                        <li>error = Erro</li>
                        <li>warning = Atenção</li>
                        <li>question = Pergunta</li>
                    </ul>
                    <li>title: Tittulo da mensagem</li>
                    <li>msg: Testo da mensagem</li>
                    <li>option_1: Texto que aparece nobotão de confirmação</li>
                    <li>icon: Texto do nome do icon, conforme abaixo:</li>
                    <ul>
                        <li>success: check</li>
                        <li>info: info</li>
                        <li>error: cancel</li>
                        <li>warning: warning</li>
                        <li>question: question</li>
                    </ul>
                </ul>                    
        """
        list_icons = {
                    "info": "info",
                    "success": "check",
                    "error": "cancel",
                    "warning": "warning",
                    "question": "question"
                }
        CTkMessagebox(title=title, message=msg, icon=list_icons[icon], option_1=option_1)