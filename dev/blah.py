import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import json


"""
for input:
'["foo",
    {"bar":
        ["baz", null, 1.0, 2]
    }
]'
"""


def parse(json_string):
    """
    Parse the json string into a list of a dictionary.
    """
    return json.loads(json_string)

print(parse('[{"faceRectangle": {"height": 53, "left": 161, "top": 118, "width": 53},'
            '"scores": {"anger": 0.0021335755, "contempt": 0.0148000093,  "disgust": 0.000458147872, '
            '"fear": 8.82706954e-05, "happiness": 0.0007227033, "neutral": 0.9745141, '
            '"sadness": 0.00594675448, ''"surprise": 0.00133642368}}]'))
# output: [{u'faceRectangle': {u'width': 53, u'top': 118, u'left': 161, u'height': 53}, u'scores': {u'sadness': 0.00594675448, u'neutral': 0.9745141, u'contempt': 0.0148000093, u'disgust': 0.000458147872, u'anger': 0.0021335755, u'surprise': 0.00133642368, u'fear': 8.82706954e-05, u'happiness': 0.0007227033}}]

print(parse('[]'))
# output: []


def return_mood_list(json_list_dict):

    """
    Return only the mood dictionary from the whole dictionary.
    """
    mood_list = []
    if json_list_dict == []: # invalid image
        return ";("
    for idx in xrange(len(json_list_dict)):
        mood_dict = json_list_dict[idx][1]
        mood_list.append(mood_dict)



# def mood_dict(json_dict):


# json_string = '{"first_name": "Guido", "last_name":"Rossum"}'
# parsed_json = json.loads(json_string)
# print(parsed_json['first_name']) # "Guido"
#
#
# client_credentials_manager = SpotifyClientCredentials(client_id='1ba453bd75d044359b41ff526bc9ba48', client_secret='8fb7cca3f3424cc3ac17911b810397cd')
# sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)
#
# playlists = sp.user_playlists('1211323534')
#
# while playlists:
#     for i, playlist in enumerate(playlists['items']):
#         print("%4d %s %s" % (i + 1 + playlists['offset'], playlist['uri'],  playlist['name']))
#     if playlists['next']:
#         playlists = sp.next(playlists)
#     else:
#         playlists = None