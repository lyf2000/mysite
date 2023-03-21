from django.contrib import admin
from django.urls import path, include

from users.views import index, MD5View, MD5HashView

urlpatterns = [
    path("api/md5/<username>", MD5View.as_view()),
    path("api/md5-hash/<hash>", MD5HashView.as_view()),
    path("", index, name="index"),
]
