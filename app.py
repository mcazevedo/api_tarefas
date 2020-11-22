from flask import Flask, jsonify, request
import json

app = Flask(__name__)

tarefas = [

    {"id":"0",
     "responsavel":"Carlos Andrade",
     "tarefa":"Limpar a calçada",
     "Status":"A iniciar"},

     {"id":"1",
     "responsavel":"Jotinha Bahia",
     "tarefa":"Humor do bem",
     "Status":"Concluído com sucesso"},

    {"id":"2",
     "responsavel":"Matheus",
     "tarefa":"Podcast politico",
     "Status":"Em andamento"}
    ]

# Lista todas as tarefas e insere uma tarefa
@app.route("/tarefa/", methods=["GET", "POST"])
def listaInsereTarefa():
    if request.method == "GET":
        return jsonify(tarefas)
    elif request.method == "POST":
        dados = json.loads(request.data)
        posicao = len(tarefas)
        dados['id'] = posicao
        tarefas.append(dados)
        return jsonify({"status":"sucesso", "mensagem":f"registro criado com sucesso."})

# Lista, atualiza ou deleta uma tarefa pelo ID
@app.route("/tarefa/<int:id>", methods=["GET", "PUT", "DELETE"])
def listaAtualizaDeletaTarefa(id):
    if request.method == "GET":
        try:
            tarefa = tarefas[id]
            return jsonify(tarefa)
        except IndexError:
            return jsonify({"status":"Erro!", "mensagem":f"A tarefa de ID {id} não existe."})
        except Exception:
            return jsonify({"status": "Erro!", "mensagem": f"Erro desconhecido, entre em contato com o adm"})

    elif request.method == "PUT":
        try:
            tarefas[id] = json.loads(request.data)
            return jsonify({"status":"sucesso", "mensagem":f"Usuário {id} cadastrado com sucesso"})
        except IndexError:
            return jsonify({"status": "Erro!", "mensagem": f"A tarefa de ID {id} não existe."})
        except Exception:
            return jsonify({"status": "Erro!", "mensagem": f"Erro desconhecido, entre em contato com o adm"})

    elif request.method == "DELETE":
        try:
            tarefas.pop(id)
            return jsonify({"status": "sucesso", "mensagem": f"Usuário {id} deletado com sucesso"})
        except Exception:
            return jsonify({"status": "Erro!", "mensagem": f"Erro desconhecido, entre em contato com o adm"})

if __name__ == '__main__':
    app.run(debug=True)