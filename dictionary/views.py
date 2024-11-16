import requests
from django.shortcuts import render
from django.conf import settings


def get_word_definition(request):
    word = request.GET.get("word", "")  # Get the word from the query parameter

    # If there's a word in the query

    # If there's a word in the query
    if word:
        # Prepare the API request URL
        url = f"https://www.dictionaryapi.com/api/v3/references/collegiate/json/{word}?key={settings.DICTIONARY_API_KEY}"
        response = requests.get(url)

        if response.status_code == 200:
            # Parse the response JSON
            data = response.json()

            if data and isinstance(data[0], dict):  # Ensure valid response
                meanings = []
                for entry in data:
                    if "shortdef" in entry:
                        meanings.append(
                            {
                                "headword": entry["hwi"]["hw"],  # The word itself
                                "part_of_speech": entry.get(
                                    "fl", "Unknown"
                                ),  # Part of speech
                                "definitions": entry["shortdef"],  # List of definitions
                            }
                        )

                return render(
                    request,
                    "dictionary/definition.html",
                    {"word": word, "meanings": meanings},
                )
            else:
                error = "No results found for this word."
        else:
            error = "Error fetching data from the dictionary API."
    else:
        error = "Please enter a word to search."

    return render(request, "dictionary/definition.html", {"error": error})
