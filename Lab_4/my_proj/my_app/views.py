from django.views import View
from django.shortcuts import render, redirect
from . import my_functions, my_objects

#Part 1
def fix_name(name: str):
    new_name = name.title()
    return new_name

#Part 2
names = ['Rich', 'Richie', 'Randy']

#Part 3
fixed_names = my_functions.fix_names_list(names)

#Part 4, 5, 6
car1 = my_objects.car(color = 'blue', sound = 'honk honk')
car2 = my_objects.car(color = 'yellow', sound = 'beep beep')
motorcycle1 = my_objects.motorcycle(color = 'red', sound = 'vroom vroom')

class HomePageView(View):

    def get(self, request):

        orig_name = "RICHARD"
        name = fix_name(orig_name)

        context = {'hi':'hello world!',
                       'name' : name,
                       'orig_name' : orig_name,
                       'names' : names,
                       'fixed_names' : fixed_names,
                       'car1' : car1,
                       'car2' : car2,
                       'motorcycle1' : motorcycle1
                       }

        return render(request, 'my_app/index.html', context)
    

    