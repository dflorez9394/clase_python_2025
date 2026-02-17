from django.http import HttpResponse
from django.views.generic.base import View
from django.shortcuts import render

class HelloWord(View):
    def get(self,request):
        #return HttpResponse("DANIEL") para devolver una respuesta Response http
        # desde la url   recibe y mapea el parametro a utilizar
        name = request.GET.get("name",'Invalido')
        data={
            'name':name,
            'age':18,
            'description':'El curso de python es este bueno',
            'topics':[ 'views', 'RestApi','Admin','CRUD','FOR','WHILE'],
            'teachers':[]
        }
        return render(request,"hello_word.html",context=data)
