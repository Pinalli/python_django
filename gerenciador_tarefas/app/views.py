from django.shortcuts import render, redirect
from .forms import TarefaForm
from .entidades.tarefa import Tarefa
from .services import tarefa_service


def listar_tarefas(request):
    nome_tarefa = "Estudar Python e Django"
    return render(request, 'tarefas/listar_tarefas.html', {"nome_tarefa": nome_tarefa})


def cadastrar_tarefa(request):
    if request.method == 'POST':
        form_tarefa = TarefaForm(request.POST)
        if form_tarefa.is_valid():
            titulo = form_tarefa.cleaned_data["titulo"]
            descricao = form_tarefa.cleaned_data["descricao"]
            data_expiracao = form_tarefa.cleaned_data["data_expiracao"]
            prioridade = form_tarefa.cleaned_data["prioridade"]

            tarefa_nova = Tarefa(titulo=titulo, descricao=descricao, data_expiracao=data_expiracao,
                                 prioridade=prioridade)
            tarefa_service.cadastrar_tarefa(tarefa_nova)
            return redirect('listar_tarefas')
    else:
        form_tarefa = TarefaForm()
    return render(request, 'tarefas/form_tarefa.html', {"form_tarefa": form_tarefa})
