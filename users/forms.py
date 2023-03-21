import hashlib
from django.contrib.auth.forms import UserCreationForm

from users.models import CustomUser


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ("username",)

    def save(self, *args, **kwargs):
        user = super().save(commit=False)
        user.password = str(
            hashlib.md5(self.cleaned_data["password1"].encode("utf-8")).hexdigest()
        )
        user.save()
        return user
