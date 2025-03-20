from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from django.http import JsonResponse

def home(request):
    return JsonResponse({"message": "Welcome to the Average Calculator API!"})

@csrf_exempt
def calculate_average(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            numbers = data.get('numbers', [])

            if not isinstance(numbers, list):
                return JsonResponse({'error': 'Input must be a list of numbers.'}, status=400)

            if not numbers:
                return JsonResponse({'error': 'The list of numbers cannot be empty.'}, status=400)

            if not all(isinstance(num, (int, float)) for num in numbers):
                return JsonResponse({'error': 'All elements in the list must be numbers.'}, status=400)

            average = sum(numbers) / len(numbers)
            return JsonResponse({'average': average})

        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON data.'}, status=400)
        except ZeroDivisionError:
            return JsonResponse({'error': 'Division by zero occurred.'}, status=400)
        except Exception as e:
            return JsonResponse({'error': f'An unexpected error occurred: {str(e)}'}, status=500)

    elif request.method == 'GET':
        return JsonResponse({
            'message': 'Welcome to the Average Calculator API.',
            'instructions': 'Send a POST request with a JSON payload to calculate the average.',
            'example_request': {
                'numbers': [10, 20, 30, 40, 50]
            },
            'example_response': {
                'average': 30.0
            }
        })

    else:
        return JsonResponse({'error': 'Only GET and POST methods are allowed.'}, status=405)