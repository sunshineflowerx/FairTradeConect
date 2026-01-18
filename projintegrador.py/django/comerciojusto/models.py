from django.db import models
from django.contrib.auth.models import User
import json

class Perfil(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    tipo = models.CharField(max_length=20, choices=[
        ('produtor', 'Produtor'),
        ('empresa', 'Empresa'),
    ])
    logo = models.ImageField(upload_to='perfis/logos/', blank=True, null=True)
    descricao = models.TextField(blank=True, null=True)
    noticia = models.TextField(blank=True, null=True)
    contato_adicional = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return f"{self.user.username} - {self.tipo}"

class Produtor(models.Model):
    id_produtor = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=100)
    cpf_cnpj = models.CharField(max_length=20, unique=True)
    email = models.EmailField(max_length=150, unique=True)
    senha = models.CharField(max_length=255)
    telefone = models.CharField(max_length=30, blank=True, null=True)

    def __str__(self):
        return f"{self.nome} ({self.cpf_cnpj})"

    class Meta:
        db_table = 'produtor'
        
class Empresa(models.Model):
    id_empresa = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=100)
    cnpj = models.CharField(max_length=20, unique=True)
    email = models.EmailField(max_length=150, unique=True)
    senha = models.CharField(max_length=255)
    telefone = models.CharField(max_length=30, blank=True, null=True)

    def __str__(self):
        return self.nome

    class Meta:
        db_table = 'empresa'

class Produto(models.Model):
    CATEGORIA_CHOICES = [
        ('todas', 'Todas Categorias'),
        ('verduras', 'Verduras, folhas e ervas'),
        ('legumes', 'Legumes Orgânicos'),
        ('frutas', 'Frutas Orgânicas'),
        ('condimentos', 'Condimento & Tempero regional'),
        ('mercearia', 'Mercearia Orgânica'),
    ]
    
    id_produto = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=100)
    descricao = models.TextField(blank=True, null=True)
    categoria = models.CharField(max_length=50, choices=CATEGORIA_CHOICES, default='todas')
    preco = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    imagem = models.ImageField(upload_to='produtos/', blank=True, null=True)
    data_producao = models.DateField(blank=True, null=True)
    status_logistica = models.CharField(max_length=30, blank=True, null=True)
    produtor = models.ForeignKey(Produtor, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome

    class Meta:
        db_table = 'produto'

class Documento(models.Model):
    id_documento = models.AutoField(primary_key=True)
    tipo = models.CharField(max_length=50)
    arquivo = models.TextField(blank=True, null=True)
    status = models.CharField(max_length=20, blank=True, null=True)
    produtor = models.ForeignKey(Produtor, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.tipo} - {self.status}"

    class Meta:
        db_table = 'documento'

class Administrador(models.Model):
    id_adm = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=100)
    email = models.EmailField(max_length=150, unique=True)
    senha = models.CharField(max_length=255)

    def __str__(self):
        return self.nome

    class Meta:
        db_table = 'administrador'


class Certificacao(models.Model):
    id_certificacao = models.AutoField(primary_key=True)
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    administrador = models.ForeignKey(Administrador, on_delete=models.CASCADE)
    data_certificacao = models.DateField(blank=True, null=True)
    validade = models.DateField(blank=True, null=True)
    status = models.CharField(max_length=20, blank=True, null=True)

    def __str__(self):
        return f"Certificação {self.id_certificacao} - {self.status}"

    class Meta:
        db_table = 'certificacao'

class AnuncioMarketplace(models.Model):
    id_anuncio = models.AutoField(primary_key=True)
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    plataforma = models.CharField(max_length=100, blank=True, null=True)
    url = models.URLField(max_length=255, blank=True, null=True)
    data_publicacao = models.DateField(blank=True, null=True)
    status = models.CharField(max_length=20, blank=True, null=True)

    def __str__(self):
        return f"{self.plataforma} - {self.status}"

    class Meta:
        db_table = 'anuncio_marketplace'


class Carrinho(models.Model):
    id_carrinho = models.AutoField(primary_key=True)
    usuario = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    sessao_id = models.CharField(max_length=255, blank=True, null=True)
    itens = models.JSONField(default=dict)
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)
    rascunho_json = models.JSONField(default=dict, blank=True)

    def __str__(self):
        return f"Carrinho {self.id_carrinho}"

    class Meta:
        db_table = 'carrinho'


class Mensagem(models.Model):
    id_mensagem = models.AutoField(primary_key=True)
    remetente = models.ForeignKey(User, on_delete=models.CASCADE, related_name='mensagens_enviadas')
    destinatario = models.ForeignKey(User, on_delete=models.CASCADE, related_name='mensagens_recebidas')
    assunto = models.CharField(max_length=255)
    corpo = models.TextField()
    lida = models.BooleanField(default=False)
    criada_em = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"De: {self.remetente} Para: {self.destinatario}"

    class Meta:
        db_table = 'mensagem'


