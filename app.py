# Wir importieren die benötigten Funktionen aus dem Flask-Framework:
# Flask = Die Hauptklasse, um eine Webanwendung zu erstellen
# jsonify = Um Python-Daten (z. B. Dictionary) als JSON an den Browser zu schicken
# render_template = Um HTML-Dateien aus einem Template-Ordner zu laden
from flask import Flask, jsonify, render_template

# Wir erstellen ein neues Flask-Objekt namens "app".
# __name__ sorgt dafür, dass Flask weiß, in welcher Datei es gerade läuft.
app = Flask(__name__)

# Mit @app.route("/") definieren wir eine sogenannte "Route".
# Diese sagt: Wenn jemand die Startseite ("/") im Browser aufruft, dann…
@app.route("/")
def startseite():
    # …soll die HTML-Datei "startseite.html" angezeigt werden.
    # Diese Datei muss im Ordner "templates/" liegen.
    return render_template("startseite.html")

# Eine weitere Route: Wenn jemand "/nachricht" im Browser aufruft, dann…
@app.route("/nachricht")
def nachricht_abrufen():
    # …erstellen wir ein Dictionary mit einer kleinen Nachricht.
    nachricht = {
        "motd": "Willkommen auf der Seite! ☀️"  # motd = message of the day
    }
    # Wir geben die Nachricht als JSON-Objekt zurück.
    return jsonify(nachricht)

# Diese Zeile stellt sicher, dass die App nur gestartet wird,
# wenn wir diese Datei direkt ausführen (nicht beim Import in eine andere Datei).
if __name__ == "__main__":
    # Wir starten den eingebauten Webserver von Flask.
    # debug=True zeigt uns hilfreiche Fehlermeldungen während der Entwicklung.
    app.run(debug=True)
