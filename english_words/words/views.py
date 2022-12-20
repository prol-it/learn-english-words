from django.shortcuts import render, redirect
from .models import Words
from .forms import AddWordForm

menu = ["Изучаемые слова", "Статистика",
        "Настройки", "Обратная связь", "Войти"]


def index(request):
    words_list = Words.objects.all()
    form = AddWordForm()

    if request.method == 'POST':
        form = AddWordForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('add_word')
    else:
        form = AddWordForm()

    return render(request, 'words/index.html', {'menu': menu, 'title': 'words', 'words': words_list, 'form': form})
