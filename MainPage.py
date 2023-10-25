from flask import Flask, render_template, request, redirect,jsonify

app = Flask(__name__)

@app.route('/')
def index():
        return render_template('MainPage.html')

@app.route('/TakeAway.html')
def TakeAway():
        return render_template('TakeAway.html')

@app.route('/InHouse.html')
def InHouse():
        return render_template('InHouse.html')

if __name__ == '__main__':
    app.run(debug= True)

