from src.controller.sql_controller import SQLController
from src.server.server_setup import setup_server
from configs import PORT
import psycopg2

print("Starting script")
conn = psycopg2.connect(
        database = 'eleicoes2020',
        user='docker',
        password='docker',
        host='0.0.0.0'
    )
cur = conn.cursor()

controller = SQLController(conn, cur)

app, socketio = setup_server(controller)
socketio.run(app, port=PORT)

cur.close()
conn.close()
