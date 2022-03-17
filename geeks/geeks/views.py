from django.http import HttpResponse
from django.shortcuts import render
from geeks.entity import ToDo


lista_to_do = [
    ToDo(1, "eCAC Analise", "Analisar site eCAC", 0, "2022-03-31")
]  # ToDo(id, assunto, descricao, prioridade, data_limite)


def home(request):
    return render(request, "todos.html", {"lista_to_do": lista_to_do})


def add_to_do(request):
    if request.method == 'POST':
        assunto = request.POST.get('assunto', str)
        descricao = request.POST.get('descricao', str)
        prioridade = request.POST.get('prioridade', int)
        data_limite = request.POST.get('data_limite', str)
        lista_id = [x.id for x in lista_to_do]
        for id in range(1, len(lista_to_do) + 2):
            if id not in lista_id:
                to_do = ToDo(id, assunto, descricao, prioridade, data_limite)
                break
        lista_to_do.append(to_do)
        # imprimir para add manual...
        # for todo in lista_to_do:
        #     print(f'ToDo({todo.id}, "{todo.assunto}", "{todo.descricao}", {todo.prioridade}, "{todo.data_limite}")')
        return render(request, "todo.html", {"lista_to_do": lista_to_do})
    else:
        return render(request, "todo.html", {"lista_to_do": lista_to_do})


def excluir(request, id):
    for todo in lista_to_do:
        if int(todo.id) == int(id):
            lista_to_do.remove(todo)
            return render(request, "todos.html", {"lista_to_do": lista_to_do})
    return render(request, "todos.html", {"lista_to_do": lista_to_do})


def atualizar(request, id):
    for todo in lista_to_do:
        if int(todo.id) == int(id):
            return render(request, "todo.html", {"lista_to_do": lista_to_do, "todo_atualizar": todo})
    return render(request, "todo.html", {"lista_to_do": lista_to_do})
