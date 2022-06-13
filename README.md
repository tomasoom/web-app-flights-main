# web-app-flights


## Primeiros passos para correr aplicação
1. Abra a linha de comandos (PowerShell ou cmd)
1. Descarregue uma cópia (clone) do repositório com o comando `git clone https://github.com/teoria-da-computacao/web-app-flights` 
1. Entre na pasta  `cd web-app-flights`
1. Garanta que tem o pipenv instalado, correndo o comando `python3 -m pip install pipenv`
   1. se tiver erro de permissões execute:`Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser`
   1. se não conseguir instalar o pipenv ou der erro, trabalhe sem ambiente virtual. Para tal, instale o django sem pipenv (ambiente virtual) com o comando `python -m pip install django`. nessa caso não precisarás de ativar o ambiente, com `pipenv shell`
3. Crie um ambiente virtual `pipenv install django` 
4. Active o ambiente virtual `pipenv shell`
5. Lance a aplicação no browser com o comando `python manage.py runserver`. 
6. Tem disponíveis as aplicações hello no link `http://127.0.0.1:8000`
7. abra a pasta com o Pycharm ou VS Code, para a explorar.
8. devera criar um superuser `python manage.py createsuperuser` para pode aceder ao modo admin e ditar diretamente a base de dados
9. aceda à aplicação admin, em  `http://127.0.0.1:8000/admin`
