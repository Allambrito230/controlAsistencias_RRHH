# login/forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User, Group

class CustomUserCreationForm(UserCreationForm):
    
    groups = forms.ModelMultipleChoiceField(
        queryset=Group.objects.all(),
        required=False,
        widget=forms.CheckboxSelectMultiple, 
        label="Grupos"
    )
    
    class Meta:
        model = User
        fields = ("username", "first_name", "last_name", "email", "password1", "password2", "groups")
      
    def save(self, commit=True):
        # Guardar
        user = super().save(commit=False)
        if commit:
            user.save()
       
        if self.cleaned_data["groups"]:
            user.groups.set(self.cleaned_data["groups"])
        return user
