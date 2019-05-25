from django.shortcuts import render
from .models import Word

def index(request):
    query = request.GET.get('q')
    if query:
        try:
            word = Word.objects.get(word_text=query)
        except Word.DoesNotExist:
            context = {'no_results': query}
            return render(request, "en_ka/index.html", context)
        return render(request, "en_ka/index.html", {'word': word})
    else:
        context = {'no_results': query}
        return render(request, "en_ka/index.html", context)

