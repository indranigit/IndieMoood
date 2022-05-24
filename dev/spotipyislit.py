import spotipy
from spotipy import util
import random
from spotipy.oauth2 import SpotifyClientCredentials

moods_to_music = {'anger': ['Get Turnt', 'Rock Hard'],
                'contempt': ['Down in the Dumps', 'Most Necessary'],
                'disgust': ['Move On & Don\'t Look Back'],
                'fear': ['Tender', 'Techno Bunker'],
                'happiness': ['Have a Great Day!', 'Happy Hits!'],
                'neutral': ['Your Favorite Coffeehouse', 'chill.out.brain'],
                'sadness': ['Melancholia', 'Life Sucks'],
                'surprise': ['Songs to Sing in the Shower', 'Energizing Hits']}

def authenticate():
    username = "travrb16"
    token = util.prompt_for_user_token(username, 
        client_id='1ba453bd75d044359b41ff526bc9ba48',
        client_secret='8fb7cca3f3424cc3ac17911b810397cd',
        redirect_uri="http://localhost:5000/callback")

    client_credentials_manager = SpotifyClientCredentials(client_id='1ba453bd75d044359b41ff526bc9ba48', client_secret='8fb7cca3f3424cc3ac17911b810397cd')
    sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager, auth=token)    

def playMood(primaryMood):
    playlist = random.choice(moods_to_music[primaryMood])
    search = sp.search(moodsic, type='playlist')['playlists']['items']
    for term in search:
        if term['name'] == moodsic:
            moodsic_uri = term['uri']
            break

    sp.start_playback(device_id="travrb16", context_uri=moodsic_uri, uris=None, offset=None)