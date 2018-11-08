from django.shortcuts import render, redirect, get_object_or_404
from .models import Contact
from .forms import ContactForm

def say_hello(request):
    contact = Contact.objects.all()
    return render(request, "contacts/index.html", {'contact':contact})

def add_contact(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        form.save()
        return redirect("/")
    else:    
        form = ContactForm()
        return render(request, "contacts/add_contact.html", {'form': form })


  
def edit_contact(request, id):
    contact = get_object_or_404(Contact, pk=id)
    if request.method == "POST":
        form = ContactForm(request.POST, instance=contact)
        form.save()
        return redirect("/")
    else:        
        form=ContactForm(instance=contact)
        return render(request, "contacts/add_contact.html", {'form': form })