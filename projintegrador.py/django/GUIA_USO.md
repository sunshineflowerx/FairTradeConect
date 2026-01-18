# 📖 Guia de Uso - Fair Trade Connect

## 🎯 Funcionalidades Principais

### 1️⃣ Página Inicial (Home)

#### O que você vê:
- **Navbar Sticky** com logo, barra de pesquisa, ícone de carrinho e menu
- **Hero Section** com mensagem de boas-vindas
- **Seção de Categorias** com filtros interativos
- **Grid de Produtos** com cards clicáveis

#### Como usar:
```
1. Digitar na barra de pesquisa para filtrar por nome/descrição
2. Clicar em uma categoria para filtrar
3. Clicar no card do produto para ver detalhes
4. Clicar em "Carrinho" para adicionar ao carrinho (sem necessidade de login!)
```

---

### 2️⃣ Página de Detalhes do Produto

#### Seções:
- **Imagem Grande** do produto
- **Informações**: nome, categoria, preço, descrição
- **Seletor de Quantidade**: escolha quantas unidades deseja
- **Métodos de Pagamento**: PIX, Crédito, Débito
- **Informações do Produtor**: logo, nome, tipo, descrição, contatos
- **Botão "Adicionar ao Carrinho"**

#### Fluxo:
```
1. Ver imagem e informações do produto
2. Escolher quantidade
3. Selecionar método de pagamento
4. Clicar "Adicionar ao Carrinho"

Resultado:
- ✅ Logado: produto adicionado ao carrinho (salvo no banco)
- ✅ Não logado: produto adicionado temporariamente (salvo em sessão)
```

---

### 3️⃣ Carrinho (🛒)

#### Se logado:
- Ver todos os itens adicionados
- Quantidade de cada item
- Subtotal por item
- **Total geral**
- Botão "Prosseguir para Pagamento"

#### Se NÃO logado:
- Mesmo layout, mas com aviso:
  > "Você precisa fazer login ou se cadastrar para finalizar sua compra"
- Links para Login e Cadastro
- Opção "Continuar Comprando"

#### Sistema de Rascunho:
Quando você fecha o navegador ou a internet cai:
1. Uma notificação aparece: **"Detectamos um rascunho não salvo. Deseja restaurar?"**
2. Clique em "Restaurar" para trazer os itens de volta
3. Clique em "Descartar" para limpar

---

### 4️⃣ Meu Perfil

**Disponível APENAS para usuários logados**

#### Seções:

##### A. Logo/Avatar do Perfil
- Imagem circular
- Clique para fazer upload de uma nova
- Padrão: ícone de usuário

##### B. Informações Pessoais
- Nome (do cadastro)
- Email
- Tipo de conta (Produtor / Empresa)

##### C. Editar Perfil (Formulário)
Você pode atualizar:
- **Logo/Imagem**: upload de nova imagem
- **Descrição**: conta sobre você/sua empresa
- **Notícias**: atualizações, promoções, etc.
- **Contato Adicional**: redes sociais, site, etc.

Botão "💾 Salvar Alterações" para atualizar

##### D. Meus Produtos (apenas Produtores)
- Grid com todos os seus produtos
- Nome, categoria e preço
- (Edição de produtos em breve)

##### E. Seção de Contato
- Email
- Botão "Sair da Conta"

---

### 5️⃣ Caixa de Entrada (📬)

**Disponível APENAS para usuários logados**

#### O que mostra:
- Lista de mensagens recebidas
- **De quem**: nome do remetente
- **Assunto**: tema da mensagem
- **Preview**: primeiras palavras da mensagem
- **Data/Hora**: quando foi recebida
- **Status**: lida ou não lida (badge vermelho)

#### Visual:
- Mensagens não lidas têm fundo verde claro
- Avatar do remetente com primeira letra do nome
- Indicador de lida (ponto verde/vermelho)

#### Ações:
- Clique em uma mensagem para ler (em breve)
- Contador de "não lidas" no header

---

### 6️⃣ Autenticação

#### Cadastro
URL: `/cadastro/`

```
Preencher:
1. Nome Completo
2. Email
3. Senha
4. Tipo de Conta: [Produtor] [Empresa]
↓
Clique em "Criar Conta"
↓
Redirecionado para Login
```

#### Login
URL: `/login/`

```
Preencher:
1. Email
2. Senha
↓
Clique em "Entrar"
↓
Redirecionado para sua Área Pessoal
```

#### Logout
- Clique em "Sair" no navbar
- Sessão encerrada
- Redirecionado para Home

---

## 🛍️ Fluxo Completo de Compra

### Cenário 1: Usuário Novo

```
1. Acessa home → vê produtos
2. Clica em um produto → vê detalhes
3. Adiciona ao carrinho (sem login necessário)
4. Continua comprando, adiciona mais itens
5. Clica em "Carrinho"
6. Vê aviso: "Faça login para comprar"
7. Clica em "Criar Conta" → Cadastro
8. Preenche dados → Cria conta
9. Faz login
10. Voltar para "Carrinho"
11. Clica em "Prosseguir para Pagamento"
12. (Sistema de pagamento em breve)
```

### Cenário 2: Usuário Logado

```
1. Acessa home
2. Pesquisa ou filtra por categoria
3. Clica no produto que quer
4. Escolhe quantidade
5. Adiciona ao carrinho
6. Vai para carrinho
7. Clica em "Prosseguir para Pagamento"
8. (Sistema de pagamento em breve)
```

### Cenário 3: Carrinho Abandonado

```
1. Adiciona produtos ao carrinho
2. Fecha o navegador sem comprar
3. Volta depois
4. Notificação: "Detectamos um rascunho não salvo"
5. Clica em "Restaurar"
6. Carrinho volta com os mesmos itens!
```

---

## 👥 Funcionalidades por Tipo de Usuário

### 🌱 Produtor

✅ Pode:
- Navegar e pesquisar produtos
- Ver perfil de outros produtores
- Receber mensagens de empresas interessadas
- Editar seu próprio perfil
- Adicionar logo/imagem
- Compartilhar descrição e notícias
- Ver seus produtos cadastrados

❌ Não pode:
- Comprar produtos (não é o objetivo)

### 🏢 Empresa

✅ Pode:
- Navegar e pesquisar produtos
- Comprar produtos de produtores
- Editar seu perfil
- Receber mensagens de produtores
- Adicionar logo/imagem
- Compartilhar descrição
- Fazer compras no carrinho

❌ Não pode:
- Cadastrar produtos

### 👤 Visitante (Não Logado)

✅ Pode:
- Navegar produtos
- Pesquisar e filtrar
- Adicionar ao carrinho
- Ver detalhes dos produtos
- Ver perfil de produtores/empresas

❌ Não pode:
- Comprar (precisa de login)
- Acessar caixa de entrada
- Editar perfil

---

## 💾 Dados Salvos

### No Banco de Dados:
- ✅ Carrinho de usuários logados
- ✅ Perfil do usuário (logo, descrição, notícias)
- ✅ Mensagens

### No Navegador (LocalStorage):
- ✅ Rascunho do carrinho (para restauração)

### Em Sessão Django:
- ✅ Carrinho de usuários não logados
- ✅ ID da sessão

---

## 🔒 Privacidade e Segurança

- ✅ Senhas hasheadas (não são visíveis)
- ✅ CSRF protection em formulários
- ✅ Sessões seguras
- ✅ Apenas seu próprio perfil pode ser editado
- ✅ Mensagens privadas entre usuários

---

## ⚙️ Configurações

### Para Produtores/Empresas (Admin)
- Acessar `/admin/`
- Login com credenciais de admin
- Gerenciar:
  - Usuários
  - Perfis
  - Produtos
  - Mensagens
  - Carrinhos

---

## 📱 Responsividade

A plataforma funciona perfeitamente em:
- ✅ Desktop (1920x1080+)
- ✅ Tablet (768px+)
- ✅ Mobile (360px+)

Layout se adapta automaticamente!

---

## 🚀 Dicas de Uso

1. **Pesquisa**: Use a barra de pesquisa para encontrar produtos rapidamente
2. **Filtros**: Combine categoria + pesquisa para resultados mais precisos
3. **Carrinho**: Não perca seu carrinho! Use "Restaurar rascunho" se precisar
4. **Perfil**: Atualize seu perfil com logo e descrição para ficar mais profissional
5. **Contato**: Use o contato adicional para compartilhar redes sociais

---

## ❓ Perguntas Frequentes

### P: Preciso fazer login para adicionar ao carrinho?
**R:** Não! Você pode adicionar sem login. Mas para **comprar**, precisa de login.

### P: Onde vai meu carrinho se não fizer login?
**R:** Fica na sua sessão do navegador. Se você fechar e reabrir a aba rapidinho, volta. Se fechar completamente, usamos o "rascunho" para recuperar.

### P: Posso editar meu perfil depois?
**R:** Sim! Vá em "Meu Perfil" e clique em "Editar Perfil".

### P: Como envio mensagem para um produtor?
**R:** Clique no botão "Enviar Mensagem ao Produtor" na página de detalhes. (Funcionalidade em desenvolvimento)

### P: Meu carrinho foi perdido!
**R:** Aparece uma notificação perguntando se deseja restaurar. Clique em "Restaurar".

---

## 🎨 Paleta de Cores

- 🟢 Verde Primário: `#7a9d3d` (botões, destaque)
- 🟩 Verde Secundário: `#5a7a2f` (hover)
- ⚪ Branco: `#ffffff` (fundos)
- 🔘 Cinza: `#f8f9fa` (áreas secundárias)
- ⚫ Preto: `#333333` (textos)

---

## 📞 Suporte

Dúvidas? Entre em contato via:
- 📧 Email: contato@fairtradeconnect.com
- 💬 Mensagens dentro da plataforma
- 🔗 Redes sociais (em breve)

---

**Obrigado por usar Fair Trade Connect! 🌾**

Ajudando a conectar produtores e empresas para um comércio mais justo e sustentável.
