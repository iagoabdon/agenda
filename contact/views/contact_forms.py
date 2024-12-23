

from django.shortcuts import redirect, render ## erros e redirecionar pag

 

from contact.forms import ContactForm



def create(request):
       if request.method == 'POST':
            form = ContactForm(request.POST)
            context = {
              'form': form
            }
            if form.is_valid():
             contact = form.save()
             contact.save()
             return redirect('contact:create')
            
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