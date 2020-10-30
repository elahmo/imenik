from flask import Flask, Response, request, render_template

from constants import AREA_CODE_MAPPINGS, BHT, ERONET, MTEL
import providers


app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # get the phone number
        number = ''.join(i for i in request.form['number'] if i.isdigit())

        area_code = number[:3]
        phone_number = number[3:]

        # get potential providers for the area code, iterate until result is found
        providers_for_area_code = AREA_CODE_MAPPINGS[area_code]
        for provider in providers_for_area_code:
            result = getattr(providers, provider)(area_code, number)
            if result['success']:
                return Response(result['message'])

        return Response(f'Nema rezultata ({",".join([p for p in providers_for_area_code])})')
    return render_template('index.html')

if __name__ == '__main__':
   app.run()