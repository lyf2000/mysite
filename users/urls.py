from django.urls import path

from users.views import (
    index,
    MD5View,
    MD5HashView,
    HelmanGetKeysView,
    HelmanCalcKeysView,
)

urlpatterns = [
    path("api/md5/<username>", MD5View.as_view()),
    path("api/md5-hash/<hash>", MD5HashView.as_view()),
    path("api/helman/", HelmanGetKeysView.as_view()),
    path("api/helman-calc/<key>", HelmanCalcKeysView.as_view()),
    path("", index, name="index"),
]
