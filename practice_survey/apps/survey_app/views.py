from django.shortcuts import render, redirect


def process(request):
    if 'number' not in request.session:
        request.session['number'] = 0
    if request.method == "POST":
        request.session['number'] += 1
        request.session['name'] = request.POST['name']
        request.session['location'] = request.POST['location']
        request.session['language'] = request.POST['language']
        request.session['comment'] = request.POST['comment']
        return redirect('/result')
    return redirect('/')

def result(request):
    context = {
        'number': request.session['number'],
        'name': request.session['name'],
        'location': request.session['location'],
        'language': request.session['language'],
        'comment': request.session['comment'],
    }
    return render(request, 'survey_app/result.html', context)


def survey(request):
    return render(request, 'survey_app/index.html' )