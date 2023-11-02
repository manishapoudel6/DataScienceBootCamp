import requests

url ='http://127.0.0.1:5000/add'
myobj = {'a':2, 'b':4}

x = requests.post(url, json=myobj)

print(x.text)



url ='http://127.0.0.1:5000/sub'
myobj = {'a':2, 'b':4}

y = requests.post(url, json=myobj)

print(y.text)



url ='http://127.0.0.1:5000/div'
myobj = {'a':4, 'b':2}

m = requests.post(url, json=myobj)

print(m.text)



url ='http://127.0.0.1:5000/mul'
myobj = {'a':4, 'b':2}

n = requests.post(url, json=myobj)

print(n.text)