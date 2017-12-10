from django.shortcuts import render

from .forms import NewAdForm


# Create your views here.

def new_ad(request):
    """
    View for posting new ads
    :param request:
    :return:
    """
    if request.method == "POST":
        form = NewAdForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = NewAdForm()
    return render(request,'newad.html', {'form': form} )