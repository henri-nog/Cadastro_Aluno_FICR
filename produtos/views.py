from django.shortcuts import render, redirect, get_object_or_404
from .models import Produto, Categoria, Pedido
from django.utils.timezone import now

from .models import Produto, Categoria

# Listagem de todos os produtos
def listar_produto(request):
    produtos = Produto.objects.all()
    return render(request, 'produtos/listar.html', {'produtos': produtos})


# Cadastrar novo produto
def adicionar_produto(request):
    if request.method == 'POST':
        nome = request.POST['nome']
        descricao = request.POST['descricao']
        preco = request.POST['preco']
        disponibilidade = 'disponibilidade' in request.POST  
        foto = request.FILES['foto'] if 'foto' in request.FILES else None # Faz uma requisição pela foto, se não tiver, atribui como 'None'

        Produto.objects.create(
            nome=nome,
            descricao=descricao,
            preco=preco,
            disponibilidade=disponibilidade,
            foto=foto
        )

        return redirect('listar_produto')

    return render(request, 'produtos/adicionar.html')


# Editar produto existente
def editar_produto(request, id):
    produto = get_object_or_404(Produto, id=id)

    if request.method == 'POST':
        produto.nome = request.POST['nome']
        produto.descricao = request.POST['descricao']
        produto.preco = request.POST['preco']
        produto.disponibilidade = 'disponibilidade' in request.POST

        if 'foto' in request.FILES: 
            produto.foto = request.FILES['foto']

        produto.save()
        return redirect('listar_produto')

    return render(request, 'produtos/editar.html', {'produto': produto})


# Excluir produto
def excluir_produto(request, id):
    produto = get_object_or_404(Produto, id=id)
    produto.delete()
    return redirect('listar_produto')


def listar_categorias(request):
    categorias = Categoria.objects.all()
    return render(request, 'categorias/listar.html', {'categorias': categorias})

def adicionar_categoria(request):
    if request.method == 'POST':
        nome = request.POST['nome']
        Categoria.objects.create(nome=nome)
        return redirect('listar_categorias')
    return render(request, 'categorias/adicionar.html')

def editar_categoria(request, id):
    categoria = get_object_or_404(Categoria, id=id)
    if request.method == 'POST':
        categoria.nome = request.POST['nome']
        categoria.save()
        return redirect('listar_categorias')
    return render(request, 'categorias/editar.html')

def excluir_categoria(request, id):
    categoria = get_object_or_404(Categoria, id=id)
    categoria.delete()
    return redirect('listar_categorias')

def listar_pedidos(request):
    pedidos = Pedido.objects.all()
    return render(request, 'pedidos/listar.html', {'pedidos': pedidos})


def adicionar_pedido(request):
    produtos = Produto.objects.all()

    if request.method == "POST":
        comprador = request.POST.get("comprador")
        produto_id = request.POST.get("produto")
        quantidade = int(request.POST.get("quantidade", 1))

        produto = get_object_or_404(Produto, id=produto_id)

        pedido = Pedido.objects.create(
            comprador=comprador,
            produto=produto,
            quantidade=quantidade
        )
        
        return redirect('listar_pedidos')

    return render(request, 'pedidos/adicionar.html', {'produtos': produtos})


def editar_pedido(request, id):
    pedido = get_object_or_404(Pedido, id=id)

    if request.method == 'POST':
        pedido.status = request.POST['status']
        pedido.save()
        return redirect('listar_pedidos')

    return render(request, 'pedidos/editar.html', {'pedido': pedido})


def excluir_pedido(request, id):
    pedido = get_object_or_404(Pedido, id=id)
    pedido.delete()
    return redirect('listar_pedidos')




