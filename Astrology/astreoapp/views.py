from django.shortcuts import render, redirect
from datetime import datetime
from .models import Zodiac, Horoscope
from .forms import ZodiacForm, HoroscopeForm

# Utility function
def _time_of_day():
    hour = datetime.now().hour
    if hour < 12:
        return 'Good Morning'
    elif hour < 16:
        return 'Good Afternoon'
    else:
        return 'Good Evening'

# Home page view
def home(request):
    return render(request, 'home.html')

# View horoscope page (select zodiac)
def horoscope(request):
    zodiacs = Zodiac.objects.all()
    selected_zodiac = request.GET.get('zodiac')
    horoscope_data = None

    if selected_zodiac:
        horoscope_data = Horoscope.objects.filter(
            zodiac__name__iexact=selected_zodiac
        ).order_by('-date').first()

    context = {
        'time_of_day': _time_of_day(),
        'zodiacs': zodiacs,
        'selected_zodiac': selected_zodiac,
        'horoscope_data': horoscope_data
    }
    return render(request, 'horoscope.html', context)

# Zodiac CRUD
def zodiac_list(request):
    zodiacs = Zodiac.objects.all()
    return render(request, 'zodiac_list.html', {'zodiacs': zodiacs})

def zodiac_create(request):
    form = ZodiacForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('zodiac_list')
    return render(request, 'zodiac_form.html', {'form': form})

# Horoscope CRUD
def horoscope_list(request):
    horoscopes = Horoscope.objects.all().order_by('-date')
    return render(request, 'horoscope_list.html', {'horoscopes': horoscopes})

def horoscope_create(request):
    form = HoroscopeForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('horoscope_list')
    return render(request, 'horoscope_form.html', {'form': form})
