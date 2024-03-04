1 - pip install virtualenv
2 - python -m venv +(nome do embiente virtual que vamos criar) exemplo -> python -m venv cadastro_curso_womakers
3 - Ativar o embiente virtual -> entra na pasta que acabou de criar e colocar no terminal .\Scripts\activate
4 - Entrar dentro da pasta craiada e ativar novamente o ambiente virtual
5 - Instalar o django - pip install django
6 - Criar o projeto -> django-admin starproject (nome do projeto) -> django-admin startproject projeto_womakers .(onde vai ficar as configurações)
7 - Comando python manage.py runserver (rodar o servidor)
8 - python manage.py startapp base (criar o aplicativo), onde fica as funcionalidades.
9 - Ir no setting.py e registrar o aplicativo que foi criado (no Instaled_APPS)
10 - Testar rodando novamente o servidor
11 - Comecar pelas views