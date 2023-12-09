import requests
import os

diary = os.path.dirname(__file__)
PORT = 8080


def upload_file(file_path):
    # Készítsen HTTP POST kérést a szerverhez
    request = requests.post(f'http://localhost:{PORT}/upload', files={'file': open(file_path, 'rb')})

    # Ellenőrizze a válasz kódját
    if request.status_code == 200:
        # A fájl sikeresen feltöltésre került
        return True
    else:
        # A fájl feltöltése sikertelen
        return False

if __name__ == '__main__':
    # Adja meg a fájl elérési útját
    file = input('Enter the path of the file to upload: ')
    file_path = os.path.join(file)

    # Töltse fel a fájlt
    success = upload_file(file_path)

    # Írja ki a sikert vagy a hibát
    if success:
        print('A fájl sikeresen feltöltésre került.')
    else:
        print('A fájl feltöltése sikertelen.')
