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
Assign instance of a model to variable e.g.
    product = Product.objects.get(id=1)
Get the python/django functions that can be called on it
    dir(product)
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
{% extends "base.html" %}
    {% for sub_data in my_data %}
        {% sub_data %}
    {% endfor %}
-------------------
FORMS
-------------------
create forms.py inside the model folder e.g. proucts/forms.py
-------------------
from django import forms
from .models import Product

    class ProductForm(forms.ModelForm):
        class Meta:
            model = Product
            fields = [
                'title',
                'description',
                'price'
            ]

then make a template in products/templates/products e.g. product_create.html
    {% extends 'base.html' %}

    {% block content %}
    <form method="POST"> {% csrf_token %}
        {{form.as_p}}
        <input type="submit" value="save">
    </form>
    {% endblock %}

then add function to views:

    def product_create_view(request):
        form = ProductForm(request.POST or None)
        if form.is_valid():
            form.save()

        context = {
            'form': form
        }
        return render(request, "product/product_create.html", context)

remember we need to python manage.py makemigrations then python manage.py migrate
whenever we change the model
-------------------

-------------------

-------------------
-------------------

-------------------
"""