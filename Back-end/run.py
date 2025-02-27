from app import create_app

app = create_app()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)



#Para rodar a venv e desativar
# venv\Scripts\activate
# deactivate

#Para rodar a aplicação-disponivel no meu localhost, e na minha rede locar, colocando o ip do computador
#Exemplo   'http://ip do computador{192.168.237.80}:5000/'
# python -m flask run --host=0.0.0.0 --port=5000
