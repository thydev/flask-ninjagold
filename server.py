from flask import Flask, render_template, request, session, redirect
import random, datetime

app = Flask(__name__)
app.secret_key = "3kdfs3223@#@%@sfAS#@;l"

@app.route('/')
def index():
    if not 'gold' in session:
        session['gold'] = 0
    if not 'activity' in session:
        session['activity'] = ""

    return render_template('index.html')

@app.route('/process_money', methods=['POST'])
def process_money():
    place = request.form['place']
    income = 0
    if place == 'farm':
        income += random.randint(10, 20)
    elif place == 'cave':
        income += random.randint(5, 10)
    elif place == 'house':
        income += random.randint(2, 5)
    else:
        income += random.randint(-50, 50)

    if income >= 0:
        session['activity'] += '<p class="win">Earn {} golds from {}! ({})</p>'.format(income, place, datetime.datetime.now().strftime("%Y/%m/%d %I:%M %p"))
    else:
        session['activity'] += '<p class="lost">Entered a casino and lost {} golds... Ouch. ({})</p>'.format(income, datetime.datetime.now().strftime("%Y/%m/%d %I:%M %p"))
    session['gold'] += income
    return redirect('/')

@app.route('/reset')
def reset():
    session.clear()
    return redirect('/')
    
app.run(debug = True)

