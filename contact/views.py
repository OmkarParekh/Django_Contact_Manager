from django.shortcuts import redirect, render
from .models import Contact
from django.contrib import messages
# Create your views here.
def contact(request):
     data=Contact.objects.all()
     return render(request, 'contact.html',{'data':data,'url':request.get_full_path})
def addcontact(request):
     if request.method=='POST':
          name=request.POST['name']
          email=request.POST['email']
          number=request.POST['number']
          data=Contact(Name=name ,email=email,Number=number)
          data.save()
          messages.info(request, 'Contact has Been Created')
          return redirect("/contact/")
     return render(request, 'Add.html',{'url':request.get_full_path})
def delete(request ,id):
     data=Contact.objects.get(id=id)
     data.delete()
     messages.info(request, 'Contact has Been Deleted')
     return redirect("/contact/")
  
def edit(request ,id):
     data=Contact.objects.get(id=id)
     if request.method=='POST':
          name=request.POST['name']
          email=request.POST['email']
          number=request.POST['number']
          data.Name=name
          data.email=email
          data.Number=number
          data.save()
          messages.info(request, 'Contact has Been Updated')
          return redirect("/contact/")
     return render(request, 'edit.html',{'url':request.get_full_path ,'data':data})
  