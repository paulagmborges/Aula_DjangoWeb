Framework - Padrões<br>
MVT - estrutura:<br>
- Model(Camada de dados,estrutura do banco de dados). <br>
- View(Lógica do processamento). <br>
- tamplte(Como os dados são renderizados-html-CSS_JS).<br>
MVC - estrutura:<br>
-User
-View()
-Controller(recebe e responde as solicitaçôes do usuario)
-Model(dados)
<br>
Framework - django - MTV<br>
<br>
Instalar o ambiente virtual para garantir que todos os pacotes e instalações vão ser feitas localmente.
1 - pip install virtualenv <br>
2 - python -m venv +(nome do embiente virtual que vamos criar) exemplo -> python -m venv cadastro_curso_womakers <br>
3 - Ativar o embiente virtual -> entra na pasta que acabou de criar e colocar no terminal .\Scripts\activate <br>
4 - Entrar dentro da pasta craiada e ativar novamente o ambiente virtual <br>
Instalar as ferramentas:
5 - Instalar o django - pip install django <br>
6 - Criar o projeto -> django-admin starproject (nome do projeto) -> django-admin startproject projeto_womakers .(onde vai ficar as configurações) o ponto é importante colocar para não ser criado 2 pastas<br>
7 - Comando python manage.py runserver (rodar o servidor) <br>
8 - python manage.py startapp base (criar o aplicativo), onde fica as funcionalidades.<br>
9 - Ir no setting.py e registrar o aplicativo que foi criado (no Instaled_APPS) <br>
10 - Testar rodando novamente o servidor <br>
11 - Comecar pelas views <br>

Para criar a parte admin - python manage.py createsuperuser <br>