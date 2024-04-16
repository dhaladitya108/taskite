from django.conf import settings

def organization_settings(request):
    return {"organization_settings": settings.ORGANIZATION_SETTINGS}
