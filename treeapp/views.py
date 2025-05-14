from django.shortcuts import render

def index(request):
    return render(request, 'treeapp/index.html')

def about(request):
    return render(request, 'treeapp/about.html')

def contact(request):
    return render(request, 'treeapp/contact.html')

def main_menu_view(request):
    return render(request, 'treeapp/main_menu.html')

def home(request):
    return render(request, 'treeapp/home.html')

def base(request):
    return render(request, 'treeapp/base.html')

def menu(request):
    return render(request, 'treeapp/menu.html')

def menu_item(request):
    return render(request, 'treeapp/menu_item.html')

def help(request):
    return render(request, 'treeapp/help.html')
def news_view(request):
    return render(request, 'treeapp/news.html')
