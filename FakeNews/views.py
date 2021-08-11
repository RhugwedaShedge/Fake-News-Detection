from django.shortcuts import render
from django.http import HttpResponse
import nltk
from nltk.corpus import stopwords
from .Testing import testing
# Create your views here.

stop = stopwords.words('english')
funct = lambda x: ' '.join([word for word in x.split() if word not in (stop)])

def homePage(request):
    text = ""
    news = ""
    
    if request.method == 'POST':
        text = request.POST.get('news')

    if text:
        text = funct(text)
        prediction = testing([text])

        if prediction[0] == 0:
            news = "Fake News"
        else:
            news = "True News"

    context = {
            'news': news
    }

    return render(request, 'index.html', context)



    

