import requests
from django.shortcuts import render
from django.conf import settings


def search(request):
    word = request.GET.get("word", "")  # Get the word from the query parameter

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
                pronunciations = []
                audios = []

                for entry in data:
                    if "shortdef" in entry:
                        pronunciation = None
                        audio = None

                        # Check for pronunciation
                        if "prs" in entry["hwi"]:
                            pronunciation = entry["hwi"]["prs"][0].get("mw")
                            pronunciations.append(pronunciation)

                            # Check for audio
                            if "sound" in entry["hwi"]["prs"][0]:
                                audio_file = entry["hwi"]["prs"][0]["sound"]["audio"]
                                audio = f"https://media.merriam-webster.com/audio/prons/en/us/mp3/{audio_file[0]}/{audio_file}.mp3"
                                audios.append(audio)

                        meanings.append(
                            {
                                "headword": entry["hwi"]["hw"],  # The word itself
                                "part_of_speech": entry.get(
                                    "fl", "Unknown"
                                ),  # Part of speech
                                "definitions": entry["shortdef"],  # List of definitions
                                "pronunciation": pronunciation,  # Modern IPA pronunciation
                                "audio": audio,  # Audio URL (if available)
                            }
                        )

                return render(
                    request,
                    "dictionary/results.html",
                    {
                        "word": word,
                        "meanings": meanings,
                        "pronunciation": (
                            pronunciations[0] if (len(pronunciations) == 1) else None
                        ),
                        "audio": audios[0] if (len(audios) == 1) else None,
                    },
                )
            else:
                error = "No results found for this word."
        else:
            error = "Error fetching data from the dictionary API."
        return render(
            request, "dictionary/results.html", {"error": error, "word": word}
        )

    # If no word is provided, just show the search form
    return render(request, "dictionary/home.html")
