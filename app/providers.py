import requests
from bs4 import BeautifulSoup

def bhtelecom(area, number):
    # bht is unsupported at the moment as the lookup requires captcha
    return {
        'success': False,
        'message': 'BHT Imenik je trenutno nedostupan.',
    }

    # get the session cookies
    s = requests.Session()
    s.get('https://www.bhtelecom.ba/index.php?id=7345&')

    # post the request
    payload = {
        'di': area,
        'br': f'{area}{number}',
        '_uqid': '',
        '_cdt': '',
        '_hsh': '',
        'btnSearch': 'Traži'
    }
    res = s.post('https://www.bhtelecom.ba/pretraga-po-broju.html?a=search', data=payload)

    # parse the response
    bs = BeautifulSoup(res.text)

    success = False
    # handle the case without results
    if 'Nema rezultata' in bs.text:
        message = 'Nema rezultata'
    else:
        success = True
        # get the data about the recipient
        name = bs.table.findAll('td')[1].text.strip()
        prikljucak = bs.table.findAll('td')[5].text.strip()
        adresa = bs.table.findAll('td')[7].text.strip()
        mjesto = bs.table.findAll('td')[9].text.strip()
        message=  "\n".join([name, prikljucak, adresa, mjesto])

    return {
        'success': success,
        'message': message,
    }


def eronet(area, number):
    # post the request
    payload = {
        'pozivni_broj2': area,
        'telefon': number,
    }
    res = requests.post('https://www.hteronet.ba/telefonski-imenik?action=check&type=broj', data=payload)

    # parse the response
    bs = BeautifulSoup(res.text)
    success = False
    results = bs.findAll('div', 'results-imenik')
    if len(results) == 1:
        message = results[0].text
    else:
        success = True
        rezultat = bs.find('div', id='imenik_results')
        rezultati = rezultat.findAll('td')
        message = f"{rezultati[3].text}\n{rezultati[4].text}"

    return {
        'success': success,
        'message': message,
    }


def mtel(area, number):
    return {
        'success': False,
        'message': 'mTel nije podrzan',
    }

