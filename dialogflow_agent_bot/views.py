import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from services.request_handler import RequestHandler


@csrf_exempt
def index(request):
    if request.method == "POST":
        RequestHandler(params=json.loads(request.body)).process()
    return JsonResponse({"success": True})
