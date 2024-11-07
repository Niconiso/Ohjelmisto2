from flask import Flask, jsonify

app = Flask(__name__)
def alkuluku(n):
    if n <= 1:
        return False
    elif n % 2 == 0 or n % 3 == 0:
        return False
    else:
        return True
@app.route('/alkuluku/<int:numero>', methods=['GET'])
def Alkulukucheck(numero):
    result = {"Numero": numero, "On alkuluku": alkuluku(numero)}
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True, port=3000)