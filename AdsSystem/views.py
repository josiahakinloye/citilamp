from django.shortcuts import render

from .models import NewAdsForm
# Create your views here.

def new_ad(request):
    """
    View for posting new ads
    :param request:
    :return:
    """
    if request.method == "POST":
        form = NewAdsForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = NewAdsForm()
    return render(request,'newad.html', {'form': form} )