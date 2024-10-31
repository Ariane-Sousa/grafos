## Pré-requisitos

Antes de começar, verifique se você possui o Docker e o Docker Compose instalados em sua máquina.

- Docker: [Instalação do Docker](https://docs.docker.com/get-docker/)
- Docker Compose: [Instalação do Docker Compose](https://docs.docker.com/compose/install/)

## Instruções

1. Clone o repositório do projeto:

    ```bash
    git clone https://github.com/Ariane-Sousa/desafio-spotsat.git
    ```

2. Acesse o diretório do projeto:

    ```bash
    cd desafio-spotsat
    ```

3. Execute o Docker Compose para construir e iniciar os contêineres:

    ```bash
    docker-compose up --build
    ```

4. projeto estará disponível nos seguintes endereços:

    - Aplicação Web: [http://localhost:8000](http://localhost:8000)
    - API: [http://localhost:8000/api](http://localhost:8000/api)

5. Para parar a execução do projeto, pressione `Ctrl + C` no terminal e execute o seguinte comando:

    ```bash
    docker-compose down
    ```

5. Para rodar o Lint:

    ```bash
    docker-compose run web pylint graphs
    ```

6. Para rodar os Testes:

    ```bash
    docker-compose run web pytest
    ```

# Tecnologias Utilizadas

Este projeto foi desenvolvido utilizando as seguintes tecnologias:

## Pytest

Pytest é uma estrutura de teste que torna mais fácil escrever pequenos testes, mas escaláveis em Python. Foi utilizado para escrever e executar testes automatizados no projeto.

- Mais informações: [Documentação do Pytest](https://docs.pytest.org/en/latest/)

## Pylint

Pylint é uma ferramenta que verifica se um programa Python cumpre um conjunto de padrões de codificação. Foi utilizado para garantir a conformidade com as diretrizes de estilo e boas práticas de codificação.

- Mais informações: [Documentação do Pylint](https://pylint.pycqa.org/en/latest/)

## FastAPI

FastAPI é um framework web rápido (high-performance) para construir APIs com Python 3.7+ baseado em padrões de tipo Python padrão. Foi utilizado para desenvolver as APIs neste projeto.

- Mais informações: [Documentação do FastAPI](https://fastapi.tiangolo.com/)

## PostGIS

PostGIS é uma extensão espacial para o PostgreSQL que adiciona suporte para objetos geográficos, permitindo armazenar e consultar dados geográficos em um banco de dados PostgreSQL. Foi utilizado para armazenar e consultar dados geográficos neste projeto.

- Mais informações: [Site do PostGIS](https://postgis.net/)

## Docker

Docker é uma plataforma de software que permite criar, testar e implantar aplicativos rapidamente. Ele encapsula o aplicativo em contêineres, que podem ser executados em qualquer ambiente. Foi utilizado para criar e executar ambientes de desenvolvimento e produção consistentes e isolados.

- Mais informações: [Site do Docker](https://www.docker.com/)

# Logs

Este projeto utiliza logs para registrar informações relevantes durante a execução das APIs. Os logs são úteis para depuração, monitoramento e análise de problemas no sistema.

## Uso de Logs

Os logs são registrados em diferentes níveis de gravidade, como DEBUG, INFO, WARNING, ERROR e CRITICAL. Cada nível fornece informações específicas sobre o estado e o funcionamento do sistema.

- **INFO**: Mensagens informativas que destacam o progresso e as atividades normais do sistema.

## Configuração dos Logs

Os logs são configurados para serem armazenados em arquivos ou enviados para destinos específicos, como consoles, serviços de log em nuvem ou sistemas de monitoramento. A configuração dos logs pode ser ajustada conforme necessário para atender aos requisitos do projeto.

