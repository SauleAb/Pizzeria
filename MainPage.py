from flask import Flask, render_template, request, redirect,jsonify
import tkinter 
from tkinter import messagebox
import random
import time
from datetime import datetime

app = Flask(__name__)


pizzas = ["Margherita", "Pepperoni", "Hawaiian", "BBQ Chicken", "Meat Lovers", "Veggie", "Four Cheese (Quattro Formaggi)", "White Pizza", "Buffalo Chicken", "Supreme", "Sicilian", "Neapolitan", "Spinach and Feta", "Pesto", "Barbecue Bacon"]
sizes = ["Small (6 slices)", "Medium (8 slices)", "Large (12 pieces)", "Jumbo (16 pieces)"]
Staff = [{'username': 'mario@gmail.com', 'password': '123456789', 'person':'Mario'},{'username': 'luigi@gmail.com', 'password': '987654321', 'person':'Luigi'}]
orders = []

@app.route('/')
def index():
    return render_template('MainPage.html')

@app.route('/TakeAway.html')
def TakeAway():
    return render_template('TakeAway.html', pizzas = pizzas, sizes = sizes)

@app.route('/InHouse.html')
def InHouse():
    return render_template('InHouse.html', pizzas = pizzas, sizes = sizes)

@app.route('/LogIn.html')
def LogIn():
    return render_template('LogIn.html')

@app.route('/StaffPage.html')
def StaffPage():
    return render_template('StaffPage.html')


@app.route('/TakeAway.html', methods = ['POST'])
def WaitRoom():
    PizzaType = request.form['SelectedPizza']
    Size = request.form['PizzaSize']
    AdditionalComments = request.form['AdditionalComments']
    OrderNumber = random.randint(20,10000)
    timestamp = time.time()
    orders.append({'PizzaType': PizzaType, 'Size': Size, 'AdditionalComments': AdditionalComments, 'OrderNumber': OrderNumber, 'timestamp': timestamp})
    return render_template('OrderWaitRoom.html', PizzaType = PizzaType, Size = Size, AdditionalComments = AdditionalComments, OrderNumber = OrderNumber)

@app.route('/InHouse.html', methods = ['POST'])
def WaitRoomInHouse():
    error = None
    PizzaType = request.form['SelectedPizza']
    Size = request.form['PizzaSize']
    AdditionalComments = request.form['AdditionalComments']
    TableNumber = request.form['TableNumber']

    try:
        TableNumber = int(TableNumber)
        if 1 <= TableNumber <= 20:
            timestamp = time.time()
            orders.append({'PizzaType': PizzaType, 'Size': Size, 'AdditionalComments': AdditionalComments, 'TableNumber': TableNumber, 'timestamp': timestamp})
            return render_template('OrderWaitRoomInHouse.html', PizzaType=PizzaType, Size=Size, AdditionalComments=AdditionalComments, TableNumber=TableNumber)
        else:
            error = "Table number must be between 10 and 20."
    except ValueError:
        error = "Table number must be a valid number."

    return render_template('InHouse.html', pizzas=pizzas, sizes=sizes, error=error)


@app.route('/LogIn.html', methods = ['POST'])
def ToStaffPage():
    error = None
    Username = request.form['username']
    Password = request.form['password']
    authenticated = False
    
    for i in Staff:
        for i in Staff:
            if Username == i.get('username') and Password == i.get('password'):
                authenticated = True
                Person = i.get('person')
                break

    if not authenticated:
        error = "Incorrect data"

    if authenticated:
        return render_template('StaffPage.html', Person = Person)
    else:
        return render_template('LogIn.html', error=error)
 

if __name__ == '__main__':
    app.run(debug= True)



# add a price to each pizza and size (with a dictionary)


