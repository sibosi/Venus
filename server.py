from bottle import Bottle, route, request
import os

app = Bottle()

IP = 'localhost' # 192.168.101.
PORT = 8080
actual_diary = os.path.dirname(__file__)
upload_diary = os.path.join(actual_diary, 'upload/')


@app.route('/upload', method='POST')
def handle_upload():
    # Ellenőrizze, hogy a kérésben van-e fájl
    if request.files.get('file'):
        # Olvassa be a fájlt
        file = request.files['file']
        # Mentse a fájlt
        file.save(upload_diary + file.filename)
        return 'A fájl sikeresen feltöltésre került.'
    else:
        return 'Nincs fájl a kérésben.'

app.run(host=IP, port=PORT)
