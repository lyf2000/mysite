import hashlib
from datetime import datetime
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render

from users.models import CustomUser
from users.forms import CustomUserCreationForm


def index(request):
    if request.method == "POST":
        # регистрация
        form = CustomUserCreationForm(request.POST)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse("index"))
    else:
        form = CustomUserCreationForm()

    context = {
        "form": form,
    }
    # главная страница
    return render(request, "index.html", context=context)


from rest_framework.response import Response
from rest_framework.views import APIView

from django.conf import settings


class MD5View(APIView):
    def get(self, request, username):
        # задание метки пользователю и генерирование хэша по md5
        settings.USERNAME = username
        user = CustomUser.objects.filter(username=settings.USERNAME).first()
        if user:
            user.ts = int(datetime.now().timestamp())
            user.save()
            settings.HASH = str(hashlib.md5(str(user.ts).encode("utf-8")).hexdigest())
            return Response({"ts": settings.HASH})

        return Response(status=404)


class MD5HashView(APIView):
    def get(self, request, hash):
        # сверка хэшей
        user = CustomUser.objects.get(username=settings.USERNAME)
        a = hashlib.md5((user.password + settings.HASH).encode("utf-8")).hexdigest()
        if a != hash:
            return Response(status=404)
        return Response(status=200)


from random import randint


class HelmanGetKeysView(APIView):
    def get(self, request):
        # генерирование ключей
        settings.a = randint(1, 100)
        settings.A = (pow(settings.G, settings.a)) % settings.P
        a = dict(
            A=settings.A,
            g=settings.G,
            p=settings.P,
        )
        return Response(a)


class HelmanCalcKeysView(APIView):
    def get(self, request, key):
        # генерирование ключа К
        return Response(dict(K=((pow(int(key), settings.a)) % settings.P)))
