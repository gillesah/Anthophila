from django.shortcuts import render, get_object_or_404
from anthophila_app.models import Beeyard, Beehive, Status, User


def index_view(request):
    context = {'beeyards':  Beeyard.objects.all(
    ),  'beehives': Beehive.objects.all(), 'status': Status.objects.all(), "beekeepers": User.objects.all()}

    # if the user is authenticated, he can see his elements.
    if request.user.is_authenticated:
        user_beeyards = Beeyard.objects.filter(beekeeper=request.user)
        context['user_beeyards'] = user_beeyards

    return render(request, 'index.html', context)


def beekeeper_view(request, beekeeper_id):
    beekeeper = get_object_or_404(User, pk=beekeeper_id)

    context = {'beeyards':  Beeyard.objects.filter(beekeeper=beekeeper),
               'beehives': Beehive.objects.all(),
               'status': Status.objects.all(),
               "beekeepers": User.objects.all()}
    return render(request, 'beekeeper.html', context)
