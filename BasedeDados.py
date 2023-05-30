# ==== Importante biblioteca que fará a Criação do Banco de dados
import sqlite3

# ==== Criando Banco de Dados
conn = sqlite3.connect("DadosUsuarios.db")

# ==== Criando Regras e tabelas para o Banco de dados
cursor = conn.cursor()
cursor.execute("""
CREATE TABLE IF NOT EXISTS Usuários (
    id INTEGER  NOT NULL PRIMARY KEY AUTOINCREMENT,
    Nome TEXT NOT NULL,
    Email TEXT NOT NULL,
    Usuário TEX NOT NULL,
    Senha TEXT NOT NULL
    );
""")


print("Conectado ao Banco de Dados")