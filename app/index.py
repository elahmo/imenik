from flask import Flask, Response, request, render_template
from .constants import AREA_CODE_MAPPINGS


app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # get the phone number
        number = ''.join(i for i in request.form['number'] if i.isdigit())

        area_code = number[:3]
        phone_number = number[3:]

        # get potential providers for the area code, iterate until result is found
        providers = AREA_CODE_MAPPINGS[area_code]
        for provider in providers:
            result = provider(area_code, phone_number)
            if result['success']:
                return Response(result['message'])

        return Response(f'Nema rezultata ({",".join([p.__name__ for p in providers])})')
    return render_template('index.html')

if __name__ == '__main__':
   app.run()