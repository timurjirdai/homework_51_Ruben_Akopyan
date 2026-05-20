from django.shortcuts import render, redirect
from .cat import Cat

cat = None

def index(request):
    global cat
    if request.method == 'POST':
        name = request.POST.get('name')
        cat = Cat(name)
        return redirect('cat')

    return render(request, 'index.html')


def cat_view(request):
    global cat
    if not cat:
        return redirect('index')

    if request.method == 'POST':
        action = request.POST.get('action')

        if action == 'feed':
            cat.feed()

        elif action == 'play':
            cat.play()

        elif action == 'sleep':
            cat.sleep()

    if cat.happiness < 30:
        image = 'sad.png'
    elif cat.happiness < 70:
        image = 'normal.png'
    else:
        image = 'happy.png'

    context = {
        'cat': cat,
        'image': image
    }

    return render(request, 'cat.html', context)