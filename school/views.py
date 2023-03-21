from django.http import JsonResponse

def students(request):
    if request.method == 'GET':
        student = {'id': 1, 'name': 'Pedro Ivo'}
        return JsonResponse(student)
