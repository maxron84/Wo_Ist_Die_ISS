import requests
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap

# Notlösung für das basemap-import-Problem unter debian 12:
# pip install basemap--break-system-packages

def wo_ist_die_iss():
    antwort = requests.get("http://api.open-notify.org/iss-now.json")
    if antwort.status_code == 200:
        daten = antwort.json()
        iss_position = daten["iss_position"]
        return iss_position
    else:
        return None

def iss_karte():
    iss_position = wo_ist_die_iss()
    if iss_position:
        lon = float(iss_position['longitude'])
        lat = float(iss_position['latitude'])

        karte = Basemap(projection='ortho', lat_0=lat, lon_0=lon)
        karte.drawcoastlines()

        x, y = karte(lon, lat)
        karte.plot(x, y, 'ro', markersize=10)

        plt.title("Aktuelle Position der ISS")
        plt.show()
    else:
        print("Fehler beim Abrufen der ISS-Position!")

if __name__ == "__main__":
    iss_karte()
