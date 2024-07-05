## Desafio - Grafos

Seja bem-vindo! Este desafio foi projetado para avaliar a sua capacidade técnica de implementação de um projeto backend e utilização de algoritimos de otimização e uma tecnologia de georreferenciamento. Na Spotsat precisamos diariamente trabalhar com referências geográficas e para isso utilizamos uma extensão no postgres, o postgis. O desafio consiste na construção de uma api que possa utilizá-lo. 

### Proposta

Crie um CRUD de grafos com coordenadas geográficas(pontos ou polígonos) que deve receber como entrada em uma rota um grafo direcionado, salvar o mesmo no banco de dados, uma outra rota apenas para buscar por um grafo em específico por o id do mesmo, um terceira rota para dado um grafo salvo anteriormente, sobre ele buscarmos todas as possíveis rotas entre dois pontos do grafo baseado em um limite de paradas ou não, e uma quarta e última rota que semelhante a terceira, se baseia em um grafo cadastrado anteriormente no banco de dados, e baseado nesse grafo, se busca a menor rota possível entre dois pontos desse dado grafo.

### Instruções
    • Utilize qualquer linguagem de sua escolha.
    • Utilize arquitetura MVC.
    • Utilize o PostgreSQL+PostGIS para determinar as distancias entre os pontos.
    • Implemente configurações de segurança e utilize um sistema de logs para identificar acesso autorizado, não autorizado, edição e exclusão de objetos no banco. Além de quais quer outros logs que julgar necessário.
    • Você deve aplicar testes automatizados ao menos nas funcionalidades básicas.
    • Sua aplicação deve ter imagem docker otimizada para produção.
    • Configure um workflow no seu repositório git para conferir lint e testes.

### Diferenciais
    • Utilizar Node preferencialmente e Python com Fastify.
    • Demonstrar cálculo de custo computacional do algoritmo de busca e conclusões de otimização.
    • Implementar implementação RBAC básica para organização dos usuários e níveis de acesso.
    • Deploy básico em plataforma gratuita de sua escolha.
    • Documentação de uso(Contrato da API).
