from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic.base import View

class HelloWord(View):
    def get(self, request):
        data={
            'name': 'Oscar Ivan',
            'age': 30,
            'description': 'Curso de Python',
            'topics': ['Python', 'Django', 'JavaScript'],
            'teacher':['Oscar', 'Ivan', 'Rodriguez']
        }
        return render(request, "hello_world.html", context=data)