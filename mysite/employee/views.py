from django.shortcuts import render
try:
    from .forms import StudentForm
except ImportError:
    from employee.forms import StudentForm

def home(request):
    return render(request, 'home.html')

def form_demo(request):
    search_query = None

    # 1. Handling POST Request (Form Submission with Regex Validation)
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            # Data after regex validation passes
            name = form.cleaned_data['name']
            phone = form.cleaned_data['phone']
            return render(request, 'result.html', {
                'name': name,
                'phone': phone,
                'method': 'POST'
            })
    else:
        # 2. Handling GET Request (Empty Form or Query String)
        form = StudentForm()
        search_query = request.GET.get('search')  # Demonstrating GET data extraction

    return render(request, 'form.html', {
        'form': form,
        'search_query': search_query,
        'method': request.method
    })
