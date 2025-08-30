# EPI MVP — CRUD de Colaboradores (Django + Front integrado)

## Como rodar
```bash
pip install -r requirements.txt
# copie .env.example para .env e configure DB_USER/DB_PASSWORD/DB_HOST/DB_PORT
python manage.py migrate
python manage.py runserver
```
Acesse: http://127.0.0.1:8000/

## Docker (opcional)
- Você pode adaptar facilmente usando docker-compose apontando para MySQL.
