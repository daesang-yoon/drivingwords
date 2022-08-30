import json
import urllib.request

def get_inspirational_quote() -> str:
    response = None
    try:
        request = urllib.request.Request('https://zenquotes.io/api/random')
        response = urllib.request.urlopen(request)
        json_text = response.read().decode(encoding = 'utf-8')
        return json.loads(json_text)[0]['q']
    finally:
        if response!=None:
            response.close()

def get_stoic_quote() -> str:
    response = None
    try:
        request = urllib.request.Request('https://stoicquotesapi.com/v1/api/quotes/random')
        response = urllib.request.urlopen(request)
        json_text = response.read().decode(encoding = 'utf-8')
        return json.loads(json_text)['body']
    finally:
        if response!=None:
            response.close()

#print(get_inspirational_quote())
#print(get_stoic_quote())