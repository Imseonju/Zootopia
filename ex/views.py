from django.shortcuts import render, get_object_or_404
from ex.models import Character
# Create your views here.
def index(request):
    chars = Character.objects.all()
    context = {'chars' : chars}
    return render(request, 'index.html', context)

def detail(request, pk):
    char = get_object_or_404(Character, pk=pk)
    context = {'char' : char}
    return render(request, 'detail.html', context)