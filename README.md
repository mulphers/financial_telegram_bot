## Financial telegram bot

Telegram bot on AIOgram, SQLAlchemy, Alembic and PostgreSQL for financial control

#### 1. Project structure:
````
financial_telegram_bot/
├── migrations/ # default alembic folder
├── src/
│   ├── common/
│   │   ├── callback_factory/
│   │   │   ├── __init__.py
│   │   │   └── expense.py
│   │   ├── dto/
│   │   │   ├── __init__.py
│   │   │   ├── expense.py 
│   │   │   └── user.py 
│   │   ├── fsm/
│   │   │   ├── __init__.py
│   │   │   ├── ad_filling_state.py
│   │   │   └── expense_filling_state.py
│   │   ├── interfaces/
│   │   │   ├── __init__.py
│   │   │   ├── abstract_repository.py
│   │   │   └── abstract_uow.py
│   │   ├── keyboards/
│   │   │   ├── __init__.py
│   │   │   ├── command_menu.py
│   │   │   └── keyboard_generator.py
│   │   ├── __init__.py
│   │   └── types.py
│   ├── core/   
│   │   ├── __init__.py
│   │   └── settings.py
│   ├── database/
│   │   ├── core/
│   │   │   ├── __init__.py
│   │   │   ├── connection.py
│   │   │   └── sqlalchemy_uow.py
│   │   ├── models/
│   │   │   ├── base/
│   │   │   │   ├── mixins/
│   │   │   │   │   ├── __init__.py
│   │   │   │   │   └── with_time.py
│   │   │   │   ├── __init__.py
│   │   │   │   └── core.py
│   │   │   ├── __init__.py
│   │   │   ├── expense.py
│   │   │   └── user.py
│   │   ├── repositories/
│   │   │   ├── __init__.py
│   │   │   ├── expense_repository.py
│   │   │   ├── sqlalchemy_repository.py
│   │   │   └── user_repository.py
│   │   └── __init__.py
│   ├── filters/
│   │   ├── __init__.py
│   │   └── is_admin.py
│   ├── routers/
│   │   ├── admin/
│   │   │   ├── commands/
│   │   │   │   ├── __init__.py
│   │   │   │   ├── ad.py
│   │   │   │   └── change_admin_status.py
│   │   │   ├── messages/
│   │   │   │   ├── __init__.py
│   │   │   │   └── ad_filling.py
│   │   │   ├── __init__.py
│   │   │   └── router.py
│   │   ├── client/
│   │   │   ├── callbacks/
│   │   │   │   ├── __init__.py
│   │   │   │   ├── actions_on_finances.py
│   │   │   │   ├── add_expense.py
│   │   │   │   ├── remove_expense.py
│   │   │   │   └── view_expense.py
│   │   │   ├── commands/
│   │   │   │   ├── __init__.py
│   │   │   │   ├── action.py
│   │   │   │   ├── help.py
│   │   │   │   ├── profile.py
│   │   │   │   └── start.py
│   │   │   ├── messages/
│   │   │   │   ├── __init__.py
│   │   │   │   └── expense_filling.py
│   │   │   ├── my_chat_member/
│   │   │   │   ├── __init__.py
│   │   │   │   └── member_status_changed.py
│   │   │   ├── __init__.py
│   │   │   └── router.py
│   │   ├── default/
│   │   │   ├── callback/
│   │   │   │   ├── __init__.py
│   │   │   │   └── other.py
│   │   │   ├── messages/
│   │   │   │   ├── __init__.py
│   │   │   │   └── other.py
│   │   │   ├── __init__.py
│   │   │   └── router.py
│   │   └── __init__.py
│   ├── utils/
│   │   ├── lexicon/
│   │   │   ├── __init__.py
│   │   │   ├── admin.py
│   │   │   ├── client.py
│   │   │   └── command.py
│   │   ├── __init__.py
│   │   ├── decorators.py
│   │   └── send_ad.py
│   ├── __init__.py
│   └── __main__.py
├── .dockerignore
├── .env_example
├── .flake8
├── .gitignore
├── Dockerfile
├── alembic.ini
├── docker-compose.yml
├── requirements.txt
└── mypy.ini
````

### 2. How to copy a project:
````
git clone https://github.com/mulphers/financial_telegram_bot.git
````

### 3. Env-file:

Rename .env_example to .env and fill in

````
BOT_TOKEN=yourtoken

DATABASE_URL=sqlite+aiosqlite:///{} || postgresql+asyncpg://{}
DATABASE_NAME=yourdbname
DATABASE_HOST=yourdbhost || None
DATABASE_PORT=yourdbport || None
DATABASE_USER=yourdbuser || None
DATABASE_PASSWORD=yourdbpassword || None
````

### 4. Run a project:

Go to your working directory and enter the command

````
docker-compose up
````

### 5. Database:

You can manage the database by following the link

````
http://127.0.0.1:8080
````
