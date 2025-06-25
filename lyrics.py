import requests
from bs4 import BeautifulSoup


def fetch_lyrics(artist, song):
    artist = artist.replace(" ", "").lower()
    song = song.replace(" ", "").lower()

    url = f"https://www.azlyrics.com/lyrics/{artist}/{song}.html"

    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, "html.parser")
        div = soup.find("div", class_="ringtone")
        lyrics = div.find_next_sibling("div").text.strip()

        return lyrics

    except requests.exceptions.RequestException as e:
        print(f"Failed to fetch lyrics: {e}")
        return None


artist = input("Enter the artist name: ")
song = input("Enter the song name: ")

lyrics = fetch_lyrics(artist, song)
if lyrics:
    print("\nLyrics")
    print(lyrics)
