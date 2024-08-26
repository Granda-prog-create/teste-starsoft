# Starsoft Project - OpenAI API Integration

## Descrição

Este projeto é um teste de integração com a API da OpenAI, criado como parte de um processo de entrevista de emprego. Ele utiliza Docker para facilitar a configuração e execução do ambiente, garantindo que todas as dependências estejam isoladas e funcionem corretamente. O código principal faz uma chamada à API da OpenAI para gerar conteúdo baseado em um prompt fornecido.

## Estrutura do Projeto

- **`Dockerfile`**: Arquivo de configuração para criar a imagem Docker do projeto.
- **`docker-compose.yml`**: Arquivo que orquestra os contêineres Docker necessários para o projeto.
- **`main.py`**: Script principal em Python que interage com a API da OpenAI.
- **`requirements.txt`**: Lista de dependências Python necessárias para o projeto.
- **`README.md`**: Documento com informações sobre o projeto e como executá-lo.
- **`venv/`**: Ambiente virtual Python usado para isolar as dependências do projeto.
- **`.env`**: Arquivo para armazenar variáveis de ambiente, incluindo a chave de API da OpenAI.

## Pré-requisitos

- **Docker**: Certifique-se de ter o Docker instalado em sua máquina. [Instruções de instalação](https://docs.docker.com/get-docker/)
- **Python 3.8+**: Para rodar o projeto localmente fora do Docker (opcional).
- **Conta na OpenAI**: Para gerar uma chave de API e acessar a API da OpenAI.

## Configuração

1. **Clone o repositório:**

   ```bash
   git clone 
   cd starsoft-project
   ```

2. **Crie a chave de API da OpenAI:**

   - Acesse a [página de API Keys da OpenAI](https://platform.openai.com/account/api-keys).
   - Crie uma nova chave, com o nome `starsoft-project` e permissões `Restricted`.
   - Copie a chave gerada.

3. **Configure as variáveis de ambiente:**

   - Crie um arquivo `.env` na raiz do projeto:
     ```bash
     touch .env
     ```
   - Adicione a sua chave de API ao arquivo `.env`:
     ```env
     OPENAI_API_KEY=sua-nova-chave-aqui
     ```

4. **Construa e execute o contêiner Docker:**

   ```bash
   docker-compose up --build
   ```

   Isso vai baixar as dependências, criar o ambiente, e rodar o script `main.py` automaticamente.

## Execução Manual

Se você quiser rodar o script manualmente sem o Docker:

1. **Ative o ambiente virtual:**

   ```bash
   source venv/bin/activate
   ```

   No Windows:
   ```bash
   .env\Scriptsctivate
   ```

2. **Instale as dependências:**

   ```bash
   pip install -r requirements.txt
   ```

3. **Rode o script principal:**

   ```bash
   python main.py
   ```

## Solução de Problemas

- **Erro de Autenticação (401):** Verifique se a chave de API está correta no arquivo `.env`.
- **Problemas com Docker:** Certifique-se de que o Docker está instalado e funcionando corretamente na sua máquina.

## Tecnologias Utilizadas

- **Python 3.8+**
- **Docker**
- **OpenAI API**
- **LangChain** (Biblioteca utilizada para interação com a OpenAI)
- **VS Code** (Recomendado para desenvolvimento)