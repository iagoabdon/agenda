from django import forms # import modulo de formulario 
from django.core.exceptions import ValidationError ## validação de erros 
from . import models


class ContactForm(forms.ModelForm):
    first_name = forms.CharField(
     widget=forms.TextInput(
     attrs={
        'class': 'class-a class-b',
        'placeholder': 'Escreva aqui',
     }),
         label='Primeiro nome',
         help_text= 'texto de ajuda para usuario'
    )
    


    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
        
    #     self.fields['first_name'].widget.attrs.update({
    #         'class': 'class-a class-b',
    #         'placeholder': 'Escreva aqui',
    #     })




    class Meta:
        model = models.Contact
        fields = (
            'first_name', 'last_name', 'phone',
        )
    def clean(self):
        cleaned_data = self.cleaned_data
        first_name = cleaned_data.get('first_name')
        last_name = cleaned_data.get('last_name')

        if first_name == last_name:
            msg = ValidationError(
                'Primeiro nome não pode ser igual ao segundo',
                code='invalid'
            )
            self.add_error('first_name', msg)
            self.add_error('last_name', msg)

        return super().clean()

    def clean_first_name(self):
        first_name = self.cleaned_data.get('first_name')

        if first_name == 'ABC':
            self.add_error(
                'first_name',
                ValidationError(
                    'Veio do add_error',
                    code='invalid'
                )
            )
        print(first_name)
        return first_name
    
             