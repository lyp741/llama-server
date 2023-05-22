import requests

url = 'http://8.217.115.123:8000/model?question='

question = '''Answer the question using the alphabet. "3 - 4- -4 - 5 - 7 - 4- -8 - 5---2"  How many THREE is/ are there?
A. THREE OR ABOVE
B. ONE
C. NONE'''

req = url + question

res = requests.get(req)
print(res.content)