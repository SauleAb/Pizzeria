from flask import Flask, render_template, request, session, redirect,jsonify
import tkinter 
from tkinter import messagebox
import random
import time
import datetime
import math
import copy

app = Flask(__name__)


pizzas = ["Margherita", "Pepperoni", "Hawaiian", "BBQ Chicken", "Meat Lovers", "Four Cheese (Quattro Formaggi)", "White Pizza","Sicilian", "Neapolitan", "Pesto", "Barbecue Bacon"]
sizes = ["Small (6 slices)", "Medium (8 slices)", "Large (12 pieces)", "Jumbo (16 pieces)"]
Staff = [{'username': 'mario@gmail.com', 'password': '123456789', 'person':'Mario'},{'username': 'luigi@gmail.com', 'password': '987654321', 'person':'Luigi'}]
orders = []
basket = []
# basket.clear()


pizza_details = {
    "Margherita": {
        "Size": {
            "Small (6 slices)": "$5.00",
            "Medium (8 slices)": "$7.00",
            "Large (12 pieces)": "$10.50",
            "Jumbo (16 pieces)": "$15.00",
        },
        "Ingredients": "Fresh Tomatoes, Fresh Mozzarella, Fresh Basil",
    },
    "Pepperoni": {
        "Size": {
            "Small (6 slices)": "$6.50",
            "Medium (8 slices)": "$8.50",
            "Large (12 pieces)": "$12.00",
            "Jumbo (16 pieces)": "$16.50",
        },
        "Ingredients": "Pepperoni, Cheese, Tomato Sauce",
    },
    "Hawaiian": {
        "Size": {
            "Small (6 slices)": "$7.50",
            "Medium (8 slices)": "$9.50",
            "Large (12 pieces)": "$13.00",
            "Jumbo (16 pieces)": "$18.00",
        },
        "Ingredients": "Ham, Pineapple, Cheese, Tomato Sauce",
    },
    "BBQ Chicken": {
        "Size": {
            "Small (6 slices)": "$8.00",
            "Medium (8 slices)": "$10.00",
            "Large (12 pieces)": "$14.00",
            "Jumbo (16 pieces)": "$20.00",
        },
        "Ingredients": "BBQ Chicken, Onions, Cheese, BBQ Sauce",
    },
    "Meat Lovers": {
        "Size": {
            "Small (6 slices)": "$9.00",
            "Medium (8 slices)": "$11.00",
            "Large (12 pieces)": "$16.00",
            "Jumbo (16 pieces)": "$22.00",
        },
        "Ingredients": "Pepperoni, Sausage, Bacon, Cheese, Tomato Sauce",
    },
    "Four Cheese (Quattro Formaggi)": {
        "Size": {
            "Small (6 slices)": "$7.50",
            "Medium (8 slices)": "$9.50",
            "Large (12 pieces)": "$13.00",
            "Jumbo (16 pieces)": "$18.00",
        },
        "Ingredients": "Mozzarella, Gorgonzola, Parmesan, Ricotta",
    },
    "White Pizza": {
        "Size": {
            "Small (6 slices)": "$7.50",
            "Medium (8 slices)": "$9.50",
            "Large (12 pieces)": "$13.00",
            "Jumbo (16 pieces)": "$18.00",
        },
        "Ingredients": "Olive Oil, Garlic, Ricotta, Mozzarella, Spinach",
    },
    "Sicilian": {
        "Size": {
            "Small (6 slices)": "$8.50",
            "Medium (8 slices)": "$10.50",
            "Large (12 pieces)": "$15.00",
            "Jumbo (16 pieces)": "$21.00",
        },
        "Ingredients": "Thick Crust, Tomato Sauce, Mozzarella, Parmesan",
    },
    "Neapolitan": {
        "Size": {
            "Small (6 slices)": "$7.00",
            "Medium (8 slices)": "$9.00",
            "Large (12 pieces)": "$12.50",
            "Jumbo (16 pieces)": "$17.50",
        },
        "Ingredients": "Thin Crust, Tomato Sauce, Mozzarella, Basil",
    },
    "Pesto": {
        "Size": {
            "Small (6 slices)": "$8.00",
            "Medium (8 slices)": "$10.00",
            "Large (12 pieces)": "$14.00",
            "Jumbo (16 pieces)": "$20.00",
        },
        "Ingredients": "Pesto Sauce, Mozzarella, Tomatoes, Garlic",
    },
    "Barbecue Bacon": {
        "Size": {
            "Small (6 slices)": "$8.50",
            "Medium (8 slices)": "$10.50",
            "Large (12 pieces)": "$15.00",
            "Jumbo (16 pieces)": "$21.00",
        },
        "Ingredients": "Barbecue Sauce, Bacon, Onion, Mozzarella",
    },
}

@app.route('/')
def index():
    basket.clear()
    return render_template('MainPage.html')

@app.route('/TakeAway.html')
def TakeAway():
    Total = sum(pizza['Price'] for pizza in basket)
    return render_template('TakeAway.html', Total = Total, pizza_details = pizza_details, pizzas = pizzas, sizes = sizes, basket = basket)

# @app.route('/InHouse.html')
# def InHouse():
#     return render_template('InHouse.html', pizzas = pizzas, sizes = sizes)

@app.route('/LogIn.html')
def LogIn():
    current_datetime = datetime.datetime.now()
    time1 = current_datetime.time()
    ftime = time1.strftime("%H:%M:%S")
    return render_template('LogIn.html',ftime = ftime)

@app.route('/StaffPage.html')
def StaffPage():
    Total = sum(pizza['Price'] for pizza in orders)
    # current_datetime = datetime.datetime.now()
    # time1 = current_datetime.time()
    # ftime = time1.strftime("%H:%M:%S")

    # pizza_totals = calculate_pizza_totals(orders)
    # table_totals = calculate_table_totals(orders)
    # start_index = (orders[pizza['TableNumber']:] for pizza in orders)
    # AllMoney = 0
    # for pizza in orders:
    #     for pizza2 in orders:
    #         if pizza['TableNumber'] == pizza2['TableNumber']:




    return render_template('StaffPage.html',basket = basket, orders = orders, Total = Total)

    # return render_template('StaffPage.html',table_totals = table_totals, AllMoney = AllMoney, pizza_totals = pizza_totals, start_index = start_index, orders = orders, basket = basket, Total = Total)

# def calculate_table_totals(orders):
#     table_totals = {}
#     for order in orders:
#         table_number = order['TableNumber']
#         total_price = order['TotalPrice']
#         if table_number in table_totals:
#             table_totals[table_number] += total_price
#         else:
#             table_totals[table_number] = total_price
#     return table_totals

# def calculate_pizza_totals(orders):
#     pizza_totals = {}
#     for order in orders:
#         pizza_name = order['Pizza']
#         total_price = order['Amount'] * order['Price']
#         if pizza_name in pizza_totals:
#             pizza_totals[pizza_name] += total_price
#         else:
#             pizza_totals[pizza_name] = total_price
#     return pizza_totals


@app.route('/AwayVsHouse.html',methods = ['GET', 'POST'])
def Location():
    global basket,orders
    error = None
    Total = 0
    Total = sum(pizza['Price'] for pizza in basket)


    if request.method == "POST":
        action3 = request.form.get('Confirm')
        action4 = request.form.get('ToMenu')
        if action3 == 'ToWaitRoom':
            location = request.form.get('SelectLocation')
            if location:
                if location == 'Restaurant':
                    TableNumber = request.form.get('TableNumber')
                    if TableNumber:
                        tnum = int(TableNumber)
                        if tnum > 20 or tnum < 1:
                            error = "No such table"
                        else:
                            # table_orders = []
                            for pizza in basket:
                                order = {
                                    'TableNumber': tnum,
                                    'Pizza': pizza['Pizza'],
                                    'Size': pizza['Size'],
                                    'Amount': pizza['Amount'],
                                    'Price': pizza['Price'],
                                    # 'TotalPrice': None
                                }
                                if 'Comments' in pizza:
                                    order['Comments'] = pizza['Comments']


                                Total = sum(pizza['Price'] for pizza in basket)
                                order['TotalPrice'] = (f'{Total}')

                                orders.append(order)
                            # table_orders.append(order)
                            # orders.append(table_orders)
                            # print(orders)


                            return render_template('OrderWaitRoom.html', tnum = tnum, basket = basket, Total = Total)
                    else: 
                        error = "Please select a Table Number"

                elif location == 'TakeAway':
                    tnum = random.randint(20,1000)

                    for pizza in basket:
                                order = {
                                    'TableNumber': tnum,
                                    'Pizza': pizza['Pizza'],
                                    'Size': pizza['Size'],
                                    'Amount': pizza['Amount'],
                                    'Price': pizza['Price'],
                                    # 'TotalPrice': None
                                }
                                if 'Comments' in pizza:
                                    order['Comments'] = pizza['Comments']
                        # orders.append(order)

                                Total = sum(pizza['Price'] for pizza in basket)
                                order['TotalPrice'] = (f'{Total}')

                                orders.append(order)
                                print(orders)




                    return render_template('OrderWaitRoom.html', tnum = tnum, basket = basket, Total = Total)
                
            else:
                error = "Please select a location"


        elif action4 == 'BackToMenu':

            Total = sum(pizza['Price'] for pizza in orders)
            order['TotalPrice'] = Total

            return render_template('TakeAway.html', basket = basket, Total = Total)

    return render_template('/AwayVsHouse.html', basket = basket, Total = Total, error = error)

@app.route('/OrderWaitRoom.html')
def WaitRoom():
    return render_template('OrderWaitRoom.html',basket = basket)


@app.route('/Margherita.html/<pizza_name>', methods = ['GET', 'POST'])
def Margherita(pizza_name):
    global basket
    Total = 0
    error = None
    pizza_info = pizza_details.get(pizza_name)

    if request.method == 'POST':
        action = request.form.get('action')
        action2 = request.form.get('ToMenu')

        if action == 'add':
            size = request.form.get('SelectedSize')
            if size:
                amount = request.form['Amount']
                if amount:
                    try:
                        amount = int(amount)
                    except ValueError:
                        error_message = "Please select a valid amount."
                        return render_template('Margherita.html', pizza_details=pizza_details, basket=basket, error=error_message,pizza_name=pizza_name)
                else:
                    amount = 1

                PricePerOne = pizza_details.get(pizza_name, {}).get("Size", {}).get(size, None)
                PricePerOne_float = float(PricePerOne.replace("$",""))
                price = PricePerOne_float * amount

                comments = request.form.get('AdditionalComments', '')
                if comments:
                    selected_pizza = {
                        'Pizza': pizza_name,
                        'Size': size,
                        'Amount': amount,
                        'Comments': comments,
                        'Price': price,
                    }
                    basket.append(selected_pizza)
                    print(basket)

                else:
                    selected_pizza = {
                        'Pizza': pizza_name,
                        'Size': size,
                        'Amount': amount,
                        'Price': price,
                    }
                    basket.append(selected_pizza)
                    print(basket)

            else:
                error = "Please select a size"
            
        elif action2 == 'BackToMenu':
            Total = sum(pizza['Price'] for pizza in basket)
            return render_template('TakeAway.html', basket=basket, Total=Total)
        
    Total = sum(pizza['Price'] for pizza in basket)
    return render_template('Margherita.html',pizza_info = pizza_info, pizza_details=pizza_details, basket=basket, error=error,pizza_name=pizza_name, Total=Total)

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
        # pizza_totals = calculate_pizza_totals(orders)
        # Total = sum(pizza['Price'] for pizza in orders)
        # table_totals = calculate_table_totals(orders)

        # start_index = (orders[pizza['TableNumber']:] for pizza in orders)
        # AllMoney = 0
        print(orders)
        current_datetime = datetime.datetime.now()
        time1 = current_datetime.time()
        ftime = time1.strftime("%H:%M:%S")

        return render_template('StaffPage.html',ftime = ftime, Person = Person, basket = basket, orders = orders)
    else:
        current_datetime = datetime.datetime.now()
        time1 = current_datetime.time()
        ftime = time1.strftime("%H:%M:%S")
        return render_template('LogIn.html',ftime = ftime, error=error)
 

if __name__ == '__main__':
    app.run(debug= True)










# it lets me in to the staff page when no username is entered