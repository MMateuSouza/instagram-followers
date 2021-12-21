# *Instagram Followers*

Projetinho desenvolvido utilizando *Python* 3 para obter informações de reciprocidade.

## Estrutura do Projeto

```bash
.
├── README.md
├── accounts_following_you.txt
├── accounts_you_follow.txt
└── main.py

0 directories, 4 files
```

## Pré-requisitos

Possuir *Python* 3 instalado em seu computador. Para baixá-lo utilizar o seguinte [link](https://www.python.org/downloads/).

## Instruções para Uso

1. Popular os arquivos `accounts_you_follow.txt` e `accounts_following_you.txt` com os respectivos *links*: [Sigo](https://www.instagram.com/accounts/access_tool/accounts_you_follow) e [Seguidores](https://www.instagram.com/accounts/access_tool/accounts_following_you).

2. Com o *Python* instalado, utilizar o terminal de seu sistema operacional e executar o arquivo `main.py` da seguinte forma:

    ```bash
    python main.py
    ```

3. A aplicação irá dar um resultado similar ao abaixo:

    Arquivo de exemplo `accounts_you_follow.txt`

    ```txt
    fulano
    ciclobeltrano
    ```

    Arquivo de exemplo `accounts_following_you.txt`

    ```txt
    fulano
    ciclano
    beltrano
    ```

    Resultrado obtido:

    ```bash
    username@hostname:/$ python main.py
    Sigo mas não me segue: ['ciclobeltrano']
    Segue mas não sigo: ['ciclano', 'beltrano']
    ```