from flask import Flask, render_template

app = Flask(__name__)

# Define the available pizzas
pizzas = ["Margherita", "Pepperoni", "Hawaiian", "Vegetarian", "Supreme"]

@app.route('/')
def index():
    return render_template('testermenu.html', pizzas=pizzas)

if __name__ == '__main__':
    app.run(debug=True)
