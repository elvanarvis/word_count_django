from django.shortcuts import render, HttpResponse
from .forms import CountText
import string
# Create your views here.

def wordCount(request):
    print('word count view is running...')
    form = CountText(data=request.GET or None)
    if form.is_valid():
        txt = form.cleaned_data.get('txt')
        result = sum([i.strip(string.punctuation).isalpha() for i in txt.split()])
        print(txt)
        return render(request, 'word_count/word_count.html', context={'form':form, 'txt':txt, 'result':result})

    return render(request,'word_count/word_count.html', context={'form': form})
