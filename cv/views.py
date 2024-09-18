from django.http import HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
def index(request):
    # template = loader.get_template("polls/index.html")
    return render(request, "cv/index.html")