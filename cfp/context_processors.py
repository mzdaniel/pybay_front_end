from django.conf import settings


def conf_date(request):
    return {'conf_meta': settings.CONF_DATE_TEXT}
