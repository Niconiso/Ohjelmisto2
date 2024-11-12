from flask import Flask, jsonify
import sqlite3

app = Flask(__name__)
def hae_lentokentan_tiedot(icao):
    conn = sqlite3.connect('maailmanympari')
    cursor = conn.cursor()
    cursor.execute("SELECT name, municipality FROM airports WHERE ident = ?", (icao,))
    result = cursor.fetchone()
    conn.close()

    if result:
        return {
            "ICAO": icao,
            "Name": result[0],
            "Municipality": result[1]
        }
    else:
        return None


@app.route('/kenttä/<icao>', methods=['GET'])
def hae_kentta(icao):
    lentokentan_tiedot = hae_lentokentan_tiedot(icao)
    if lentokentan_tiedot:
        return jsonify(lentokentan_tiedot)


if __name__ == '__main__':
    app.run(debug=True, port=3000)
