O projeto foi desenvolvido com o objetivo de demonstrar meu conhecimento em lógica de programação, estrutura de dados e conceitos básicos de APIs RESTful.

Foi utilizado o Framework Flask (Python). Esse ano tive meu primeiro contato com a linguagem (na faculdade) e acho que ela é uma das mais simples para usar e aprender. Ele é uma forma simples de criação de APIs.

Foi implementado em dicionário (hash map) do Python. Ele permite o armazenamento de dados no formato de chave-valor, onde id é único do estudante e o valor é um dicionário contendo os dados. 

Foi utilizado também a biblioteca uuid (uuid.uuid4()) gera um identificador universalmente unico, o que evita que existam mesmos IDs.

A rota POST inclui validação de dados recebidos. A API verifica se os campos obrigatórios (name e score) estão presentes. Em caso de dado inválido, a API retorna uma mensagem de erro de status HTTP (400 Bad Request).

Utilizei a lógica find_unique_char para não repetir letra. 

A API estará disponível em: http://127.0.0.1:5000/students

### Servidor Rodando
<img width="508" height="279" alt="image" src="https://github.com/user-attachments/assets/0abee341-9d4e-4ab9-8226-50fec694f9d6" /><br>

### POST /students - Cadastrar Estudante
<img width="752" height="167" alt="image" src="https://github.com/user-attachments/assets/68524622-7ffe-4034-b3bf-62f318fbf900" /><br>

### GET /students - Listar Todos
<img width="488" height="392" alt="image" src="https://github.com/user-attachments/assets/0ba28350-713c-4a5c-b20b-6ff14da84dcc" /><br>

<img width="675" height="872" alt="image" src="https://github.com/user-attachments/assets/00de43de-5186-4f46-8d89-eeb71955e8d3" /><br>

<img width="499" height="403" alt="image" src="https://github.com/user-attachments/assets/af9f612f-0290-415f-93a0-8fab0e5cdd6d" /><br>

### GET /students/:id - Buscar por ID
<img width="414" height="306" alt="image" src="https://github.com/user-attachments/assets/72276b1a-26d7-44ab-9b28-8b2af2e696c8" /><br>
<img width="462" height="149" alt="image" src="https://github.com/user-attachments/assets/ab798efc-f269-400a-89a8-003837f14b29" />





