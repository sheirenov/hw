from django.shortcuts import render

# Create your views here.

def calculate_view(request):
    return render(request, 'calculate.html')

def result_view(request):
    context = {
        'first': request.POST.get('first'),
        'second': request.POST.get('second'),
        'action': request.POST.get('action')
    }
    if context['action'] == 'add':
        a = {'result': int(context['first']) + int(context['second'])}
        context.update(a)
        action_sign = {'action_sign': '+'}
        context.update(action_sign)
    elif context['action'] == 'subtract':
        a = {'result': int(context['first']) - int(context['second'])}
        context.update(a)
        action_sign = {'action_sign': '-'}
        context.update(action_sign)
    elif context['action'] == 'multiply':
        a = {'result': int(context['first']) * int(context['second'])}
        context.update(a)
        action_sign = {'action_sign': '*'}
        context.update(action_sign)
    else:
        a = {'result': int(context['first']) / int(context['second'])}
        context.update(a)
        action_sign = {'action_sign': '/'}
        context.update(action_sign)
    return render(request, 'result.html', context)