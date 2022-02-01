from django.shortcuts import render,redirect


# Create your views here.
def index(request):
    return render(request, 'main/index.html')


def meetings(request):
    return render(request, 'main/meetings.html')


def meeting_details(request):
    return render(request, 'main/meeting-details.html')


def about(request):
    return render(request, 'main/about.html')


def wiki(request):
    return render(request, 'main/wiki.html')


