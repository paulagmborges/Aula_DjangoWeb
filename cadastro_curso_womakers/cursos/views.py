from django.shortcuts import render
from cursos.forms import CursoForm
# Create your views here.

def criar_curso(request):
    if request.method == 'POST':
        form = CursoForm(request.POST)
        if form.is_valid():
            form.save()
            sucesso = True
        else:
            sucesso = False
    else:
        form = CursoForm()
        sucesso = False

    contexto ={
        'form': form,
        'sucesso': sucesso
    }
    return render(request, 'criar_curso.html', contexto)
