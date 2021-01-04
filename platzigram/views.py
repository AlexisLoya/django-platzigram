# Django
from django.http import HttpResponse
from django.http import JsonResponse

# Utilities
from datetime import datetime

def hello_world(request):
    """Return a greeting."""
    return HttpResponse('Oh, hi! Current server time is {now}'.format(
        now=datetime.now().strftime('%b %dth, %Y - %H:%M hrs')
    ))

def hi(request):
    sorted_numbers = sorted(request.GET['numbers'].split(','))
    data = {
        'status': 'ok',
        'numbers': sorted_numbers,
        'message': 'sorted_numbers successfully.'

    }
    return JsonResponse(data, safe=False)