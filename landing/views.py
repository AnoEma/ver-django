from django.shortcuts import render
def mostrar_index(request):
    nome = 'Flavia'
    lista_compras = ['desenhar', 'chiclete', 'mexer_celular']
    return render(request, 'index.html', {'item' : nome, 'lista' : lista_compras})

def mostrar_sobre(request):
    return render(request, 'sobre.html')