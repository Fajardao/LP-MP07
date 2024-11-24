# Aplicação de Gestão de Tópicos

## Descrição
Este projeto é uma aplicação web desenvolvida com Django que simula um fórum de discussão. Os utilizadores podem criar tópicos, visualizar os detalhes de cada tópico, adicionar comentários e editar ou eliminar conteúdos (se forem os autores). É uma aplicação prática que segue boas práticas de desenvolvimento web, integrando funcionalidades completas de CRUD (Create, Read, Update, Delete).

## Funcionalidades
- **Listagem de Tópicos:** Página inicial com uma lista de todos os tópicos criados, mostrando título e descrição.
- **Detalhes de Tópicos:** Página para visualizar os detalhes de um tópico, incluindo os comentários associados.
- **Criação de Tópicos:** Formulário para criar novos tópicos.
- **Adicionar Comentários:** Formulário para adicionar comentários em tópicos existentes.
- **Editar e Eliminar Conteúdo:** Possibilidade de editar e eliminar tópicos e comentários, disponível apenas para o autor.
- **Autenticação:** Registo, login e logout de utilizadores para acesso às funcionalidades.

## Requisitos
- **Python 3.9 ou superior**
- **Django 4.0 ou superior**

Certifique-se de que possui as seguintes ferramentas instaladas:
- Virtualenv (opcional, mas recomendado)

## Configuração do Projeto

### Passos para Instalação
1. Clone este repositório:
   ```bash
   git clone https://github.com/SEU_UTILIZADOR/NOME_DO_REPOSITORIO.git
   cd NOME_DO_REPOSITORIO
   ```

2. Crie e ative um ambiente virtual (opcional, mas recomendado):
   ```bash
   python -m venv venv
   source venv/bin/activate    # Linux/Mac
   venv\Scripts\activate       # Windows
   ```

3. Instale as dependências necessárias:
   ```bash
   pip install -r requirements.txt
   ```

4. Configure a base de dados e realize as migrações:
   ```bash
   python manage.py migrate
   ```

5. Crie um superutilizador para aceder ao painel administrativo:
   ```bash
   python manage.py createsuperuser
   ```

6. Inicie o servidor:
   ```bash
   python manage.py runserver
   ```

7. Aceda ao projeto em [http://localhost:8000](http://localhost:8000).

---

## Como Utilizar

### 1. Painel de Administração
- Aceda a [http://localhost:8000/admin](http://localhost:8000/admin).
- Utilize as credenciais do superutilizador criado anteriormente para fazer login.
- Aqui, pode gerir tópicos, comentários e utilizadores diretamente.

### 2. Funcionalidades da Aplicação
- **Página Inicial:** Lista de tópicos.
- **Detalhes de Tópico:** Clique num tópico para ver detalhes e comentários.
- **Criar Tópico:** Utilize o botão "Add new topic" na página inicial.
- **Adicionar Comentário:** Dentro de um tópico, use o formulário de comentário.
- **Editar ou Eliminar:** Disponível para o autor do conteúdo.

---

## Testes

### Executar Testes Unitários
Os testes garantem o correto funcionamento das principais funcionalidades da aplicação. Para executá-los:
```bash
python manage.py test
```

Certifique-se de que todos os testes passam com sucesso antes de submeter o projeto.

---

## Tecnologias e Bibliotecas Utilizadas
- **Django Framework:** Backend e ORM.
- **SQLite:** Base de dados padrão (pode ser alterado para PostgreSQL ou MySQL, se necessário).