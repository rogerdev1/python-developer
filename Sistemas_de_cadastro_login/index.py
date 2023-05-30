# Importante bibliotecas
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import BasedeDados

# ========================= Criando Janela ============================ #

# Adicionando, na ordem: janela, titulo, tamanho, fundo, responsividade e icone
janela = Tk()
janela.title("RVS System - Painel de acesso")
janela.geometry("700x300")
janela.configure(background="grey")
janela.resizable(width=False, height=False)


# ====================== Widgets do Menu Inicial ======================== #

# ===== Carregando Imagens ===== #
logo = PhotoImage(file="icones/icon.png")

# ===== Criando Divisão na Janela ====== #
LadoEsquerdo = Frame(janela, width=200, height=300, bg="PURPLE", relief="raise")
LadoEsquerdo.pack(side=LEFT)

LadoDireio = Frame(janela, width=495, height=300, bg="PURPLE", relief="raised")
LadoDireio.pack(side=RIGHT)

# ===== Adcionando Conteúdo ======= #

MensagemEntrada = Label(LadoDireio, text="     Bem Vindo(a) ao Portal de Acesso", font=("Times", 20), bg="PURPLE", fg="white")
MensagemEntrada.place(x=30, y=40)

LogoLabel = Label(LadoEsquerdo, image=logo, bg="PURPLE")
LogoLabel.place(x=50, y=100)

UsuarioLabel = Label(LadoDireio, text="Usuário: ", font=("Century Gothic", 20), bg="PURPLE", fg="white")
UsuarioLabel.place(x=50, y=122)

SenhaLabel = Label(LadoDireio, text="Senha: ", font=("Century Gothic", 20), bg="PURPLE", fg="white")
SenhaLabel.place(x=50, y=160)

# ======= Entrada de Dados ====== #

UsuarioEntry = ttk.Entry(LadoDireio, width=40)
UsuarioEntry.place(x=160, y=135)

SenhaEntry = ttk.Entry(LadoDireio, width=40, show="*")
SenhaEntry.place(x=160, y=173)

def Login():
    Usuário = UsuarioEntry.get()
    Senha = SenhaEntry.get()
    
    BasedeDados.cursor.execute("""
    SELECT * FROM Usuários
    WHERE (Usuário = ? and Senha = ?)    
    """, (Usuário, Senha))
    print("selecionou")
    VerificadorLogin = BasedeDados.cursor.fetchone()
    try: 
        if Usuário in VerificadorLogin and Senha in VerificadorLogin:
            messagebox.showinfo(title="Acesso ao Sistema", message="Bem Vindo(a)")
    except:
        messagebox.showerror(title="Acesso Negado", message="Usuário ou Senha Incorretos")
    

# ====================== Adicionando Botões Interativos ====================== #

# Serão adicionados, no menu inicial, o botão "Login" e, após a criação da def Cadastro, o botão "Cadastre-se"
LoginBotao = ttk.Button(LadoDireio, text="Login", command=Login)
LoginBotao.place(x=240, y=205)

# ======================= Acessando o Menu de Cadastro ======================= #

# === Ligando a Função(def) "Cadastro()" ao COMMAND do "CadastroBotao"
def Cadastro():
    # == Removendo Widgets do Menu Inicial == #
    LoginBotao.place(x=5000)
    CadastroBotao.place(x=5000)
    MensagemEntrada.place(x=5000)
    # == Adicionando Widgets ao Menu de Cadastro == #
    MensagemCadastro = Label(LadoDireio, text="Preencha os seguintes dados:", font=("Times", 20), bg="PURPLE", fg="WHITE")
    MensagemCadastro.place(x=100, y=5)

    NomeCompleto = Label(LadoDireio, text="Nome: ", font=("Century Gothic", 20), bg="PURPLE", fg="WHITE")
    NomeCompleto.place(x=50, y=50)
    NomeEntry = Entry(LadoDireio, width=40, bg="WHITE")
    NomeEntry.place(x=160, y=65)

    Email = Label(LadoDireio, text="E-mail: ", font=("Century Gothic", 20), bg="PURPLE", fg="WHITE")
    Email.place(x=50, y=87)
    EmailEntry = Entry(LadoDireio, width=40, bg="WHITE")
    EmailEntry.place(x=160, y=100)

    # ==== Criando Conexão com Banco de Dados ==== #
    def RegistrarBasededados():
        Nome = NomeEntry.get()
        Email = EmailEntry.get()
        Usuario = UsuarioEntry.get()
        Senha= SenhaEntry.get()

        if (Nome == ""):
            messagebox.showerror(title="Erro", message="Campo 'Nome' Não Preenchido")
        elif (Email == ""):
            messagebox.showerror(title="Erro", message="Campo 'E-mail' Não Preenchido")
        elif (Usuario == ""):
            messagebox.showerror(title="Erro", message="Campo 'Usuário' Não Preenchido")
        elif (Senha == ""):
            messagebox.showerror(title="Erro", message="Campo 'Nome' Não Preenchido")
        else:
            BasedeDados.cursor.execute("""
            INSERT INTO Usuários(Nome, Email, Usuário, Senha) VALUES (?, ?, ?, ?)
            """, (Nome, Email, Usuario, Senha))
            # === Salvando dados ==== #
            BasedeDados.conn.commit()
            # === Emitindo Mensagem de aviso === #
            messagebox.showinfo(title="informação do Sistema", message="Cadastro Realizado com Sucesso")
        

    # === Ligando o Botão "SalvarDados" a Base de Dados pelo COMMANDO=BasedeDdos
    SalvarDados = ttk.Button(LadoDireio, text="Salvar Dados", width=20, command=RegistrarBasededados)
    SalvarDados.place(x=212, y=225)

    #==================== Retornando ao Menu Inicial ==================#

    #=== Ligando o Botão "Voltar" ao COMMAND do "SalvarDados"
    def MenuInicial():
        #=== Remover a Mensagem de Cadastro, Entrada de Nome e E-mail
        MensagemCadastro.place(x=5000)
        NomeCompleto.place(x=5000)
        NomeEntry.place(x=5000)
        Email.place(x=5000)
        EmailEntry.place(x=5000)
        SalvarDados.place(x=5000)
        Voltar.place(x=5000)
        #=== Retornando Widgets do Menu de Inico ==
        MensagemEntrada.place(x=30, y=40)
        LoginBotao.place(x=240, y=205)
        CadastroBotao.place(x=212, y=245)
    
    Voltar = Button(LadoDireio, text="Voltar", width=15, bg="WHITE", command=MenuInicial)
    Voltar.place(x=220, y=255)
   
    
CadastroBotao = ttk.Button(LadoDireio, text="Cadastre-se", width=20, command=Cadastro)
CadastroBotao.place(x=212, y=245)

# ========== Encerrando a Janela ======== #

janela.mainloop()

