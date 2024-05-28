from django.http import HttpResponse, JsonResponse

def home_page(request):
    print('Home page requested')
    test = ['t1', 't2', 't3']
    return JsonResponse(test, safe=False)