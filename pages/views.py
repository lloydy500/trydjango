from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home_view(request, *args, **kwargs):
    print(args, kwargs)
    print(request.user)
    # return HttpResponse("<h1>Hello World!</h1>") # string of HTML code
    return render(request, "home.html", {})
def contact_view(request, *args, **kwargs):
    # return HttpResponse("<h1>Contact View!</h1>") # string of HTML code
    my_context = {
        "title": "The is 'title' tag",
        "my_number": 7849182,
        "my_list": [123, 456, "Yo!"],
        "this_is_true": True,
        "my_html": "<h1>This was rendered using the 'safe' tag </h1>",
        "slugged_and_stripped": "<h2>This used to be a normal string with h2 tags</h2>"
    }

    return render(request, "contact.html", my_context)
