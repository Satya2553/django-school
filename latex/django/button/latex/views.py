from django.shortcuts import render
from django.shortcuts import render
from django.http import HttpResponse
from .models import Text
import pypandoc
# Create your views here.
def Hello(request):
    plaintexts=Text.objects.all()
    return render(request, 'sample.html', {'plaintexts': plaintexts})
def store(request):
    if request.method == 'POST':
        plaintext=request.POST.get('plaintext')
        Text.objects.create(plaintext=plaintext)
        plaintexts=Text.objects.all()
        return render(request, 'sample.html', {'plaintexts': plaintexts})
def add(request):
    if request.method == 'POST':
        plaintext=request.POST.get('plaintext')
        x=Text.objects.last()
        plaintext = x.plaintext+" "+plaintext
        x.delete()
        Text.objects.create(plaintext=plaintext)
        plaintexts=Text.objects.all()
        return render(request, 'sample.html', {'plaintexts': plaintexts})
def conv(request):
    if request.method == 'POST':
        latex_text = request.POST.get('latextext')
        latextext = pypandoc.convert_text(latex_text, 'plain', format='latex')
        x=Text.objects.last()
        plaintext = x.plaintext+" "+latextext
        x.delete()
        Text.objects.create(plaintext=plaintext)
        plaintexts=Text.objects.all()
        return render(request, 'sample.html', {'plaintexts': plaintexts})
def final(request):
    if request.method == 'POST':
        x=Text.objects.last()
        x.finaltext=x.plaintext
        Text.objects.create(finaltext=x.finaltext)
        x.delete()
        plaintexts=Text.objects.all()
        for x in plaintexts:
            if x.finaltext is None or x.finaltext == "":
                x.delete()
            # if x.plaintext is not None:
            #     x.plaintext=None
            #     Text.objects.update(plaintext=None)
        plaintexts=Text.objects.all()
        return render(request, 'sample.html', {'plaintexts': plaintexts})