from django.shortcuts import render

# Create your views here.
from django.views import generic

from catalog.models import Fighter


def index(request):
    fighters = Fighter.objects.all()
    print(fighters)
    context = {
        'fighters': fighters,
    }
    return render(request, 'index.html', context=context)

class FighterListView(generic.ListView):
    model = Fighter
    paginate_by = 10


class FighterDetailView(generic.DetailView):
    model = Fighter