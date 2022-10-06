from django.shortcuts import render

# Create your views here.


def set_session(request):
    request.session['name'] = 'Tony Stark'
    return render(request, 'set.html')

def get_session(request):
    if 'name' in request.session:
        return_value = request.session['name']
    keys = request.session.keys()
    items = request.session.items()
    return render(request, 'get.html', {'return_value':return_value, 'keys':keys, 'items':items})

def del_session(request):
    request.session.flush()
    return render(request, 'del.html')