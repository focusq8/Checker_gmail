import requests
import json

file = input("Enter Your File: ")

openFile = open(file ,'r').read().splitlines()
for email in openFile:

    url = 'https://android.clients.google.com/setup/checkavail'
    hed = {
        'Content-Length':'98',
        'Content-Type':'text/plain; charset=UTF-8',
        'Host':'android.clients.google.com',
        'Connection':'Keep-Alive',
        'user-agent':'GoogleLoginService/1.3(m0 JSS15J)'
        }
    data = json.dumps(
        {
            'username':email,
            'version':'3',
            'firstName':'salem',
            'lastName':'Alazmi'
            })
    
    req = requests.post(url,data=data,headers=hed)

    if 'SUCCESS' in req.text:
        print(f'Available: {email}')
        with open('Available.txt' ,'a')as file:
            file.write(f"{email}\n'")

    elif "USERNAME_UNAVAILABLE" in req.text:
        print(f'UnAvailable: {email}')
    else:
        input(req.text)