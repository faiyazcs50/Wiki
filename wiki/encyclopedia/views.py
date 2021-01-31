from django.shortcuts import render
from . import util
import os
from django import forms
import random

form = forms.Form()

def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def Entry(request, name):
    if util.get_entry(name) is None:
        return render(request, "encyclopedia/not_found.html",{
            "name": name
        })
    else:
        return render(request, f"encyclopedia/{name}.html")

def random_selector(request):
    return Entry(request,random.choice( util.list_entries()))