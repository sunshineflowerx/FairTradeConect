# 🌾 Fair Trade Connect - Sistema de Comércio Justo

## 📋 Descrição

**Fair Trade Connect** é uma plataforma web completa que conecta produtores agrícolas locais com empresas comprometidas com o comércio justo e sustentável.

### Principais Funcionalidades:
- 🔍 Busca e filtro de produtos por categoria
- 🛒 Carrinho de compras com modo anônimo
- 💾 Sistema de rascunho automático
- 👤 Perfis personalizáveis para produtores/empresas
- 📬 Sistema de mensagens
- 📦 Detalhes completos de produtos
- 💳 Suporte a múltiplos métodos de pagamento

---

## ✨ O que foi Implementado

### 1. Página Inicial Redesenhada
- ✅ Barra de pesquisa **fixa no topo**
- ✅ Ícone de **carrinho com badge** de quantidade
- ✅ **6 categorias de produtos** com filtros interativos
- ✅ Grid responsivo de produtos

### 2. Carrinho Inteligente
- ✅ Funciona **sem login** (guest checkout)
- ✅ Sistema de **rascunho automático** no localStorage
- ✅ **Notificação de restauração**: "Detectamos um rascunho não salvo. Deseja restaurar?"
- ✅ Salva quantidade, preço e nome de cada item

### 3. Interface Dinâmica
- ✅ **Antes do login**: Botões "Login" e "Cadastro"
- ✅ **Depois do login**: "Meu Perfil" e "Caixa de Entrada"
- ✅ **Navbar inteligente** que muda conforme autenticação

### 4. Página de Perfil (5️⃣)
- ✅ **Upload de logo/avatar** circular
- ✅ **Editar descrição** do produtor/empresa
- ✅ **Publicar notícias** e atualizações
- ✅ **Contato adicional** (redes sociais, website, etc)
- ✅ **Lista de produtos** para produtores
- ✅ **Salvar alterações** com feedback visual

### 5. Página de Produto
- ✅ **Imagem grande** do produto
- ✅ **Informações completas**: nome, categoria, preço, descrição
- ✅ **Seletor de quantidade** intuitivo
- ✅ **Métodos de pagamento**: PIX (padrão), Crédito, Débito
- ✅ **Dados do produtor**: logo, nome, descrição, contatos
- ✅ **Botão de ação**: Adicionar ao Carrinho

### 6. Caixa de Entrada (Bônus)
- ✅ **Lista de mensagens** com remetente, assunto, data
- ✅ **Status de leitura** (badge vermelho)
- ✅ **Preview do conteúdo**
- ✅ **Contador de não lidas**

---

## 🚀 Como Iniciar

### Pré-requisitos
- Python 3.8+
- pip (gerenciador de pacotes)

### Instalação Rápida

```bash
# 1. Navegar para o diretório
cd C:\Users\barau\Desktop\cursopy\projintegrador.py\django

# 2. Criar ambiente virtual (opcional mas recomendado)
python -m venv venv
venv\Scripts\activate

# 3. Instalar dependências
pip install -r requirements.txt

# 4. Aplicar migrações
python manage.py migrate

# 5. Criar super usuário (admin)
python manage.py createsuperuser
# Preencha: username, email, password, confirmação

# 6. Executar servidor
python manage.py runserver

# 7. Acessar no navegador
# Homepage: http://localhost:8000/
# Admin: http://localhost:8000/admin/
```

---

## 📱 Páginas e Rotas

| URL | Descrição | Autenticação |
|-----|-----------|--------------|
| `/` | Homepage com produtos | Público |
| `/produto/<id>/` | Detalhes do produto | Público |
| `/carrinho/` | Visualizar carrinho | Público |
| `/carrinho/adicionar/` | Adicionar ao carrinho | POST |
| `/login/` | Fazer login | Público |
| `/cadastro/` | Criar conta | Público |
| `/logout/` | Sair | Requer login |
| `/meu-perfil/` | Editar perfil | Requer login |
| `/caixa-entrada/` | Ver mensagens | Requer login |
| `/area/produtor/` | Área produtor | Requer login |
| `/area/empresa/` | Área empresa | Requer login |
| `/admin/` | Painel de administração | Requer login + admin |

---

## 🎯 Fluxo do Usuário

### 1. Novo Usuário
```
Homepage → Explora Produtos → Cadastro → Login → Compras
```

### 2. Comprador (Sem Login)
```
Homepage → Pesquisa Produto → Adiciona ao Carrinho → 
Vê Aviso de Login → Faz Login → Checkout
```

### 3. Produtor/Empresa
```
Login → Meu Perfil → Edita Informações → Upload de Logo →
Visualiza seus Produtos
```

---

## 📚 Documentação Incluída

### 1. **ALTERACOES.md**
Resumo detalhado de todas as 6 alterações implementadas

### 2. **GUIA_USO.md**
Manual completo para usuários finais

### 3. **TESTES.md**
Checklist completo de testes para validação

### 4. **DOCUMENTACAO_TECNICA.md**
Documentação técnica: modelos, views, URLs, migrações

---

## 🏗️ Arquitetura

```
Frontend (HTML/CSS/JavaScript)
         ↓
Django Framework
         ↓
SQLite Database
         ↓
Media Files (Imagens)
```

### Principais Tecnologias
- **Backend**: Django 6.0
- **Frontend**: HTML5, CSS3, Bootstrap 5, JavaScript
- **Banco de Dados**: SQLite (desenvolvimento), PostgreSQL (produção recomendada)
- **Uploads**: Pillow para processamento de imagens

---

## 🔐 Segurança

- ✅ Autenticação via Django User
- ✅ Proteção CSRF em formulários
- ✅ Senhas criptografadas
- ✅ Sessões seguras
- ✅ Permissões granulares

---

## 📊 Dados

### Modelos (7 no total)
1. **User** (Django built-in) - Autenticação
2. **Perfil** - Info do usuário (expandido)
3. **Produtor** - Dados do produtor
4. **Empresa** - Dados da empresa
5. **Produto** - Produtos à venda (modificado)
6. **Carrinho** - Carrinho de compras (novo)
7. **Mensagem** - Comunicação entre usuários (novo)

### Mais modelos:
- Documento, Administrador, Certificacao, AnuncioMarketplace

---

## 🎨 Design

- **Paleta de Cores**: Verde ecológico (#7a9d3d, #5a7a2f)
- **Tipografia**: Segoe UI (moderna e legível)
- **Responsive**: Mobile-first com Bootstrap
- **Icons**: Font Awesome 6.4

---

## 💾 Bancos de Dados

### Estrutura do Carrinho (JSONField)
```json
{
    "1": {"quantidade": 2, "preco": "12.90", "nome": "Cenoura Orgânica"},
    "2": {"quantidade": 1, "preco": "45.00", "nome": "Café Premium"}
}
```

### Rascunho (LocalStorage)
Salvo no navegador para restauração automática

---

## 🚀 Próximas Funcionalidades

- [ ] Sistema de pagamento integrado (Stripe/PayPal)
- [ ] Visualização de detalhes de mensagens
- [ ] Envio de mensagens entre usuários
- [ ] Reviews/avaliações de produtos
- [ ] Histórico de compras
- [ ] Notificações em tempo real
- [ ] Dashboard de vendas para produtores
- [ ] Cupons e promoções
- [ ] Rastreamento de pedidos

---

## 🐛 Troubleshooting

### "Erro ao fazer upload de imagem"
```
Solução: Verificar se a pasta "media/" existe
Se não existir, Django criará automaticamente no primeiro upload
```

### "Carrinho não funciona sem login"
```
Solução: Verificar se SESSION_ENGINE está configurado em settings.py
Django usa sessões para salvar carrinhos anônimos
```

### "Migrations não aplicam"
```
Solução: 
python manage.py makemigrations
python manage.py migrate --verbosity=2
```

---

## 📞 Suporte

Para dúvidas sobre funcionalidades:
1. Consulte **GUIA_USO.md**
2. Consulte **DOCUMENTACAO_TECNICA.md**
3. Verifique **TESTES.md** para validação

---

## 📄 Licença

Projeto educacional para aprendizado de Django

---

## 👥 Autor

Desenvolvido como sistema completo de e-commerce Fair Trade

---

## ✅ Checklist de Implementação

- ✅ 1. Produtos com categorias e barra de pesquisa
- ✅ 2. Carrinho com guest checkout
- ✅ 3. Sistema de rascunho automático
- ✅ 4. Interface dinâmica (login/meu perfil)
- ✅ 5. Página de perfil com logo e edição
- ✅ 6. Página de detalhes do produto
- ✅ 7. Caixa de entrada (bônus)
- ✅ 8. Migrações do banco de dados
- ✅ 9. Documentação completa
- ✅ 10. Testes e validação

---

**🎉 Sistema pronto para usar! Bom desenvolvimento!**

---

### 📖 Comece por:
1. Ler [GUIA_USO.md](GUIA_USO.md)
2. Executar servidor: `python manage.py runserver`
3. Criar dados de teste no admin: `http://localhost:8000/admin/`
4. Testar homepage: `http://localhost:8000/`

Divirta-se! 🚀
