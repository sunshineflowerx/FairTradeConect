# ✅ Checklist de Testes - Fair Trade Connect

## 🧪 Testes Básicos

### Homepage
- [ ] Navbar sticky aparece ao descer a página
- [ ] Barra de pesquisa funciona
- [ ] Ícone de carrinho é clicável
- [ ] Categorias aparecem com botões clicáveis
- [ ] Cards de produtos são responsivos

### Sem Login
- [ ] Vejo botões "Login" e "Cadastro" no navbar
- [ ] Posso clicar em um produto
- [ ] Posso adicionar ao carrinho sem login
- [ ] Badge do carrinho atualiza a quantidade
- [ ] Ao ir pro carrinho, vejo aviso de login necessário

### Com Login
- [ ] Navbar mostra "Meu Perfil" em vez de "Login"
- [ ] Botão "Cadastro" desaparece
- [ ] "Caixa de Entrada" aparece
- [ ] Botão "Sair" existe
- [ ] Ao clicar "Meu Perfil", vou para página de perfil
- [ ] Ao clicar "Caixa de Entrada", vou para caixa de entrada

---

## 🔍 Testes de Pesquisa e Filtros

### Pesquisa
- [ ] Digitar no campo de busca filtra produtos por nome
- [ ] Digitar filtra também por descrição
- [ ] Pesquisa funciona com maiúsculas e minúsculas
- [ ] Campo vazio mostra todos os produtos

### Categorias
- [ ] Clicar em "Todas Categorias" mostra todos os produtos
- [ ] Clicar em "Verduras..." filtra apenas verduras
- [ ] Clicar em "Legumes..." filtra apenas legumes
- [ ] Clicar em "Frutas..." filtra apenas frutas
- [ ] Clicar em "Condimentos..." filtra apenas condimentos
- [ ] Clicar em "Mercearia..." filtra apenas mercearia
- [ ] Botão ativo muda de cor (verde)
- [ ] Combinar pesquisa + categoria funciona

---

## 🛒 Testes do Carrinho

### Carrinho Anônimo (Sem Login)
- [ ] Adiciono produto, apareço no carrinho
- [ ] Quantidade correta aparece no badge
- [ ] Posso adicionar várias unidades
- [ ] Subtotal calcula corretamente
- [ ] Total soma todos os itens
- [ ] Ao fechar aba e reabrir, rascunho aparece
- [ ] Notificação de rascunho funciona
- [ ] Botão "Restaurar" traz itens de volta

### Carrinho Logado
- [ ] Adiciono produto, aparece no banco de dados
- [ ] Quantidade atualiza corretamente
- [ ] Ao sair e voltar, itens persistem
- [ ] Posso remover itens (em breve)
- [ ] Posso alterar quantidade (em breve)
- [ ] Subtotal e total calculam corretamente

### Checkout
- [ ] Usuário não logado vê aviso
- [ ] Usuários não logados podem clicar em Login/Cadastro
- [ ] Usuário logado vê "Prosseguir para Pagamento"
- [ ] Métodos de pagamento aparecem (PIX, Crédito, Débito)

---

## 👤 Testes de Autenticação

### Cadastro
- [ ] Campos obrigatórios validam
- [ ] Email único é verificado
- [ ] Senha mínima é aceita
- [ ] Tipo de conta (Produtor/Empresa) aparece
- [ ] Mensagem de sucesso aparece
- [ ] Redireciona para login

### Login
- [ ] Posso fazer login com email e senha
- [ ] Credenciais inválidas mostram erro
- [ ] Após login, vou para área pessoal
- [ ] Sessão persiste ao navegar

### Logout
- [ ] Clico em "Sair"
- [ ] Sessão é encerrada
- [ ] Vejo navbar com "Login" e "Cadastro" novamente
- [ ] Redireciona para home

---

## 👨‍💼 Testes de Perfil

### Editar Perfil
- [ ] Página carrega corretamente
- [ ] Logo é exibido (ou ícone padrão)
- [ ] Posso fazer upload de nova logo
- [ ] Campo de descrição está vazio ou preenchido
- [ ] Campo de notícias está vazio ou preenchido
- [ ] Campo de contato está vazio ou preenchido
- [ ] Botão "Salvar" funciona
- [ ] Dados salvos persistem ao recarregar

### Meus Produtos (Produtor)
- [ ] Seção aparece apenas para produtores
- [ ] Lista todos os produtos do produtor
- [ ] Cada produto mostra: nome, categoria, preço
- [ ] Grid é responsivo
- [ ] Não aparece para empresas

### Informações de Contato
- [ ] Email aparece corretamente
- [ ] Botão "Sair da Conta" está visível

---

## 📬 Testes de Caixa de Entrada

### Listagem
- [ ] Página carrega corretamente
- [ ] Mostra contador de mensagens
- [ ] Mostra contador de não lidas
- [ ] Cada mensagem mostra: avatar, remetente, assunto, preview, data/hora
- [ ] Mensagens não lidas têm fundo destacado
- [ ] Indicador de não lido (ponto vermelho) aparece

### Interação
- [ ] Clico em mensagem não faz nada ainda (funcionalidade em desenvolvimento)
- [ ] Caixa vazia mostra mensagem apropriada
- [ ] Link de voltar funciona

---

## 📦 Testes de Detalhes do Produto

### Layout
- [ ] Imagem grande aparece do lado esquerdo
- [ ] Informações aparecem do lado direito
- [ ] Link "Voltar para Produtos" funciona
- [ ] Layout responsivo em mobile

### Informações
- [ ] Nome do produto é exibido
- [ ] Preço é destacado em verde
- [ ] Categoria aparece como badge
- [ ] Descrição completa é mostrada
- [ ] Seletor de quantidade funciona
- [ ] Posso aumentar/diminuir quantidade

### Métodos de Pagamento
- [ ] Opção PIX aparece e está selecionada por padrão
- [ ] Opção Crédito aparece
- [ ] Opção Débito aparece
- [ ] Posso selecionar cada uma

### Botão Adicionar
- [ ] Usuário não logado vê mensagem de aviso
- [ ] Usuário logado pode clicar sem problemas
- [ ] Produto é adicionado ao carrinho
- [ ] Badge do carrinho atualiza

### Informações do Produtor
- [ ] Logo/avatar aparece (ou ícone padrão)
- [ ] Nome do produtor é exibido
- [ ] Tipo (Produtor/Empresa) aparece com emoji
- [ ] Descrição é mostrada (se preenchida)
- [ ] Notícias são mostradas (se preenchidas)
- [ ] Email aparece
- [ ] Telefone aparece
- [ ] Contato adicional aparece (se preenchido)
- [ ] Botão "Enviar Mensagem" aparece (em desenvolvimento)

---

## 📱 Testes de Responsividade

### Desktop (1920x1080)
- [ ] Todos os elementos visíveis
- [ ] Layout lado a lado (imagem + informações)
- [ ] Grid de produtos em 3 colunas

### Tablet (768px)
- [ ] Navbar collapsa (menu hamburger)
- [ ] Grid de produtos em 2 colunas
- [ ] Detalhes do produto em 2 colunas (responsivo)

### Mobile (360px)
- [ ] Navbar collapsa
- [ ] Barra de pesquisa acessível
- [ ] Grid de produtos em 1 coluna
- [ ] Detalhes do produto em 1 coluna
- [ ] Produtor info stacks bem
- [ ] Botões são clicáveis (não muito pequenos)

---

## 🔒 Testes de Segurança

### Autenticação
- [ ] Páginas protegidas redirecionam para login
- [ ] Não posso acessar `/meu-perfil/` sem login
- [ ] Não posso acessar `/caixa-entrada/` sem login
- [ ] Não posso acessar `/area/produtor/` sem login
- [ ] Logout realmente encerra a sessão

### Dados
- [ ] Não vejo dados de outros usuários
- [ ] Não posso editar perfil de outro
- [ ] Senhas não aparecem em place algum
- [ ] Carrinho de outro usuário não é acessível

### CSRF
- [ ] Formulários têm {% csrf_token %}
- [ ] Submissões sem token falham (desenvolvimento only)

---

## ⚡ Testes de Performance

### Carregamento
- [ ] Homepage carrega em < 2 segundos
- [ ] Pesquisa é instantânea
- [ ] Filtros são instantâneos
- [ ] Página de detalhes carrega rápido
- [ ] Imagens carregam corretamente

### Banco de Dados
- [ ] Carrinho salva corretamente
- [ ] Perfil salva corretamente
- [ ] Múltiplos usuários não interferem uns nos outros

---

## 🎨 Testes de UI/UX

### Cores e Fontes
- [ ] Verde primário é consistente
- [ ] Fonte é legível
- [ ] Contraste é adequado
- [ ] Ícones fazem sentido

### Navegação
- [ ] Menu é intuitivo
- [ ] Breadcrumb ajuda a voltar
- [ ] Links estão claramente identificados
- [ ] Botões são óbvios

### Feedback Visual
- [ ] Botões mudam ao hover
- [ ] Categoria selecionada fica verde
- [ ] Carrinho atualiza em tempo real
- [ ] Carregamento é suave (sem saltos)

---

## 📊 Testes de Dados

### Criar Usuário
- [ ] Produtor novo tem perfil vazio
- [ ] Empresa nova tem perfil vazio
- [ ] Ambos podem fazer upload de logo
- [ ] Dados são salvos no banco

### Criar Produto
- [ ] Deve ter nome, categoria, preço
- [ ] Imagem é opcional
- [ ] Ligado ao produtor correto
- [ ] Aparece no carrinho com dados corretos

### Criar Carrinho
- [ ] Usuário logado tem carrinho único
- [ ] Usuário anônimo usa sessão
- [ ] Itens são JSONField (estrutura flexível)
- [ ] Rascunho persiste no localStorage

---

## 🚀 Checklist Final

Antes de entregar:
- [ ] Todos os arquivos `.pyc` deletados
- [ ] Banco de dados migrado completamente
- [ ] Sem erros no `python manage.py check`
- [ ] README.md atualizado
- [ ] GUIA_USO.md completo
- [ ] Sem dados sensíveis em arquivos
- [ ] `.gitignore` inclui `db.sqlite3`, `media/`, `__pycache__/`
- [ ] `requirements.txt` atualizado com Pillow
- [ ] Servidor inicia sem erros
- [ ] Todas as rotas funcionam

---

## 📝 Notas

- Funcionalidade de envio de mensagens está em desenvolvimento
- Pagamento será integrado em fase 2
- Edição de itens do carrinho em fase 2
- Sistema de avaliações em fase 2

---

**Status**: ✅ Pronto para Testes!
