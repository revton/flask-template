# Template Flask Application #

## Escopo ##

- [x] Poetry
- [x] Pytest
- [x] Flask
- [x] Safety
- [x] Linter
- [x] Docker
- [ ] Coverage
- [ ] DebugToolbar
- [ ] Behave
- [ ] Configuration
- [ ] Logging
- [ ] API
- [ ] Database
- [ ] Migration
- [ ] Admin
- [ ] Login
- [ ] Forms
- [ ] Mail
- [ ] CSRF Protection
- [ ] Appearence
- [ ] Commands
- [ ] Template
- [ ] Queue
- [ ] Dashboard
- [ ] Cache
- [ ] Internationalization and localization
- [x] Web Server
- [ ] Web Application

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