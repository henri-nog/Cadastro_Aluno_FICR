from django.shortcuts import render, redirect, get_object_or_404
from .models import Produto
# Create your views here.


# Listagem de todos os elementos da classe produtos
def listar_produto(request):
    produtos = Produto.objects.all()
    return render(request, 'produtos/listar.html', {'produto': produtos})


# Cadastrar itens da classe produtos
def adicionar_produto(request):
    if request.method == 'POST':
        nome = request.POST['nome']
        email = request.POST['email']
        idade = request.POST['idade']
        curso = request.POST['curso']
        Produto.objects.create(nome=nome, email=email, idade=idade, curso=curso)
        return redirect('listar_produto')
    return render(request, 'produtos/adicionar.html')


# Alterar itens da classe produtos
def editar_produto(request, id):
    produtos = get_object_or_404(Produto, id=id)
    if request.method == 'POST':
        produtos.nome = request.POST['nome']
        produtos.email = request.POST['email']
        produtos.idade = request.POST['idade']
        produtos.curso = request.POST['curso']
        produtos.save()
        return redirect('listar_produto')
    return render(request, 'produtos/editar.html')


# Excluir itens da classe produtos
def excluir_produto(request, id):
    produtos = get_object_or_404(Produto, id=id)
    produtos.delete()
    return redirect('listar_produto')
