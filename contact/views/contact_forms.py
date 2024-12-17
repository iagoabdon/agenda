from django.core.paginator import Paginator
from django.db.models import Q
from django.shortcuts import get_object_or_404, redirect, render
from django import forms

from contact.models import Contact

#### copiando meu formulario contact 
class ContactForm(forms.ModelForm):
      class Meta:
             model = Contact
             fields = (
                    'first_name', 'last_name', 'phone', 
                    )
             



def create(request):
       if request.method == 'POST':
            context = {
              'form': ContactForm(request.POST)
            }
            
            return render(
             request,
             'contact/create.html',
             context )
     

       ## quando form e atualizado usando o metodo get
       context = {
       'form' : ContactForm()
       }

       return render(
             request,
             'contact/create.html',
             context
       )