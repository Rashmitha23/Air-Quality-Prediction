from flask import Flask, render_template, request, redirect, url_for
import pandas as pd
from glob import glob
from prediction import AirQualityPrediction

app = Flask(__name__)
app.secret_key = "aitquality"


@app.route('/')
@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        email = request.form["email"]
        pwd = request.form["pwd"]
        r1 = pd.read_excel('user.xlsx')
        for index, row in r1.iterrows():
            if row["email"] == str(email) and row["password"] == str(pwd):
                return redirect(url_for('home'))

        mesg = 'Invalid Login Try Again'
        return render_template('login.html', msg=mesg)
    else:
        return render_template('login.html')


@app.route('/register', methods=['POST', 'GET'])
def register():
    try:
        if request.method == 'POST':
            email = request.form['email']
            pwd = request.form['pwd']
            repwd = request.form['repwd']
            if pwd == repwd:  # Fix the comparison operator
                col_list = ["email", "password"]
                try:
                    # Try reading the existing file, if it exists
                    r1 = pd.read_excel('user.xlsx', usecols=col_list)
                except FileNotFoundError:
                    # If the file doesn't exist, create an empty DataFrame
                    r1 = pd.DataFrame(columns=col_list)

                new_row = {'email': email, 'password': pwd}
                r1 = r1.append(new_row, ignore_index=True)
                r1.to_excel('user.xlsx', index=False)
                print("Records created successfully")
                msg = 'Registration Successful. You can log in here.'
                return render_template('login.html', msg=msg)
            else:
                msg = 'Password and Re-enter password do not match.'
                return render_template('register.html', msg=msg)
        return render_template('register.html')
    except Exception as e:
        return render_template('register.html', msg=e)


@app.route("/home")
def home():
    return render_template("index.html")


@app.route('/index', methods=['POST'])
def index():
    try:
        ui = []
        print("ui : ", ui)

        if request.method == 'POST':
            ui.append(float(request.form['i1']))
            ui.append(float(request.form['i2']))
            ui.append(float(request.form['i3']))
            ui.append(float(request.form['i4']))
            ui.append(float(request.form['i5']))
            ui.append(float(request.form['i6']))
            ui.append(float(request.form['i7']))
            ui.append(float(request.form['i8']))
            ui.append(float(request.form['i9']))
            ui.append(float(request.form['i10']))

            print("ui : ", ui)

            cl, prob = AirQualityPrediction([ui])

            formatted_score = "{:.2f}%".format(prob)

            return render_template('result.html', cl=cl, prob=formatted_score)
    except Exception as e:
        return render_template('index.html', msg=e)
    

@app.route('/password', methods=['POST', 'GET'])
def password():
    if request.method == 'POST':
        current_pass = request.form['current']
        new_pass = request.form['new']
        verify_pass = request.form['verify']
        r1 = pd.read_excel('user.xlsx')
        for index, row in r1.iterrows():
            if row["password"] == str(current_pass):
                if new_pass == verify_pass:
                    r1.loc[index, "password"] = verify_pass
                    r1.to_excel("user.xlsx", index=False)
                    msg1 = 'Password changed successfully'
                    return render_template('password.html', msg=msg1)
                else:
                    msg = 'Re-entered password is not matched'
                    return render_template('password.html', msg=msg)
        else:
            msg3 = 'Incorrect Password'
            return render_template('password.html', msg=msg3)
    return render_template('password.html')


@app.route('/submit', methods=['POST', 'GET'])
def submit():
    if request.method == 'POST':
        graph_name = request.form['text']
        graph = ''
        name = ''
        if graph_name == "r_cr":
            model_name = "Random Forest Algorithm"
            name = "Accuracy Plot Graph "
            graph = "static/graphs/r_cr.png"
        elif graph_name == 'r_cm':
            model_name = "Random Forest Algorithm"
            name = "Loss Plor Graph"
            graph = "static/graphs/r_cm.png"

        elif graph_name == 's_cr':
            model_name = "Support Vector Classifier"
            name = "Classification Report"
            graph = "static/graphs/s_cr.png"
        elif graph_name == 's_cm':
            model_name = "Support Vector Classifier"
            name = "Confusion Matrix"
            graph = "static/graphs/s_cm.png"    

        

        return render_template('graph.html', mn=model_name, name=name, graph=graph)
    
    
@app.route('/graphs', methods=['POST', 'GET'])
def graphs():
    return render_template('graph.html')

if __name__ == '__main__':
    app.run(debug=True, port=5004)
