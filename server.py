from flask import Flask, request, render_template, send_file, redirect, url_for

app = Flask(__name__)

temp_flights = [
    {
        'id': 1,
        'name': 'Flight 1',
        'from': 'PNQ',
        'to': 'BOM',
        'time': '12:30 PM',
        'date': '12-12-2020',
        'luggage': [
            {
                'owner': 'Bro 1',
                'weight': '10kg',
                'dimensions': '3m x 3m',
                'container_no': 1
            },
            {
                'owner': 'Bro 2',
                'weight': '5kg',
                'dimensions': '2m x 2m',
                'container_no': 1
            },
            {
                'owner': 'Bro 3',
                'weight': '8kg',
                'dimensions': '2m x 2m',
                'container_no': 3
            },
            {
                'owner': 'Bro 4',
                'weight': '1kg',
                'dimensions': '0.5m x 0.5m',
                'container_no': 4
            },
            {
                'owner': 'Bro 5',
                'weight': '24kg',
                'dimensions': '5m x 5m',
                'container_no': 7
            }
        ]
    },
    {
        'id': 2,
        'name': 'Flight 2',
        'from': 'DXB',
        'to': 'NYC',
        'time': '12:30 PM',
        'date': '12-12-2020',
    },
    {
        'id': 3,
        'name': 'Flight 3',
        'from': 'HYD',
        'to': 'CHN',
        'time': '12:30 PM',
        'date': '12-12-2020',
    },
    {
        'id': 4,
        'name': 'Flight 4',
        'from': 'HYD',
        'to': 'CHN',
        'time': '12:30 PM',
        'date': '12-12-2020',
    },
    {
        'id': 5,
        'name': 'Flight 5',
        'from': 'HYD',
        'to': 'CHN',
        'time': '12:30 PM',
        'date': '12-12-2020',
    },
]




#####################################################
#                 WEBSITE API                       #
#####################################################

@app.route('/luggage_of_<fname>', methods = ['GET'])
def luggage_page(fname):
    if request.method == 'GET':
        # TODO: Get all luggages in the flight
        # retrive data from db for fname
        pass
    luggage_data = temp_flights[int(fname) - 1]['luggage']
    return render_template('luggage_page.html', luggage = luggage_data, fname = fname)

@app.route('/add_luggage_<fname>', methods = ['GET', 'POST'])
def add_luggage(fname):
    if request.method == 'GET':
        return render_template('add_luggage.html')
    else:
        # TODO: Add logic to add data to db
        pass
    return redirect(url_for('luggage_page', fname = fname))
    

@app.route('/flights', methods = ['GET'])
def flights_page():
    return render_template('flights_page.html', flights = temp_flights)

@app.route('/add_flight', methods = ['GET', 'POST'])
def add_flights():
    if request.method == 'GET':
        return render_template('add_flight.html')
    else:
        pass
        # TODO: Add logic to add flights into database
    return redirect(url_for('flights_page'))        

@app.route('/login', methods = ['GET'])
def login_page():
    return render_template("login.html")

@app.route('/login_form', methods = ['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        print('Username: ', username, 'Password: ', password)
        # TODO: Enter logic to check if valid login
        return redirect(url_for('flights_page'))
    else:
        return redirect(url_for('login_page'))

@app.route('/helpdesk', methods = ['GET', 'POST'])
def helpdesk_page():
    if request.method == 'POST':
        # TODO: Add data into csv file
        pass
    return render_template('helpdesk_page.html')

@app.route('/')
def landing_page():
    return redirect(url_for('login'))

#####################################################
#                     FTP API                       #
#####################################################

@app.route('/luggage_icon.png', methods = ['GET'])
def get_luggage_icon():
    return send_file('.\\templates\\luggage_icon.png')

@app.route('/favicon.ico', methods = ['GET'])
def get_favicon():
    return send_file('.\\templates\\luggage_icon.ico')

if __name__ == '__main__':
    app.run()