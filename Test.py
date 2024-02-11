from flask import Flask, jsonify
import pyodbc

app = Flask(__name__)

# Configurações de Conexão
server = 'dbteste.database.windows.net'
database = 'dbteste'
username = 'admin_rapha'
password = 'Y8wRzX5bL2v9GnP'
driver = '{ODBC Driver 17 for SQL Server}'

# Cadeia de Conexão
connection_string = f'DRIVER={driver};SERVER={server};DATABASE={database};UID={username};PWD={password}'


@app.route('/api/data', methods=['GET'])
def get_data():
    try:
        # Estabelecer Conexão
        conn = pyodbc.connect(connection_string)

        # Criar um Cursor
        cursor = conn.cursor()

        # Exemplo: Executar uma Consulta
        cursor.execute("SELECT * FROM Teste")

        # Obter Resultados
        rows = cursor.fetchall()

        # Transformar os Resultados em um Dicionário
        data = []
        for row in rows:
            data.append({'column1': row.Id,
                         'column2': row.NomeServico})  # Substitua 'column1' e 'column2' pelos nomes reais das colunas.

        return jsonify({'data': data})

    except Exception as e:
        return jsonify({'error': str(e)})

    finally:
        # Fechar a Conexão
        if 'conn' in locals():
            conn.close()


if __name__ == '__main__':
    app.run(debug=True)