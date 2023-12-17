import os
import socket
# import bottle
from flask import Flask, render_template, url_for, request



actual_directory = os.path.dirname(__file__)
page_directory = os.path.join(actual_directory, 'page/')
os.chdir(actual_directory)

class NETWORK():
    hostname = socket.gethostname()
    local_ip = socket.gethostbyname_ex(hostname)[-1][-1]
    localhost = 'localhost'
    
    def __init__(self, IP=None, PORT=None, upload_directory_name='upload/', network_name='Nothing.') -> None:
        # self.bottle = bottle
        # self.app = self.bottle.Bottle()
        self.app = Flask(__name__, template_folder=page_directory, static_folder=page_directory)
        self.app.config['ENV'] = 'production'
        self.app.config['DEBUG'] = False

        if IP == None:
            IP = input('Enter the type of the IP ["localhost" or "local"]: ')
            if IP == "localhost":
                IP = NETWORK.localhost
            elif IP == "local":
                IP = NETWORK.local_ip
        if PORT == None:
            PORT = int(input('Enter the PORT: '))
        
        self.IP = IP
        self.PORT = PORT
        self.upload_directory_name = upload_directory_name
        self.upload_directory = os.path.join(actual_directory, self.upload_directory_name)
        self.setup_routes()  # Hívjuk meg a setup_routes metódust a konstruktorban

    def run(self):
        self.app.run(host=self.IP, port=self.PORT)

    def setup_routes(self):
        # A metóduson belül értelmezzük a route-okat
        @self.app.route("/")
        def index():
            #full_filename = os.path.join(app.config['UPLOAD_FOLDER'], 'shovon.jpg')
            return render_template("index.html")

        @self.app.route('/upload', methods=['POST'])
        def handle_upload():
            # Ellenőrizze, hogy a kérésben van-e fájl
            if request.files.get('file'):
                # Olvassa be a fájlt
                file = request.files['file']
                # Mentse a fájlt
                print()
                upload_directory = os.path.join(actual_directory, self.upload_directory_name)
                save_path = os.path.join(upload_directory, file.filename)
                print(save_path)
                file.save(save_path)
                return 'A fájl sikeresen feltöltésre került.'
            else:
                return 'Nincs fájl a kérésben.'

        @self.app.route('/chat', methods=['POST'])
        def handle_chat():
            # Ellenőrizze, hogy a kérésben van-e szöveg
            if request.headers['Content-Type'] == 'text/plain':
                # A kérésben szöveg van
                data = request.get_data(as_text=True)
                print(f"Kapott üzenet: {data}")
                return 'A kérésben {0} van.'.format(data)
            else:
                return 'A kérésben nem volt szöveg.'

if __name__ == "__main__":
    NETWORK('localhost', 8082).run()
