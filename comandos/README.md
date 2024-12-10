python -m venv venv
. venv/bin/activate
pip install django
django-admin startproject project .



git config --global user.name 'Seu nome'
git config --global user.email 'seu_email@gmail.com'
git config --global init.defaultBranch main
# Configure o .gitignore
git init
git add .
git commit -m 'Mensagem'
git remote add origin URL_DO_GIT


git log     --oneline

#repositorio
git push origin main 


#gerar chave ssh 
ssh-keygen -f ~/.ssh/iagoabdon_rsa

cat /c/Users/usuario/.ssh/iagoabdon_rsa.pub
ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIDPr1tMBMjjfMnVF/AOSk7luXD5Lqp17ZXraVNMx9pH1 usuario@WIN10PC


logar bash 

eval $(ssh-agent)

ssh-add ~/.ssh/iagoabdon_rsa



# Windao 


ssh-keygen -t ed25519 -C "iago.0206@hotmail.com"
 
type C:\Users\usuario/.ssh/id_ed25519



# Importe o módulo
from contact.models import Contact
# Cria um contato (Lazy)
# Retorna o contato
contact = Contact(**fields)
contact.save()
# Cria um contato (Não lazy)
# Retorna o contato
contact = Contact.objects.create(**fields)
# Seleciona um contato com id 10
# Retorna o contato
contact = Contact.objects.get(pk=10)
# Edita um contato
# Retorna o contato
contact.field_name1 = 'Novo valor 1'
contact.field_name2 = 'Novo valor 2'
contact.save()
# Apaga um contato
# Depende da base de dados, geralmente retorna o número
# de valores manipulados na base de dados
contact.delete()
# Seleciona todos os contatos ordenando por id DESC
# Retorna QuerySet[]
contacts = Contact.objects.all().order_by('-id')
# Seleciona contatos usando filtros
# Retorna QuerySet[]
contacts = Contact.objects.filter(**filters).order_by('-id')