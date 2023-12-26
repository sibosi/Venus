# Venus
Egy szerver - kliens gyakorlóprojekt egy Raspberry Pi-hez.

A szerver üzenetek és fájlok fogadására alkalmas.

## Telepítés
1. Futtassa az alábbi parancsot:
```
git clone https://github.com/Sibosi/Venus.git
```

2. Futtassa a `setup.py`-t. Ez létrehozza a szükséges mappákat, fájlokat.

3. A későbbi frissítések letöltéséhez futtassa az `update.py`-t.


## Használat
- `main.py` - a konfigurált hálózatokat betölti, futtatja

- `settings.json` - konfigurálja a hálózatok beállításait

- `check-in.py` - frissítések után fut le

- `check-out.py` - leállítja a `main.py`-n keresztül futó szervereket


## Fast drop
A fast drop lényege, hogy két eszköz elézetes konfigurálás nélkül fájlokat oszthatnak meg egymással.

A `fast_drop.py` futtatja a szerver és a kliens programját egyaránt.

1. Futtassa a `fast_drop.py`-t a szerver (címzett) oldalán

2. Futtassa a `fast_drop.py`-t a kliens (feladó) oldalán

3. A `fast_drop` mappa tartalma automatikusan átküldésre kerül a szerver oldalon, a profil gyökérkönyvtárában ("~").

## A program eltávolítása
Ajánoltt az egész mappa törlése manuálisan, mivel a `program_remover.py` csak a mappa tartalmát törli.
