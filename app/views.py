from django.shortcuts import render

# Create your views here.


def set_session(request):
    request.session['name'] = 'Tony Stark'
    return render(request, 'set.html')

def get_session(request):
    if 'name' in request.session:
        return_value = request.session['name']
    return render(request, 'get.html', {'return_value':return_value})

def del_session(request):
    request.session.flush()
    return render(request, 'del.html')