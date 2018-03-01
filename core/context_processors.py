from django.conf import settings


def google_maps_key(request):
    return {'GOOGLE_MAPS_KEY': settings.GOOGLE_MAPS_KEY}
