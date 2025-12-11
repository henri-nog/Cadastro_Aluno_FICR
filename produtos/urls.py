from django.urls import path
from . import views

urlpatterns = [

    # home 
    path("", views.home, name="home"),

    # produtos
    path("produtos/", views.listar_produto, name="listar_produto"),
    path("produtos/adicionar/", views.adicionar_produto, name="adicionar_produto"),
    path("produtos/editar/<int:id>/", views.editar_produto, name="editar_produto"),
    path("produtos/excluir/<int:id>/", views.excluir_produto, name="excluir_produto"),
    path("produtos/<int:id>/", views.detalhes_produto, name="detalhes_produto"),

    # categorias
    path("categorias/", views.listar_categorias, name="listar_categorias"),
    path("categorias/adicionar/", views.adicionar_categoria, name="adicionar_categoria"),
    path("categorias/editar/<int:id>/", views.editar_categoria, name="editar_categoria"),
    path("categorias/excluir/<int:id>/", views.excluir_categoria, name="excluir_categoria"),

    # pedidos
    path("pedidos/", views.listar_pedidos, name="listar_pedidos"),
    path("pedidos/adicionar/", views.adicionar_pedido, name="adicionar_pedido"),
    path("pedidos/editar/<int:id>/", views.editar_pedido, name="editar_pedido"),
    path("pedidos/excluir/<int:id>/", views.excluir_pedido, name="excluir_pedido"),
    path("pedidos/<int:id>/", views.detalhes_pedido, name="detalhes_pedido"),
]
