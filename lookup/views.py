from django.shortcuts import render

def home(request):
    import json
    import requests

    api_request = requests.get('https://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=89129&distance=5&API_KEY=8685D647-7997-416C-B091-A27AC5B771E4')

    try:
        api = json.loads(api_request.content)
    except Exception as e:
        api = "Error....."
    
    return render(request, 'home.html', {'api':api})


def about(request):

    return render(request, 'about.html')

