from django.shortcuts import render
from anthophila_app.models import Beeyard


def index_view(request):
    user_beeyards = Beeyard.objects.filter(beekeeper=request.user)
    return render(request, 'index.html', {'beeyards': user_beeyards})
