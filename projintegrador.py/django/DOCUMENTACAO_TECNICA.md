# 🔧 Documentação Técnica - Fair Trade Connect

## 📊 Arquitetura do Projeto

```
django/
├── manage.py                          # Gerenciador Django
├── requirements.txt                   # Dependências (atualizado com Pillow)
├── db.sqlite3                         # Banco de dados
├── media/                             # Upload de imagens (criado automaticamente)
│   ├── perfis/logos/                  # Logos de perfis
│   └── produtos/                      # Imagens de produtos
│
├── webapp/                            # Configurações do projeto
│   ├── settings.py                    # Configurações (atualizado)
│   ├── urls.py                        # URLs principais (atualizado)
│   ├── wsgi.py
│   └── asgi.py
│
└── comerciojusto/                     # Aplicação principal
    ├── models.py                      # Modelos (6 novos modelos)
    ├── views.py                       # Views (7 novas views)
    ├── urls.py                        # URLs app (7 novas rotas)
    ├── admin.py                       # Admin panel (atualizado)
    ├── apps.py
    ├── tests.py
    ├── migrations/                    # Migrações banco de dados
    │   ├── 0001_initial.py
    │   ├── 0002_remove_gestor_operador.py
    │   └── 0003_*.py                  # Novos modelos e campos
    │
    └── templates/comerciojusto/       # Templates HTML
        ├── index.html                 # Homepage (novo design)
        ├── detalhes_produto.html      # Detalhes do produto
        ├── carrinho.html              # Visualizar carrinho
        ├── meu_perfil.html            # Perfil do usuário
        ├── caixa_entrada.html         # Mensagens
        ├── login.html                 # Login
        ├── cadastro.html              # Cadastro
        ├── area_produtor.html         # Área do produtor
        └── area_empresa.html          # Área da empresa
```

---

## 📦 Modelos de Dados

### 1. User (Django built-in)
```python
class User:
    username          # Email
    email             # Email
    password          # Hasheada
    first_name        # Nome completo
    is_authenticated  # Boolean
```

### 2. Perfil (NOVO - Expandido)
```python
class Perfil(models.Model):
    user = OneToOneField(User)        # Link com usuário Django
    tipo = CharField(choices=[        # Tipo de conta
        ('produtor', 'Produtor'),
        ('empresa', 'Empresa'),
    ])
    logo = ImageField()               # Logo do perfil (NOVO)
    descricao = TextField()           # Sobre (NOVO)
    noticia = TextField()             # Novidades (NOVO)
    contato_adicional = CharField()   # Redes sociais, etc (NOVO)
```

### 3. Produtor (Não Modificado)
```python
class Produtor(models.Model):
    id_produtor = AutoField(primary_key=True)
    nome = CharField()
    cpf_cnpj = CharField(unique=True)
    email = EmailField(unique=True)
    senha = CharField()
    telefone = CharField(optional)
```

### 4. Empresa (Não Modificado)
```python
class Empresa(models.Model):
    id_empresa = AutoField(primary_key=True)
    nome = CharField()
    cnpj = CharField(unique=True)
    email = EmailField(unique=True)
    senha = CharField()
    telefone = CharField(optional)
```

### 5. Produto (MODIFICADO)
```python
class Produto(models.Model):
    CATEGORIA_CHOICES = [              # NOVO - Categorias
        ('todas', 'Todas Categorias'),
        ('verduras', 'Verduras, folhas e ervas'),
        ('legumes', 'Legumes Orgânicos'),
        ('frutas', 'Frutas Orgânicas'),
        ('condimentos', 'Condimento & Tempero regional'),
        ('mercearia', 'Mercearia Orgânica'),
    ]
    
    id_produto = AutoField(primary_key=True)
    nome = CharField()
    descricao = TextField(optional)
    categoria = CharField(choices=CATEGORIA_CHOICES)  # NOVO
    preco = DecimalField()                            # NOVO
    imagem = ImageField(optional)                     # NOVO
    data_producao = DateField(optional)
    status_logistica = CharField(optional)
    produtor = ForeignKey(Produtor)
```

### 6. Carrinho (NOVO)
```python
class Carrinho(models.Model):
    id_carrinho = AutoField(primary_key=True)
    usuario = OneToOneField(User, null=True, blank=True)  # Logado
    sessao_id = CharField(null=True, blank=True)          # Anônimo
    itens = JSONField()                                   # {produto_id: {qty, preco, nome}}
    rascunho_json = JSONField()                           # Backup
    criado_em = DateTimeField(auto_now_add=True)
    atualizado_em = DateTimeField(auto_now=True)
```

Estrutura do JSONField `itens`:
```json
{
    "1": {
        "quantidade": 2,
        "preco": "12.90",
        "nome": "Cenoura Orgânica"
    },
    "2": {
        "quantidade": 1,
        "preco": "45.00",
        "nome": "Café Premium"
    }
}
```

### 7. Mensagem (NOVO)
```python
class Mensagem(models.Model):
    id_mensagem = AutoField(primary_key=True)
    remetente = ForeignKey(User, related_name='mensagens_enviadas')
    destinatario = ForeignKey(User, related_name='mensagens_recebidas')
    assunto = CharField()
    corpo = TextField()
    lida = BooleanField(default=False)
    criada_em = DateTimeField(auto_now_add=True)
```

### Modelos Inalterados
- Documento
- Administrador
- Certificacao
- AnuncioMarketplace

---

## 🔀 Views (Funções)

### 1. `index(request)` - MODIFICADA
```python
def index(request):
    categoria = request.GET.get('categoria', 'todas')
    pesquisa = request.GET.get('pesquisa', '')
    
    produtos = Produto.objects.all()
    
    # Filtrar por categoria
    if categoria != 'todas':
        produtos = produtos.filter(categoria=categoria)
    
    # Filtrar por pesquisa (nome ou descrição)
    if pesquisa:
        produtos = produtos.filter(nome__icontains=pesquisa) | \
                  produtos.filter(descricao__icontains=pesquisa)
    
    context = {
        'produtos': produtos,
        'categorias': [...],
        'categoria_selecionada': categoria,
        'pesquisa': pesquisa
    }
    return render(request, 'comerciojusto/index.html', context)
```

### 2. `detalhes_produto(request, id_produto)` - NOVO
```python
def detalhes_produto(request, id_produto):
    produto = get_object_or_404(Produto, id_produto=id_produto)
    produtor_info = produto.produtor
    
    context = {
        'produto': produto,
        'produtor_info': produtor_info,
    }
    return render(request, 'comerciojusto/detalhes_produto.html', context)
```

### 3. `adicionar_carrinho(request)` - NOVO
```python
@require_POST
def adicionar_carrinho(request):
    produto_id = request.POST.get('produto_id')
    quantidade = int(request.POST.get('quantidade', 1))
    
    try:
        produto = Produto.objects.get(id_produto=produto_id)
    except Produto.DoesNotExist:
        return JsonResponse({'success': False, 'message': 'Produto não encontrado'})
    
    # Se logado, usar carrinho do usuário; senão usar sessão
    if request.user.is_authenticated:
        carrinho, created = Carrinho.objects.get_or_create(usuario=request.user)
    else:
        sessao_id = request.session.session_key
        if not sessao_id:
            request.session.create()
            sessao_id = request.session.session_key
        
        carrinho, created = Carrinho.objects.get_or_create(sessao_id=sessao_id)
    
    # Adicionar item ao carrinho
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
    
    # Atualizar session para badge do carrinho
    request.session['carrinho_itens'] = len(itens)
    
    return JsonResponse({'success': True, 'message': 'Produto adicionado ao carrinho'})
```

### 4. `visualizar_carrinho(request)` - NOVO
```python
@login_required(login_url='login')
def visualizar_carrinho(request):
    # Buscar carrinho do usuário ou sessão
    if request.user.is_authenticated:
        carrinho = Carrinho.objects.filter(usuario=request.user).first()
    else:
        sessao_id = request.session.session_key
        carrinho = Carrinho.objects.filter(sessao_id=sessao_id).first()
    
    # Processar itens
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
```

### 5. `meu_perfil(request)` - NOVO
```python
@login_required(login_url='login')
def meu_perfil(request):
    perfil = Perfil.objects.get(user=request.user)
    
    # Se produtor, mostrar produtos
    if perfil.tipo == 'produtor':
        produtos = Produto.objects.filter(produtor__id_produtor=1)
    else:
        produtos = None
    
    if request.method == 'POST':
        # Atualizar campos
        perfil.descricao = request.POST.get('descricao', perfil.descricao)
        perfil.noticia = request.POST.get('noticia', perfil.noticia)
        perfil.contato_adicional = request.POST.get('contato', perfil.contato_adicional)
        
        # Fazer upload de logo se enviado
        if 'logo' in request.FILES:
            perfil.logo = request.FILES['logo']
        
        perfil.save()
        return redirect('meu_perfil')
    
    context = {
        'perfil': perfil,
        'produtos': produtos,
    }
    return render(request, 'comerciojusto/meu_perfil.html', context)
```

### 6. `caixa_entrada(request)` - NOVO
```python
@login_required(login_url='login')
def caixa_entrada(request):
    mensagens = Mensagem.objects.filter(destinatario=request.user).order_by('-criada_em')
    nao_lidas = mensagens.filter(lida=False).count()
    
    context = {
        'mensagens': mensagens,
        'nao_lidas': nao_lidas,
    }
    return render(request, 'comerciojusto/caixa_entrada.html', context)
```

---

## 🌐 URLs

### Rotas Novas

```python
urlpatterns = [
    # Existentes
    path('', views.index, name='index'),
    path('login/', views.login_view, name='login'),
    path('cadastro/', views.cadastro_view, name='cadastro'),
    path('logout/', views.logout_view, name='logout'),
    path('pos-login/', views.pos_login, name='pos_login'),
    path('area/produtor/', views.area_produtor, name='area_produtor'),
    path('area/empresa/', views.area_empresa, name='area_empresa'),
    
    # NOVAS
    path('produto/<int:id_produto>/', views.detalhes_produto, name='detalhes_produto'),
    path('meu-perfil/', views.meu_perfil, name='meu_perfil'),
    path('caixa-entrada/', views.caixa_entrada, name='caixa_entrada'),
    path('carrinho/adicionar/', views.adicionar_carrinho, name='adicionar_carrinho'),
    path('carrinho/', views.visualizar_carrinho, name='visualizar_carrinho'),
]
```

---

## 🗄️ Migrações

### Migration 0001_initial
- Criação de todas as tabelas iniciais

### Migration 0002_remove_gestor_operador
- Remoção de 'gestor' e 'operador' das choices de Perfil

### Migration 0003_*.py (NOVA)
```
+ Add field contato_adicional to perfil
+ Add field descricao to perfil
+ Add field logo to perfil
+ Add field noticia to perfil
+ Add field imagem to produto
+ Add field preco to produto
~ Alter field categoria on produto
+ Create model Carrinho
+ Create model Mensagem
```

---

## 🎨 Templates

### Novos Templates
1. **index.html** (reescrito)
   - Navbar sticky com busca
   - Seção de categorias
   - Grid de produtos com carrinho
   - Sistema de rascunho

2. **detalhes_produto.html**
   - Imagem grande
   - Info do produtor
   - Seletor de quantidade
   - Métodos de pagamento

3. **carrinho.html**
   - Lista de itens
   - Cálculo de total
   - Botão de checkout
   - Aviso de login se necessário

4. **meu_perfil.html**
   - Upload de logo
   - Edição de descrição/notícias
   - Lista de produtos (produtores)
   - Informações de contato

5. **caixa_entrada.html**
   - Lista de mensagens
   - Status lida/não lida
   - Preview e data/hora
   - Contador de não lidas

---

## 🔐 Autenticação

### Proteção de Rotas
```python
@login_required(login_url='login')
def meu_perfil(request):
    ...
```

### Verificação no Template
```django
{% if user.is_authenticated %}
    <!-- Mostrado para logados -->
{% else %}
    <!-- Mostrado para não logados -->
{% endif %}
```

---

## 💾 Bancos de Dados

### Estrutura JSON do Carrinho
```json
{
    "produto_id_1": {
        "quantidade": 2,
        "preco": "12.90",
        "nome": "Produto A"
    },
    "produto_id_2": {
        "quantidade": 1,
        "preco": "45.00",
        "nome": "Produto B"
    }
}
```

### LocalStorage (Navegador)
```javascript
localStorage.setItem('carrinho_rascunho', JSON.stringify({
    timestamp: "2026-01-17T10:30:00",
    itens: "carregado"
}))
```

---

## 📁 Media Files

### Estrutura de Uploads
```
media/
├── perfis/
│   └── logos/
│       ├── user_1_logo.jpg
│       ├── user_2_logo.png
│       └── ...
└── produtos/
    ├── produto_1.jpg
    ├── produto_2.png
    └── ...
```

### Configuração em settings.py
```python
MEDIA_URL = 'media/'
MEDIA_ROOT = BASE_DIR / 'media'
```

### Serving em urls.py (DEBUG=True)
```python
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
```

---

## 📦 Dependências

### Atualizadas
```
Django==6.0
Pillow==12.1.0  # Para ImageField
asgiref==3.11.0
sqlparse==0.5.5
tzdata==2025.3
```

---

## 🧪 Testando Localmente

```bash
# 1. Instalar dependências
pip install -r requirements.txt

# 2. Criar banco de dados
python manage.py migrate

# 3. Criar admin
python manage.py createsuperuser

# 4. Criar dados de teste (opcional)
# Adicione alguns produtos no admin

# 5. Rodar servidor
python manage.py runserver

# 6. Acessar
# http://localhost:8000/           (homepage)
# http://localhost:8000/admin/     (painel admin)
```

---

## 🚀 Deploy

Para produção:
1. Remover `DEBUG = True` em settings.py
2. Adicionar ALLOWED_HOSTS
3. Configurar SECRET_KEY segura
4. Usar banco PostgreSQL em vez de SQLite
5. Servir media files com CDN (AWS S3, etc)
6. Configurar email para notificações
7. Adicionar SSL/HTTPS
8. Usar Gunicorn + Nginx

---

## 📝 Notas Técnicas

- **JSONField**: Salva dicionário Python como JSON no banco
- **OneToOneField**: Garante relação 1:1 entre User e Perfil
- **ForeignKey**: Relaciona produtos com produtores
- **Session**: Armazena ID de sessão para carrinhos anônimos
- **LocalStorage**: Persiste rascunho no navegador (cliente)

---

## 🐛 Debugging

### Ver logs do Django
```bash
python manage.py runserver --verbosity=2
```

### Ver queries SQL
```python
from django.db import connection
print(connection.queries)  # Em DEBUG=True
```

### Testar views individualmente
```python
from django.test import Client
client = Client()
response = client.get('/')
print(response.status_code)
```

---

**Documentação Técnica Completa! 🎉**
