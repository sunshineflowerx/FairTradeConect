from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from .models import Perfil, Produto, Carrinho, Mensagem
import json

def index(request):
    categoria = request.GET.get('categoria', 'todas')
    pesquisa = request.GET.get('pesquisa', '')
    
    produtos = Produto.objects.all()
    
    if categoria != 'todas':
        produtos = produtos.filter(categoria=categoria)
    
    if pesquisa:
        produtos = produtos.filter(nome__icontains=pesquisa) | produtos.filter(descricao__icontains=pesquisa)
    
    categorias = [
        ('todas', 'Todas Categorias'),
        ('verduras', 'Verduras, folhas e ervas'),
        ('legumes', 'Legumes Orgânicos'),
        ('frutas', 'Frutas Orgânicas'),
        ('condimentos', 'Condimento & Tempero regional'),
        ('mercearia', 'Mercearia Orgânica'),
    ]
    
    context = {
        'produtos': produtos,
        'categorias': categorias,
        'categoria_selecionada': categoria,
        'pesquisa': pesquisa
    }
    return render(request, 'comerciojusto/index.html', context)

def login_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        senha = request.POST.get('senha')
        user = authenticate(username=email, password=senha)
        if user:
            login(request, user)
            return redirect('pos_login')
        return render(request, 'comerciojusto/login.html', {'erro': 'Credenciais inválidas'})
    return render(request, 'comerciojusto/login.html')

def cadastro_view(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')
        email = request.POST.get('email')
        senha = request.POST.get('senha')
        tipo = request.POST.get('tipo')

        if User.objects.filter(username=email).exists():
            return render(request, 'comerciojusto/cadastro.html', {'erro': 'Usuário já existe'})

        user = User.objects.create_user(username=email, email=email, password=senha, first_name=nome)
        Perfil.objects.create(user=user, tipo=tipo)
        return redirect('login')
    return render(request, 'comerciojusto/cadastro.html')

def logout_view(request):
    logout(request)
    return redirect('index')

@login_required(login_url='login')
def pos_login(request):
    perfil = Perfil.objects.get(user=request.user)
    if perfil.tipo == 'produtor':
        return redirect('area_produtor')
    elif perfil.tipo == 'empresa':
        return redirect('area_empresa')

@login_required(login_url='login')
def area_produtor(request):
    return render(request, 'comerciojusto/area_produtor.html')

@login_required(login_url='login')
def area_empresa(request):
    produtos = Produto.objects.all()
    return render(request, 'comerciojusto/area_empresa.html', {'produtos': produtos})


def detalhes_produto(request, id_produto):
    produto = get_object_or_404(Produto, id_produto=id_produto)
    produtor_info = produto.produtor
    
    context = {
        'produto': produto,
        'produtor_info': produtor_info,
    }
    return render(request, 'comerciojusto/detalhes_produto.html', context)


@login_required(login_url='login')
def meu_perfil(request):
    perfil = Perfil.objects.get(user=request.user)
    
    if perfil.tipo == 'produtor':
        produtos = Produto.objects.filter(produtor__id_produtor=1)
    else:
        produtos = None
    
    if request.method == 'POST':
        perfil.descricao = request.POST.get('descricao', perfil.descricao)
        perfil.noticia = request.POST.get('noticia', perfil.noticia)
        perfil.contato_adicional = request.POST.get('contato', perfil.contato_adicional)
        
        if 'logo' in request.FILES:
            perfil.logo = request.FILES['logo']
        
        perfil.save()
        return redirect('meu_perfil')
    
    context = {
        'perfil': perfil,
        'produtos': produtos,
    }
    return render(request, 'comerciojusto/meu_perfil.html', context)


@login_required(login_url='login')
def caixa_entrada(request):
    mensagens = Mensagem.objects.filter(destinatario=request.user).order_by('-criada_em')
    nao_lidas = mensagens.filter(lida=False).count()
    
    context = {
        'mensagens': mensagens,
        'nao_lidas': nao_lidas,
    }
    return render(request, 'comerciojusto/caixa_entrada.html', context)


@require_POST
def adicionar_carrinho(request):
    produto_id = request.POST.get('produto_id')
    quantidade = int(request.POST.get('quantidade', 1))
    
    try:
        produto = Produto.objects.get(id_produto=produto_id)
    except Produto.DoesNotExist:
        return JsonResponse({'success': False, 'message': 'Produto não encontrado'})
    
    if request.user.is_authenticated:
        carrinho, created = Carrinho.objects.get_or_create(usuario=request.user)
    else:
        sessao_id = request.session.session_key
        if not sessao_id:
            request.session.create()
            sessao_id = request.session.session_key
        
        carrinho, created = Carrinho.objects.get_or_create(sessao_id=sessao_id)
    
    itens = carrinho.itens or {}
    
    if str(produto_id) in itens:
        itens[str(produto_id)]['quantidade'] += quantidade
    else:
        itens[str(produto_id)] = {
            'quantidade': quantidade,
            'preco': str(produto.preco),
            'nome': produto.nome,
        }
    
    carrinho.itens = itens
    carrinho.rascunho_json = itens
    carrinho.save()
    
    request.session['carrinho_itens'] = len(itens)
    
    return JsonResponse({'success': True, 'message': 'Produto adicionado ao carrinho'})


@login_required(login_url='login')
def visualizar_carrinho(request):
    if request.user.is_authenticated:
        carrinho = Carrinho.objects.filter(usuario=request.user).first()
    else:
        sessao_id = request.session.session_key
        carrinho = Carrinho.objects.filter(sessao_id=sessao_id).first()
    
    itens = []
    total = 0
    
    if carrinho and carrinho.itens:
        for produto_id, info in carrinho.itens.items():
            try:
                produto = Produto.objects.get(id_produto=produto_id)
                subtotal = float(info['preco']) * info['quantidade']
                itens.append({
                    'produto': produto,
                    'quantidade': info['quantidade'],
                    'subtotal': subtotal,
                })
                total += subtotal
            except Produto.DoesNotExist:
                pass
    
    context = {
        'itens': itens,
        'total': total,
        'carrinho': carrinho,
    }
    return render(request, 'comerciojusto/carrinho.html', context)


