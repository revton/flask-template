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
- [ ] Commands
- [ ] Web Application
- [ ] Internationalization and localization
- [ ] Behave
- [ ] API
- [ ] Database
- [ ] Migration
- [ ] Admin
- [ ] Login
- [ ] Forms
- [ ] Mail
- [ ] CSRF Protection
- [ ] Appearence
- [ ] Template
- [ ] Queue
- [ ] Dashboard
- [ ] Cache
- [x] Web Server


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

- Fazer build do container, não esquecer de exportar as dependências do projeto para o requirements.txt
```bash
docker build -f Dockerfile . -t flask-template 
```

- Executar a imagem criada
```bash
docker run -p 5000:5000/tcp -d flask-template:latest
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