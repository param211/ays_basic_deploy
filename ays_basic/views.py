from django.shortcuts import render, redirect


def index(req):
    return render(req, 'welcome.html')
