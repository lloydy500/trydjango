"""
-------------------
CREATING A DJANGO PROJECT
-------------------
create a directory e.g. 
    mkdir lloydy500/trydjango
    cd trydjango
create venv in python3
    virtualenv .
    pip install django==2.1.5(or specify other version)
start venv
source bin/activate
check
    pip freeze
create src folder within venv
    mkdir src
    cd src
create a project with same name as venv
    django-admin startproject trydjango .
-------------------
MANAGE.PY COMMANDS
-------------------
    python manage.py runserver
-------------------
MIGRATIONS
-------------------
    python manage.py makemigrations
    python manage.py migrate
-------------------
PYTHON SHELL (interactive console)
-------------------
from the project root file:
    python manage.py shell
-------------------
MODEL COMMANDS
-------------------
When you add a model add the name to settings.py "INSTALLED_APPS".
E.g 'pages', 'products'
    Model.objects.all()
    Model.objects.create(name="test", description="test2")
-------------------
VIEWS
-------------------
inside the project's url.py file e.g.
    from appname.view (e.g. pages.views) import view_function_name (e.g. home_view)
then add route to urlpatterns array e.g.
    path('', view_function_name (e.g. home_view), name='function_name'(e.g. 'home'))
    path('admin/', admin.site.urls)
-------------------
TEMPLATES
-------------------
in settings.py we need to specify where django will find our templates
you can pass "context" as data i.e a python dictionary in the view
then pass the context as a parameter in the return statement for that view
we can access that data from within the templates using loops, counters etc.
e.g. inside templates/"contacts.html"
-------------------
    {% for sub_data in my_data %}
        {% sub_data %}
    {% endfor %}
-------------------
-------------------

-------------------
-------------------

-------------------
-------------------

-------------------
"""