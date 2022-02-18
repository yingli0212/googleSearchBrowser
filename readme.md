# Introduction 
    - This is a web service to be used by search keyword on google website.

### Summary 
    - As results, the first ten results from google are shown. The search results is saved in a json file as output. You can find this json file in your current local directory.

### Requirements 
    - Python 3.8

### Usage
    - This web service is used by Webbrowser.
    - Authentication uses the „username“, "password" and a „verifycode“.
    - To each user an individual QRcode is generated during registration. This QRcode needs to be saved by user carefully.
    - User uses „Google Authenticator“ (An application in Appstore) to scann his QRcode to get a „Time base One Time Password“, namely verifycode. This verify code is changed all 30 seconds in „Google Authenticator“. This verifycode needs to be read out and given in the next step.
    - In the Webbrowser the following url needs to be given to open the homepage: "http://localhost:5000/"
    - Go to the Sign-In page by using the url: "http://localhost:5000/signin“

### Contact 
    - email to: zhaoyingli1@hotmail.com
