# D&C Estética Automotiva

Site institucional para a D&C Estética Automotiva, desenvolvido com **Python, Flask, HTML e CSS**. A aplicação Flask pode ser servida por ASGI usando **Uvicorn** com o adaptador **asgiref**.

## Tecnologias

- **Python e Flask:** executam o servidor e definem as rotas que exibem cada página.
- **Uvicorn e asgiref:** permitem servir a aplicação Flask WSGI através de um servidor ASGI.
- **HTML e Jinja:** estruturam o conteúdo e reutilizam o layout compartilhado entre as páginas.
- **CSS:** controla cores, tipografia, espaçamento, imagens e adaptação para telas menores.

## Páginas

| Página | Endereço | Conteúdo |
| --- | --- | --- |
| Início | `/` | Apresentação e serviços de estética automotiva. |
| Serviços | `/servicos` | Serviços oferecidos e opções para agendamento. |
| Sobre nós | `/sobre-nos` | Apresentação da empresa, seus cuidados e compromisso com o cliente. |
| Contato | `/contato` | Acesso ao WhatsApp da equipe e ao endereço no mapa. |

## Estrutura do projeto

```text
.
├── app.py                  # Aplicação Flask e rotas
├── requirements.txt        # Dependências Python
├── render.yaml             # Configuração de deploy no Render
├── .gitignore              # Arquivos locais ignorados pelo Git
├── templates/
│   ├── base.html           # Layout compartilhado e navegação
│   ├── index.html          # Página inicial
│   ├── services.html        # Página Serviços
│   ├── about.html          # Página Sobre nós
│   └── contact.html        # Página Contato
└── static/
    ├── style.css           # Estilos do site
    └── imagens/            # Imagens utilizadas nas páginas
```

## Requisitos

- Python 3.9 ou superior.
- `pip`, o instalador de pacotes do Python.

## Instalação e execução

No terminal, dentro da pasta do projeto:

1. (Opcional, recomendado) Crie e ative um ambiente virtual:

   ```bash
   python -m venv .venv
   ```

   No Windows PowerShell:

   ```powershell
   .venv\Scripts\Activate.ps1
   ```

   No macOS ou Linux:

   ```bash
   source .venv/bin/activate
   ```

2. Instale as dependências do projeto (Flask, asgiref e Uvicorn):

   ```bash
   pip install -r requirements.txt
   ```

3. Inicie o servidor local:

   ```bash
   python app.py
   ```

4. Abra `http://127.0.0.1:5000` no navegador.

O servidor de desenvolvimento do Flask recarrega a aplicação quando os arquivos mudam. Para encerrar, use `Ctrl+C` no terminal.

## Executar com Uvicorn

Com as dependências instaladas, execute na pasta do projeto:

```bash
uvicorn app:asgi_app --host 0.0.0.0 --port 8000
```

Abra `http://127.0.0.1:8000` no navegador. Para desenvolvimento com recarga automática, acrescente `--reload` ao comando. A opção `--host 0.0.0.0` permite receber conexões externas quando o ambiente de hospedagem liberar a porta configurada.

## Deploy no Render

O arquivo `render.yaml` configura o build com `pip install -r requirements.txt` e inicia o site com Uvicorn na porta fornecida pelo Render. No painel do Render, crie um **Blueprint** apontando para o repositório GitHub deste projeto para aplicar essa configuração.

O `.gitignore` exclui ambientes virtuais, caches, arquivos `.env` e dados locais. Templates, CSS e imagens necessários ao site permanecem incluídos no deploy.

## Contato e agendamento

A página `/contato` oferece acesso direto ao WhatsApp da equipe e ao endereço no mapa. Os botões de agendamento do site direcionam para essa página.
