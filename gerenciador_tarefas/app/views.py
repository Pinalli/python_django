from django.shortcuts import render


def listar_tarefas(request):
    nome_tarefa = "Estudar Python e Django"
    return render(request, 'tarefas/listar_tarefas.html', {"nome_tarefa": nome_tarefa})
