O projeto foi desenvolvido com o objetivo de demonstrar meu conhecimento em lógica de programação, estrutura de dados e conceitos básicos de APIs RESTful.

Foi utilizado o Framework Flask (Python). Esse ano tive meu primeiro contato com a linguagem (na faculdade) e acho que ela é uma das mais simples para usar e aprender. Ele é uma forma simples de criação de APIs.

Foi implementado em dicionário (hash map) do Python. Ele permite o armazenamento de dados no formato de chave-valor, onde id é único do estudante e o valor é um dicionário contendo os dados. 

Foi utilizado também a biblioteca uuid (uuid.uuid4()) gera um identificador universalmente unico, o que evita que existam mesmos IDs.

A rota POST inclui validação de dados recebidos. A API verifica se os campos obrigatórios (name e score) estão presentes. Em caso de dado inválido, a API retorna uma mensagem de erro de status HTTP (400 Bad Request).

Utilizei a lógica find_unique_char para não repetir letra. 