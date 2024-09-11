from django.shortcuts import render, redirect   # Tambahkan import redirect di baris ini
from main.forms import MoodEntryForm
from main.models import MoodEntry
from django.http import HttpResponse
from django.core import serializers

def show_main(request):
    mood_entries = MoodEntry.objects.all()

    context = {
        'npm' : '2306208363',
        'name': 'Edmond Christian',
        'class': 'PBP D',
        'mood_entries': mood_entries
    }

    return render(request, "main.html", context)
# Create your views here.

def create_mood_entry(request):
    form = MoodEntryForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        form.save()
        return redirect('main:show_main')

    context = {'form': form}
    return render(request, "create_mood_entry.html", context)


def show_xml(request):
    data = MoodEntry.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")


def show_json(request):
    data = MoodEntry.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")


def show_xml_by_id(request, id):
    data = MoodEntry.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")


def show_json_by_id(request, id):
    data = MoodEntry.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")
