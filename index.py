import requests
from bs4 import BeautifulSoup

from flask import Flask, Response, request, render_template

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # get the phone number
        number = ''.join(i for i in request.form['number'] if i.isdigit())

        # get the session cookies
        s = requests.Session()
        s.get('https://www.bhtelecom.ba/index.php?id=7345&')


        # post the request
        payload = {
            'di': number[:3],
            'br': number[3:],
            '_uqid': '',
            '_cdt': '',
            '_hsh': '',
            'btnSearch': 'Traži'
        }
        res = s.post('https://www.bhtelecom.ba/pretraga-po-broju.html?a=search', data=payload)

        # parse the response
        bs = BeautifulSoup(res.text)

        # handle the case without results
        if 'Nema rezultata' in bs.text:
            return Response('Nema rezultata')

        # get the data about the recipient
        name = bs.table.findAll('td')[1].text.strip()
        prikljucak = bs.table.findAll('td')[5].text.strip()
        adresa = bs.table.findAll('td')[7].text.strip()
        mjesto = bs.table.findAll('td')[9].text.strip()

        result = "\n".join([name, prikljucak, adresa, mjesto])

        return Response(result)
    return render_template('index.html')

    return Response("Make a POST request with number=000123456 as payload")
