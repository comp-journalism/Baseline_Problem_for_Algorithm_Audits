'''
Based on exmaple code provided my microsoft

'''

import http.client, urllib.request, urllib.parse, urllib.error
import glob, time, json, sys

headers = {
    # Request headers
    'Content-Type': 'application/octet-stream', # for using local files
    'Ocp-Apim-Subscription-Key': '   ',  # put your own Key here
}

params = urllib.parse.urlencode({
    # Request parameters
    'subscription-key': " ",
    'returnFaceId': 'true',
    'returnFaceLandmarks': 'false',
    'returnFaceAttributes': 'age,smile,emotion,gender',
})

def make_json(candidate):
    body = ""

    #candidate = 'donald_trump'
    #image_filename = file_dir + '0_' + candidate + '.jpg'

    file_dir = './' + candidate + "_image_universe/"
    output_dir = 'MicrosoftAPI_jsons/'

    #load image
    for image_filename in glob.glob(file_dir + '*.jpg'):
        print(image_filename)

        with open(image_filename, 'rb') as f:
            print(f)
            body = f.read()

        try:
            conn = http.client.HTTPSConnection('westus.api.cognitive.microsoft.com')
            conn.request("POST", "/face/v1.0/detect?%s" % params, body, headers)
            response = conn.getresponse()
            data = response.read()
            data = data.decode('utf-8')
            print(data)
            conn.close()
        except Exception as e:
            print(e.args)

        output_file = image_filename.split('/')[2]
        output_file = output_file.split('.')[0]
        print(output_file)
        with open(output_dir + output_file + '.json', 'w', encoding='utf-8') as fp:
            json.dump(data, fp)

        time.sleep(2)

make_json('hillary_clinton' )
