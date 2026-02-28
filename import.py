import json
import os

ARQUIVO = "tarefas.json"

def carregar_tarefas():
    if os.path.exists(ARQUIVO):
        with open(ARQUIVO, "r") as f:
            return json.load(f)
    return []

def salvar_tarefas(tarefas):
    with open(ARQUIVO, "w") as f:
        json.dump(tarefas, f, indent=4)

def adicionar_tarefa(tarefas):
    titulo = input("Título: ")
    prioridade = input("Prioridade (baixa/media/alta): ")

    tarefa = {
        "id": len(tarefas) + 1,
        "titulo": titulo,
        "prioridade": prioridade,
        "concluida": False
    }

    tarefas.append(tarefa)
    salvar_tarefas(tarefas)
    print("Tarefa adicionada com sucesso.")

def listar_tarefas(tarefas):
    if not tarefas:
        print("Nenhuma tarefa cadastrada.")
        return

    for t in tarefas:
        status = "✔" if t["concluida"] else "✘"
        print(f'{t["id"]} - {t["titulo"]} [{t["prioridade"]}] {status}')

def concluir_tarefa(tarefas):
    listar_tarefas(tarefas)
    try:
        id_tarefa = int(input("Digite o ID da tarefa: "))
        for t in tarefas:
            if t["id"] == id_tarefa:
                t["concluida"] = True
                salvar_tarefas(tarefas)
                print("Tarefa concluída.")
                return
        print("ID não encontrado.")
    except:
        print("Entrada inválida.")

def main():
    tarefas = carregar_tarefas()

    while True:
        print("\n==== GERENCIADOR DE TAREFAS ====")
        print("1 - Adicionar")
        print("2 - Listar")
        print("3 - Concluir")
        print("0 - Sair")

        opcao = input("Escolha: ")

        if opcao == "1":
            adicionar_tarefa(tarefas)
        elif opcao == "2":
            listar_tarefas(tarefas)
        elif opcao == "3":
            concluir_tarefa(tarefas)
        elif opcao == "0":
            break
        else:
            print("Opção inválida.")

if __name__ == "__main__":

    main()
