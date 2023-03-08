from django.shortcuts import render
from base.forms import PostCv

# Create your views here.
def form_view(request):
    form = PostCv()
    context = {"form":form}
    return render(request, "cvform.html", context)