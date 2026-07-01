import sqlite3
import os

PASTA = "arquivos"
CAMINHO_ARQUIVO = os.path.join(PASTA, "biblioteca.db")

def acoes_no_banco(query, args):
    conn = sqlite3.connect(CAMINHO_ARQUIVO)
    cursor = conn.cursor()
    cursor.execute(query, args)
    conn.commit()
    conn.close()

def extrair_do_banco(query):
    conn = sqlite3.connect(CAMINHO_ARQUIVO)
    cursor = conn.cursor()
    cursor.execute(query)
    result = cursor.fetchall()
    conn.close()
    return result



acoes_no_banco(
    """
    CREATE TABLE IF NOT EXISTS livros (
        isbn TEXT PRIMARY_KEY UNIQUE,
        titulo TEXT,
        autor TEXT,
        genero TEXT,
        ano_publicacao INTEGER,
        editora TEXT,
        paginas INTEGER,
        status TEXT,
        localizacao TEXT
    );
    """,
    []
)

args = (
    '978-6559882403',
    'Em Seus Passos que Faria Jesus?',
    'Charles Sheddon',
    'Romance',
    1896,
    'Companhia das Letras',
    416,
    'disponivel',
    'Estante A1, Prateleira 2'
)

acoes_no_banco(
    """INSERT INTO livros VALUES(?,?,?,?,?,?,?,?,?);""",
    args
)  
print(extrair_do_banco(
    """
    SELECT * FROM livros;
    """
))