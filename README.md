# WEDev Learning

Este foi o test ou desafio que me foi proposto pela Wedev a fim de testar as minhas competências como desenvolvedor na linguagen `Python`.

A aplicação desenvolvida tem a finalidade de registrar cursos, professores, alunos, inscrever alunos em cursos, entre outros.

## Como rodar a aplicação

Deixei alguns scripts já prontos no makefile, no entanto precisa rodar o docker compose para download da imagem da base de dados em seguida,
criar uma base de dados com o nome **wedevLearning** e executar as migrations.

Antes porém inicializar o ambiente virtual e instalar todas as dependências.

Em seguida rodar

```bash
 # Baixar a imagem do projecto

 docker-compose up

 # Inicializar a base de dados

 docker run -d -it --name pg_database -e POSTGRES_PASSWORD=postgresdb2022 -e POSTGRES_DB=wedevLearning -p 5432:5432 postgres:latest

 # Rodar as migrations

 alembic upgrade heads

 # Inicializar a aplicação

 python3 main.py

```

Agora, falando sobre a aplicação, possuí três níveis de usuário

A saber:

- **staff** - Super Admin
- **teacher** - Professores
- **student** - Estudantes

Dito isso porque existe determinadas rotas que não são acessadas por outros usuários a não ser o staff ou a especificação do usuário.
Foi desenvolvido um decorator para rodar a autorização de acesso as rotas.

```python
from functools import wraps
from fastapi import HTTPException


def Authorization(*permitions):
    """Recive authorizations params"""

    def inner(func):
        """Agregate func scoped"""

        @wraps(func)
        async def wrapper(*args, **kwargs):
            """Recive a func parameters"""

            if kwargs["auth"] not in permitions:
                raise HTTPException(
                    status_code=401,
                    detail="Unauthorized access",
                    headers={"WWW-Authenticate": "Bearer"},
                )

            return await func(*args, **kwargs)

        return wrapper

    return inner
```

Implementação das autorizações

```python
@student_routes.get("/students", response_model=StudentResponseModel)
@Authorization("staff")
async def get_teachers(auth=Depends(AuthMiddleware.auth_wrapper)):

    students_handler = GetAllStudentsHandler(StudentRepository)
    students = students_handler.handle()
    return {"students": students.get_value()}


```

Para acessar a documentação da aplicação, após rodar a mesma acessar a rota **/docs**

```bash
http://0.0.0.0:8000/docs

# Link
```

Comandos

```shell
pip3 install -r requirements.txt,
python3 main.py
```

## Métodos

Requisições para a API devem seguir os padrões:
| Método | Descrição |
| -------- | ----------------------------------------------------- |
| `GET` | Retorna informações de um ou mais registros. |
| `POST` | Utilizado para criar um novo registro. |
| `PUT` | Atualiza dados de um registro ou altera sua situação. |
| `DELETE` | Remove um registro do sistema. |

## Respostas

| Código | Descrição                                                                            |
| ------ | ------------------------------------------------------------------------------------ |
| `200`  | Requisição executada com sucesso (success).                                          |
| `400`  | Erros de validação ou os campos informados não existem no sistema.                   |
| `401`  | Dados de acesso inválidos.                                                           |
| `404`  | Registro pesquisado não encontrado (Not found).                                      |
| `405`  | Método não implementado.                                                             |
| `410`  | Registro pesquisado foi apagado do sistema e não esta mais disponível.               |
| `422`  | Dados informados estão fora do escopo definido para o campo.                         |
| `429`  | Número máximo de requisições atingido. (_aguarde alguns segundos e tente novamente_) |

## Exemplo de usuário staff

- Request (application/json)

  - Body

        {
            "name": "António Campos",
            "email": "antoniocampos@gmail.com",
            "surname": "string",
            "city": "string",
            "password": "string",
            "state": true
        }

- Response 200 (application/json)

  - Body

        {
            "detail": {
                "msg": "Successfully user created!"
            }
        }

Caso a requisição não conter nenhuma resposta o retorno será:

    {
        "detail": "Não encontrado."
    }

### Listar cursos [GET]

- Request (application/json)

  - Headers

        Authorization: Bearer [access_token]

- Response 200 (application/json)

        {
            "courses": [
                {
                    "id": 1,
                    "name": "Php",
                    "startDate": "2022-04-18T21:43:04.279Z",
                    "endDate": "2022-04-18T21:43:04.279Z",
                    "state": true,
                    "teacher": {
                        "id": 3,
                        "name": "António Gabriel",
                        "email": "antoniogabriel@gmail.com"
                    }
                }
            ]
        }

### Caso autenticado e sem autorização para uma dada requisição

- Request (application/json)

  - Headers

        Authorization: Bearer [access_token]

- Response 401 (application/json)

        {
            "detail": "Unauthorized access"
        }
    

## Funcionalidades

Os recursos funcionais da aplicação são:

- [x] Criação e actualização de usuário (staff, student, teacher)
- [x] Criação de cursos
- [x] Inscrição de estudantes aos cursos
- [x] Authenticação de usuário (staff, student, teacher)
- [x] Listar os cursos com os respectivos professores0
- [x] Validação dos campos antes da inserção
- [x] Privatizar acesso as rotas aa diferentes usuários
- [x] Listar total de cursos e alunos inscritos na sessão do professor
