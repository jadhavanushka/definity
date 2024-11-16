import requests
from django.shortcuts import render
from django.conf import settings

def get_word_definition(request):
    word = request.GET.get('word', '')  # Get the word from the query parameter
    
    # If there's a word in the query
    if word:
        # Prepare the API request URL
        url = f"https://www.dictionaryapi.com/api/v3/references/collegiate/json/{word}?key={settings.DICTIONARY_API_KEY}"
        response = requests.get(url)
        
        if response.status_code == 200:
            # Parse the response JSON
            data = response.json()
            
            # Check if the response contains results
            if data:
                return render(request, 'dictionary/definition.html', {'data': data})
            else:
                error = "No results found for this word."
        else:
            error = "Error fetching data from the dictionary API."
    else:
        error = "Please enter a word to search."
    
    return render(request, 'dictionary/definition.html', {'error': error})
