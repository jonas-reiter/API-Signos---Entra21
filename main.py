from flask import Flask, jsonify, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/<data>')
def signos(data):
    datas = [118, 220, 321, 421, 521, 621, 723, 823, 923, 1023, 1122, 1222, 1231]
    signos = ['Capricornio', 'Aquario', 'Peixes', 'Aries', 'Touro',
              'Gemeos', 'Cancer', 'Leao', 'Virgem',
              'Libra', 'Escorpiao', 'Sagitario', 'Capricornio']
    num = int(data[3:5] + data[:2])
    for i in datas:
        if num < i:
            opcao = signos[datas.index(i)]
            break
    return jsonify({'signo':opcao})


app.run(host='0.0.0.0')
