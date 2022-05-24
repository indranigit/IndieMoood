from flask import Flask, render_template, request, redirect, Response, send_from_directory, jsonify, json
import spotipy
from spotipy import oauth2
import random

app = Flask(__name__)

authorized = True

moods_to_music = {'anger': ['Get Turnt', 'Rock Hard'],
                'contempt': ['Down in the Dumps', 'Most Necessary'],
                'disgust': ['Move On & Don\'t Look Back'],
                'fear': ['Tender', 'Techno Bunker'],
                'happiness': ['Have a Great Day!', 'Happy Hits!'],
                'neutral': ['Your Favorite Coffeehouse', 'chill.out.brain'],
                'sadness': ['Melancholia', 'Life Sucks'],
                'surprise': ['Songs to Sing in the Shower', 'Energizing Hits']}

SPOTIPY_CLIENT_ID = '1ba453bd75d044359b41ff526bc9ba48'
SPOTIPY_CLIENT_SECRET = '8fb7cca3f3424cc3ac17911b810397cd'
SPOTIPY_REDIRECT_URI = 'http://localhost:5000'
SCOPE = 'user-read-recently-played'
CACHE = '.spotipyoauthcache'

sp_oauth = oauth2.SpotifyOAuth(SPOTIPY_CLIENT_ID, SPOTIPY_CLIENT_SECRET, SPOTIPY_REDIRECT_URI, scope=SCOPE, cache_path=CACHE)

@app.route('/')
def index():
    print('GET INDEX')
    return render_template('./index.html')

# given primary mood returns playlist
@app.route('/getPlaylist', methods = ['POST'])
def getPlaylist():
    print('GET PLAYLIST')
    if (not authorized):
        authorize()

    primaryEmotion = list(request.form.to_dict().keys())[0] 
    jsonObj = playMood(primaryEmotion)
    print(jsonObj)
    return jsonify(jsonObj)

def authorize():
    access_token = ""
    token_info = sp_oauth.get_cached_token()

    if token_info:
        print("Found cached token!")
        access_token = token_info['access_token']
    else:
        url = request.url
        code = sp_oauth.parse_response_code(url)
        if code:
            print("Found Spotify auth code in Request URL! Trying to get valid access token...")
            token_info = sp_oauth.get_access_token(code)
            access_token = token_info['access_token']

    if access_token:
        print("Access token available! Trying to get user information...")
        global sp
        sp = spotipy.Spotify(access_token)
        primaryEmotion = list(request.form.to_dict().keys())[0] 
        return
    else:
        return htmlForLoginButton()

def htmlForLoginButton():
    auth_url = getSPOauthURI()
    htmlLoginButton = "<a href='" + auth_url + "'>Login to Spotify</a>"
    return htmlLoginButton

def getSPOauthURI():
    auth_url = sp_oauth.get_authorize_url()
    return auth_url

def playMood(primaryMood):
    playlist = random.choice(moods_to_music[primaryMood])
    search = sp.search(playlist, type='playlist')['playlists']['items']
    for term in search:
        if term['name'] == playlist:
            moodsic_url = term['external_urls']
            print(moodsic_url)
            break

    return term

if __name__ == '__main__':
    app.run()
