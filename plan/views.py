from django.shortcuts import render, render_to_response

# Create your views here.
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def plan(request):
    return render_to_response('plan.html', {})
