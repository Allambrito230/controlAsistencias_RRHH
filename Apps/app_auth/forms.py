# login/forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User, Group

class CustomUserCreationForm(UserCreationForm):
    # Si quieres permitir elegir uno o varios grupos, puedes utilizar un ModelMultipleChoiceField
    # o ModelChoiceField, dependiendo si quieres permitir múltiples grupos o solo uno.
    groups = forms.ModelMultipleChoiceField(
        queryset=Group.objects.all(),
        required=False,
        widget=forms.CheckboxSelectMultiple,  # o forms.SelectMultiple
        label="Grupos"
    )
    
    class Meta:
        model = User
        fields = ("username", "first_name", "last_name", "email", "password1", "password2", "groups")
        # Puedes ajustar los fields a tu gusto

    def save(self, commit=True):
        # Guardamos el usuario
        user = super().save(commit=False)
        if commit:
            user.save()
        # Asignamos los grupos seleccionados
        if self.cleaned_data["groups"]:
            user.groups.set(self.cleaned_data["groups"])
        return user
