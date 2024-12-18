

from django.shortcuts import render ## erros e redirecionar pag

 

from contact.forms import ContactForm



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