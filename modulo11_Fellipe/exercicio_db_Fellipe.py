import sqlite3

conn = sqlite3.connect('exercicio_pratico_BD.db')
cursor = conn.cursor()

cursor.execute('''

    CREATE TABLE IF NOT EXISTS clientes (
        id INTEGER PRIMARY KEY,
        nome TEXT NOT NULL,
        email TEXT NOT NULL
    )

''')

cursor.execute('''

    INSERT INTO clientes (nome, email) VALUES 
    ('João Silva', 'joao.silva@mail.com'),
    ('Maria Oliveira', 'maria.oliveira@mail.com'),
    ('Carlos Santos', 'carlos.santos@mail.com')

''')

conn.commit()

cursor.execute('SELECT * FROM clientes')

clientes = cursor.fetchall()

print("Clientes:")
for cliente in clientes:
    print(cliente)