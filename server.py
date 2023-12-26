import os, signal, socket
from flask import Flask, jsonify, render_template, url_for, request
from paths import *


os.chdir(ROOT_DIR)

class NETWORK():
    hostname = socket.gethostname()
    local_ip = socket.gethostbyname_ex(hostname)[-1][-1]
    localhost = 'localhost'
    
    def __init__(self, IP=None, PORT=None, upload_directory_path=UPLOAD_TO_DIR, network_name='Nothing.', DEBUG = False) -> None:
        # print(socket.gethostbyname_ex(NETWORK.hostname))
        self.app = Flask(__name__, template_folder=PAGE_DIR, static_folder=PAGE_DIR)
        if DEBUG: self.app.config['ENV'] = 'production'
        self.app.config['DEBUG'] = DEBUG
        self.request = request

        self.network_name = network_name
        self.other_info = {}

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
        self.upload_directory_path = upload_directory_path
        self.setup_routes()  # Hívjuk meg a setup_routes metódust a konstruktorban

    def run(self):
        self.app.run(host=self.IP, port=self.PORT)
    
    def shutdown_server(self):
        os.kill(os.getpid(), signal.SIGINT)
        return jsonify({ "success": True, "message": "Server is shutting down..." })


    def setup_routes(self):
        # A metóduson belül értelmezzük a route-okat
        @self.app.route("/")
        def index():
            #full_filename = os.path.join(app.config['UPLOAD_FOLDER'], 'shovon.jpg')
            return render_template("index.html")

        @self.app.route('/upload', methods=['POST'])
        def handle_upload():
            # Ellenőrizze, hogy a kérésben van-e fájl
            if self.request.files.get('file'):
                # Olvassa be a fájlt
                file = self.request.files['file']
                # Mentse a fájlt
                print()
                save_path = os.path.join(self.upload_directory_path, file.filename)
                file.save(save_path)
                return 'A fájl sikeresen feltöltésre került.'
            else:
                return 'Nincs fájl a kérésben.'

        @self.app.route('/chat', methods=['POST'])
        def handle_chat():
            # Ellenőrizze, hogy a kérésben van-e szöveg
            if self.request.headers['Content-Type'] == 'text/plain':
                # A kérésben szöveg van
                data = request.get_data(as_text=True)

                if data.split(' ')[0] == 'SYSTEM-SET': # (SYSTEM-SET KEY VALUE)
                    command = data.split(' ')
                    self.other_info[command[1]] = command[2]
                    print(self.other_info)

                print(f"Kapott üzenet: {data}")
                return 'A kérésben {0} van.'.format(data)
            else:
                return 'A kérésben nem volt szöveg.'
        
        @self.app.route('/shutdown')
        def shutdown():
            self.shutdown_server()
            return 'Server shutting down...'

if __name__ == "__main__":
    NETWORK(PORT=8082, IP='0.0.0.0').run()
