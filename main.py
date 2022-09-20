import requests
url = 'https://rasachatbotnew.herokuapp.com/webhooks/rest/webhook'
myobj = {
"message":"services",
"sender":"ABC"
}
x = requests.post(url, json = myobj)
print(x.text)
