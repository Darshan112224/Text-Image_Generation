# generator/views.py

from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .utils import generate_anime_image

def home_view(request):
    return render(request, 'home.html')

@csrf_exempt
def generate_image_view(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        prompt = data.get('prompt', '')

        if not prompt:
            return JsonResponse({'error': 'Prompt is required'}, status=400)

        try:
            img_base64 = generate_anime_image(prompt)  # Generate the image
            return JsonResponse({'image': img_base64})  # Return base64 encoded image
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)

    return JsonResponse({'error': 'Invalid method'}, status=405)

