from django.shortcuts import render

def main(request):
    return render(request,'main/main.html')

def collections(request):
    return render(request,'main/collections.html')

def contacts(request):
    return render(request,'main/contacts.html')