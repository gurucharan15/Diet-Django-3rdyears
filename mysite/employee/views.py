from django.shortcuts import render

# Create your views here.
def home(request):
    context = {
        'title': 'Employee Management System',
        'message': 'Welcome to Employee Portal',
        'employees': [
            {'id': 101, 'name': 'Alex Johnson', 'role': 'Software Engineer', 'department': 'Engineering', 'status': 'Active'},
            {'id': 102, 'name': 'Sarah Williams', 'role': 'UI/UX Designer', 'department': 'Design', 'status': 'Active'},
            {'id': 103, 'name': 'Michael Chen', 'role': 'Project Manager', 'department': 'Operations', 'status': 'On Leave'},
            {'id': 104, 'name': 'Emily Davis', 'role': 'QA Lead', 'department': 'Quality Assurance', 'status': 'Active'},
        ],
        'total_employees': 4,
        'departments_count': 3,
    }
    return render(request, 'home.html', context)

