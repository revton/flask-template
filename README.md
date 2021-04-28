# Template Flask Application #

## Escopo ##

- [x] Poetry
- [x] Pytest
- [x] Flask
- [x] Safety
- [x] Linter
- [x] Docker
- [x] Coverage
- [x] DebugToolbar
- [x] Cyclomatic Complexity
- [x] Configuration
- [x] Logging
- [x] Commands
- [x] Application Server
- [x] Web Server
- [ ] Internationalization and localization
- [x] Behave
- [x] Selenium
- [x] Admin
- [x] Database
- [ ] API
- [ ] Migration
- [ ] Login
- [ ] Forms
- [ ] Mail
- [ ] CSRF Protection
- [ ] Appearence
- [ ] Template
- [ ] Queue
- [ ] Dashboard
- [ ] Cache
- [ ] Socket


## Documentação ###

### Poetry ###

- Criando virtualenv
```bash
poetry env use 3.8
```

- Ativando no shell
```bash
poetry shell
```

- Instalar as dependências do projeto
```bash
poetry install
```

- Adicionar dependência
```bash
poetry add flask
```

- Executar os tests
```bash
poetry run pytest
```

- Exportar as dependências do projeto
```bash
poetry export -f requirements.txt --output requirements.txt
```

### Safety ###
```bash
safety check
```

### Docker ###

**Atenção**: antes de executar o `docker-compose`, não esquecer de exportar as dependências do projeto para o `requirements.txt`
```bash
docker-compose up --build
```

### Coverage ###

- Executar o teste de cobertura
```bash
coverage run --source=flask_template -m pytest
```

- Gerar relatório de cobertura
```bash
coverage report
```

- Gerar HTML
```bash
coverage html
```

### Dynaconf ###

- Validar as configurações a partir do `dynaconf_validators.toml`
```bash
dynaconf validate
```

### Radon ###

- Verificar complexidade ciclomática
```bash
radon cc flask_template -a -s
```

- Verificar índice de manutenibilidade
```bash
radon mi flask_template
```

### Commands ###

- Verificar quais comandos registrados
```bash
flask --help
```
```
Commands:
  coverage           Run/ Report/ HTML Coverage Tests.
  dynaconf-validate  Checks validation of settings parameters.
  lint               Lint and check code style with black, flake8 and isort.
  radon              Checks Cyclomatic Complexity and Halstead metrics.
  routes             Show the routes for the app.
  run                Run a development server.
  safety             Checks your installed dependencies for known security...
  shell              Run a shell in the app context.
```

### Behave ###

- Executar os testes de comportamento
```bash
behave
```

### Selenium ###

- Instalar chromedriver
```bash
brew cask install chromedriver
```

### Database ###

Banco de dados inicializado dentro da extensão `database.py`

- Caso precise excluir e criar novamente, utilize o shell no flask
```bash
flask shell
```

- Criar bando de dados
```python
from flask_template.extensions.database import db
db.create_all()
```

- Excluir bando de dados
```python
from flask_template.extensions.database import db
db.drop_all()
```
