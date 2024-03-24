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
- Montar páginas (Templates);<br>
- Interagir com diversos bancos de dados (ORM);<br>
- Validar input dos usuários (Forms);<br>
- Controlar acesso (Authorization);<br>
- Gerenciar a aplicação (Admin).<br>
<br>
Instalar o ambiente virtual para garantir que todos os pacotes e instalações vão ser feitas localmente.<br>
Criar ambiente virtual:<br>
1 - pip install virtualenv <br>
2 - python -m venv (nome do embiente virtual que vamos criar) <br>
exemplo -> python -m venv cadastro_curso_womakers <br>
3 - Ativar o embiente virtual -> entra na pasta que acabou de criar e colocar no terminal nome_ambiente.\Scripts\activate <br>
4 - Entrar dentro da pasta craiada e ativar novamente o ambiente virtual <br>
Criação do projeto e instalar as ferramentas:<br>
5 - Instalar o django - pip install django (dentro da pasta de ambiente virtual)<br>
6 - Criar o projeto -> django-admin starproject (nome do projeto)<br> 
exemplo-> django-admin startproject projeto_womakers .(onde vai ficar as configurações) o ponto é importante colocar para não ser criado 2 pastas<br>
7 - Comando python manage.py runserver (rodar o servidor) <br>
Criar aplicativo<br>
8 - python manage.py startapp App_NAME ex de name:base (criar o aplicativo), onde fica as funcionalidades.Dentro da pasta do projeto<br>
9 - Ir no setting.py e registrar o aplicativo que foi criado (no Instaled_APPS) <br>
10 - Testar rodando novamente o servidor <br>
11 - Comecar pelas views <br>
<br><br>
- Para criar a parte admin - python manage.py createsuperuser <br>
<br><br>
Rest Api -> pip install djangorestframework<br>
caso esse comando dê algum problema fazer python -m pip install djangorestfremework
fazer as configurações -> settings.py ->INSTALLED_APPS e colocar 'rest_framework'<br>
<br>
Proxima configuração é adicionar um browser paper api que é como se fosse um administrador(é opcional)-> entrar no arquivo urls.py ->adicionar uma nova url ('api-auth'/include(rest-framework.urls))<br>
Após isso rodar o comando python .\manange.py startapp rest_api cria o aplicativo res_api onde vamos criar de uma forma que possibilita que outros aplicativos se conecete a eles.<br>
depois de criar ,registrar no settings.py,no INSTALLED_APPS 'rest_api".<br>
<br>
*Sigla Rest significa transferencia do estado representacional.
Apos isso ir para a views e fazer as imposrtações.
<br>
após o código na views, importar a views na urls.py<br>
<br>
<br>
Serializers ->
<br>
<br>
<br>
# Testes -><br>
Tipos de Testes:<br>
- Funcional -> testes de unidade,teste de interface, teste de regressão, entre outros.
- Unitário -> Qualquer função, procedimento, método ou módulo pode ser uma unidade testada.
- Integração -> testa módulos em grupo.
- Não funcional-> funcionalidades testadas sob cargas.
- Usuabilidade -> interação humano - computador.
- Desempenho -> determina a velocidade, estabilidade e escabilidade em grupo.
<br>

Para fazer os testes:
Instalar a biblioteca de testes com o comando: pip install pytest-django.
Depois instalar : pip install pytest
Depois fazer as configurações para rodar o pytest -> na raiz do projeto criar arquivo pytest.ini
colocar:
[pytest]
DJANGO_SETTINGS_MODULE = <nome do projeto>.settings
python_files = tests.py test_*.py *_test.py
Depois rodar no terminal o comando pytest
