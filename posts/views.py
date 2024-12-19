import time
from django.http import JsonResponse
from django.shortcuts import render
from posts import views

def index(request):
    return render(request, "posts/index.html")

def posts(request):
    start = int(request.GET.get("start") or 0)
    end = int(request.GET.get("end") or (start + 9))

    data = [f"Post #{i}" for i in range(start, end + 1)]

    time.sleep(1)  # Simulate delay

    return JsonResponse({"posts": data})
