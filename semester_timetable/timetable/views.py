from django.shortcuts import render

def timetable_view(request):
    timetable_data = {
        'Monday': ['Math', 'Physics', 'Chemistry'],
        'Tuesday': ['Biology', 'History', 'English'],
        'Wednesday': ['Math', 'Computer Science', 'PE'],
        'Thursday': ['Chemistry', 'Physics', 'Art'],
        'Friday': ['Biology', 'Math', 'History'],
    }
    return render(request, 'timetable.html', {'timetable': timetable_data})
