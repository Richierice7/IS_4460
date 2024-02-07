from django.views import View
from django.shortcuts import render, redirect

def title_name(the_name: str):
    return the_name.title()

class HomePageView(View):
    def get(self, request):
     
        my_name = "RICHARD"
        new_name = title_name(my_name)
        the_context = {'hi':'hello CLASS!', 'name':new_name}

        return render(request, 'my_app/index.html', the_context)