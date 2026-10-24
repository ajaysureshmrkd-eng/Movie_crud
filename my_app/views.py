from django.shortcuts import render

from django.views.generic import View

from my_app.models import Moive

from django.http import JsonResponse

from json import loads

from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

# Create your views here.

@method_decorator(csrf_exempt,name="dispatch")
class MovieCreateListView(View):

    def get(self,request):

        qs =Moive.objects.all().values()

        moive_lst =list(qs)

        return JsonResponse (moive_lst,safe=False)

    def post(self,request):

        form_data =loads(request.body)

        Moive.objects.create(
            title ="Manjummel Boys",
            language ="Malayalam",
            year =2024,
            run_time =154
        )

        return JsonResponse({"message":"created..."})


@method_decorator(csrf_exempt,name="dispatch")
class MovieRetrieveUpdateDeleteView(View):

    def get(self,request,pk=None):

        qs =Moive.objects.filter(id=pk).values()

        movie_lst =list(qs)

        return JsonResponse(movie_lst,safe=False)

    def delete(self,request,pk=None):

        qs =Moive.objects.get(id=pk).delete()

        movie_lst =list(qs)

        return JsonResponse ({"message":"delete"})