from django.shortcuts import render
from anthophila_app.models import Beeyard, Beehive, Status


def index_view(request):
    user_beeyards = Beeyard.objects.filter(beekeeper=request.user)
    user_beehives = Beehive.objects.filter(beeyard__in=user_beeyards)
    beehive_status = Status.objects.filter(beehive__in=user_beehives)
    return render(request, 'index.html', {'beeyards': user_beeyards, 'beehives': user_beehives, 'status': beehive_status})
