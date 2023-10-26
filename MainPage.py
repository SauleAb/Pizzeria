from flask import Flask, render_template, request, redirect,jsonify
import tkinter 
from tkinter import messagebox
import random


app = Flask(__name__)


pizzas = ["Margherita", "Pepperoni", "Hawaiian", "BBQ Chicken", "Meat Lovers", "Veggie", "Four Cheese (Quattro Formaggi)", "White Pizza", "Buffalo Chicken", "Supreme", "Sicilian", "Neapolitan", "Spinach and Feta", "Pesto", "Barbecue Bacon"]
sizes = ["Small (6 slices)", "Medium (8 slices)", "Large (12 pieces)", "Jumbo (16 pieces)"]


@app.route('/')
def index():
    return render_template('MainPage.html')

@app.route('/TakeAway.html')
def TakeAway():
    # global pizzas
    return render_template('TakeAway.html', pizzas = pizzas, sizes = sizes)

@app.route('/InHouse.html')
def InHouse():
    return render_template('InHouse.html')

@app.route('/TakeAway.html', methods = ['POST'])
def WaitRoom():
    PizzaType = request.form['SelectedPizza']
    Size = request.form['PizzaSize']
    AdditionalComments = request.form['AdditionalComments']
    OrderNumber = random.randint(20,10000)
    return render_template('OrderWaitRoom.html', PizzaType = PizzaType, Size = Size, AdditionalComments = AdditionalComments, OrderNumber = OrderNumber)


if __name__ == '__main__':
    app.run(debug= True)

