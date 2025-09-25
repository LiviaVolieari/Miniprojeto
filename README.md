# 🛒 MiniProjeto - Lista de Produtos

Um sistema simples de gerenciamento de produtos feito com **Flask**.  
Usuários podem cadastrar, visualizar, editar e excluir produtos, além de possuir autenticação básica de usuários.

---

## 🔎 Funcionalidades

- Cadastro de usuários  
- Login de usuários  
- Cadastro de novos produtos  
- Listagem de produtos cadastrados  
- Edição de produtos existentes  
- Exclusão de produtos  
- Estilização com HTML e CSS  

---

## 📊 Tecnologias Utilizadas

- Python 3  
- Flask  
- SQLite  
- HTML / CSS  

---

## 🖥️ Instalação

1. **Clone o repositório do projeto para sua máquina e entre na pasta do projeto recém-clonada**

   ```git
   git clone https://github.com/LiviaVolieari/Miniprojeto.git
   cd Miniprojeto
    ```


2. **Crie e ative o ambiente virtual para isolar as dependências do projeto**
    ```sh
    # Criar ambiente virtual
    python -m venv env

    # Ativar no Windows
    .\env\Scripts\activate

    # Ativar no Linux/Mac
    source venv/bin/activate
        ```

3. **Instale todas as bibliotecas necessárias listadas no arquivo requirements.txt**

    ```sh
    pip install -r requeriments.txt
        ```


4. **Execute a aplicação**

    ```sh
    flask run --debug
        ```


5. **Abra no navegador:**

http://127.0.0.1:5000


## 👥 Contribuintes

- [Emanoelly Francinny](https://github.com/FranbryloB)  
    Implementou as páginas iniciais (login, index, cadastro).

    Implementou o CSS base.

- [Isabele Fernanda](https://github.com/Isa-Fee)  
    Criou os arquivos requirements.txt e README.md (bem como organização do mesmo).

    Desenvolveu melhorias no CSS da página de produtos.

- [Livia Tainá](https://github.com/LiviaVolieari)  
    Realizou correções no código, remoção do ambiente virtual, ajustes no CSS e rotas.

    Organizou o repositório e fez limpeza com .gitignore.

- [Tamíris Medeiros](https://github.com/medeirostamiris)  
    Criou a funcionalidade de Cadastro de Produtos.
    
    Adcionou produtos ao banco.
