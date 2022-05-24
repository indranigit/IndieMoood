import httplib, urllib, base64, json

headers = {
    # Request headers. Replace the placeholder key below with your subscription key.
    'Content-Type': 'application/json',
    'Ocp-Apim-Subscription-Key': '0fb41fe10d3141f68910857a7a54304b',
}

params = urllib.urlencode({
})

# Replace the example URL below with the URL of the image you want to analyze.
body = "{\'url\' : \'https://bloximages.chicago2.vip.townnews.com/thefacts.com/content/tncms/assets/v3/editorial/a/bd/abd8cd9a-7b74-504d-ad29-055ad9599521/553c408f1c69a.image.jpg?resize=500%2C751\'}"

try:
    # NOTE: You must use the same region in your REST call as you used to obtain your subscription keys.
    #   For example, if you obtained your subscription keys from westcentralus, replace "westus" in the
    #   URL below with "westcentralus".
    conn = httplib.HTTPSConnection('api.projectoxford.ai')
    conn.request("POST", "/emotion/v1.0/recognize?%s" % params, body, headers)
    response = conn.getresponse()
    data = response.read()
    # 'data' contains the JSON data. The following formats the JSON data for display.
    parsed = json.loads(data)
    print ("Response:")
    print (json.dumps(parsed, sort_keys=True, indent=2))
    conn.close()
except Exception as e:
    print("[Errno {0}] {1}".format(e.errno, e.strerror))



# import httplib, urllib, base64
#
# # Image to analyse (body of the request)
#
# body = '{\'URL\': \'http://www.peterdulworth.com/imgs/logos/luayn.jpg\'}'
#
# # API request for Emotion Detection
#
# headers = {
#     'Content-type': 'application/json',
# }
#
# params = urllib.urlencode({
#     'subscription-key': '0fb41fe10d3141f68910857a7a54304b',  # Enter EMOTION API key
#     # 'faceRectangles': '',
# })
#
# try:
#     conn = httplib.HTTPSConnection('api.projectoxford.ai')
#     conn.request("POST", "/emotion/v1.0/recognize?%s" % params, body, headers)
#     response = conn.getresponse()
#     print("Send request")
#
#     data = response.read()
#     print(data)
#     conn.close()
# except Exception as e:
#     print("[Errno {0}] {1}".format(e.errno, e.strerror))