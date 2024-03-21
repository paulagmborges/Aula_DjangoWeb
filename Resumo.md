Framework - Padrões<br>
MVT - estrutura:<br>
- URL (caminho para acessar)
- View(Lógica do processamento). <br>
- Model(Camada de dados,estrutura do banco de dados). <br>
- tamplte(Frint-end.Como os dados são renderizados-html-CSS_JS).<br>
MVC - estrutura:
-User - usuario
-View
-Controller(recebe e responde as solicitaçôes do usuario)
-Model(dados)
<br>
Framework - django - MTV<br>
- Montar páginas (Templates);
- Interagir com diversos bancos de dados (ORM);
- Validar input dos usuários (Forms);
- Controlar acesso (Authorization);
- Gerenciar a aplicação (Admin).
<br>
Instalar o ambiente virtual para garantir que todos os pacotes e instalações vão ser feitas localmente.
Criar ambiente virtual:
1 - pip install virtualenv <br>
2 - python -m venv (nome do embiente virtual que vamos criar) <br>
exemplo -> python -m venv cadastro_curso_womakers <br>
3 - Ativar o embiente virtual -> entra na pasta que acabou de criar e colocar no terminal nome_ambiente.\Scripts\activate <br>
4 - Entrar dentro da pasta craiada e ativar novamente o ambiente virtual <br>
Criação do projeto e instalar as ferramentas:
5 - Instalar o django - pip install django (dentro da pasta de ambiente virtual)<br>
6 - Criar o projeto -> django-admin starproject (nome do projeto)<br> 
exemplo-> django-admin startproject projeto_womakers .(onde vai ficar as configurações) o ponto é importante colocar para não ser criado 2 pastas<br>
7 - Comando python manage.py runserver (rodar o servidor) <br>
Criar aplicativo
8 - python manage.py startapp App_NAME ex de name:base (criar o aplicativo), onde fica as funcionalidades.Dentro da pasta do projeto<br>
9 - Ir no setting.py e registrar o aplicativo que foi criado (no Instaled_APPS) <br>
10 - Testar rodando novamente o servidor <br>
11 - Comecar pelas views <br>

- Para criar a parte admin - python manage.py createsuperuser <br>