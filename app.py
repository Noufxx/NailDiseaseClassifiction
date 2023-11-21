from __future__ import division, print_function
# coding=utf-8
import sys
import os
import glob
import re
import numpy as np
import pickle
import tensorflow as tf
from datetime import datetime
import random
import string
from flask_mail import Mail, Message

# Keras
from keras.applications.imagenet_utils import preprocess_input, decode_predictions
from keras.models import load_model
from keras.preprocessing import image

# Flask utils
from flask import Flask, redirect, url_for, request, render_template, session, flash
import bcrypt
from flask_mysqldb import MySQL
import MySQLdb.cursors
from werkzeug.utils import secure_filename
from gevent.pywsgi import WSGIServer

# Define a flask app
app = Flask(__name__)
app.secret_key = "super secret key"
# db connection
app.config["MYSQL_HOST"] = "localhost"
app.config['MYSQL_PORT'] = 3306
app.config["MYSQL_USER"] = "root"
app.config["MYSQL_PASSWORD"] = ""
app.config["MYSQL_DB"] = "nail_dataset"
app.config["MYSQL_CURSORCLASS"] = "DictCursor"

mysql = MySQL(app)

# email configuration
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'nailscope2023@gmail.com'
app.config['MAIL_PASSWORD'] = 'kiyoufwdirphyauq'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
mail = Mail(app)

# Model saved with Keras model.save()
DL_PATH = 'models\DenseNet201_SGDClassifier_melanoma.h5'
ML_PATH = 'models\SGDClassifier_dense201_model(94)_melanoma.sav'

# Load your trained DL model
DL_model = load_model(DL_PATH)

# Load your trained ML model
ML_model = pickle.load(open(ML_PATH, 'rb'))

UPLOAD_FOLDER = './static/uploads/'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Prediction Model Done by: Dalia Ahmed Alzahrani - ID: 2190005273
def model_predict(img_path):
    img= tf.keras.utils.load_img(img_path, target_size=(224, 224))
    img = tf.keras.utils.img_to_array(img)
    img = np.true_divide(img, 255)
    img = np.expand_dims(img, axis=0)
    features = DL_model.predict(img)
    reshaped_features = features.reshape(features.shape[0], -1)
    # classification
    pred = ML_model.predict(reshaped_features)[0]

    return pred


@app.route('/', methods=['GET'])
def index():
    if "username" in session:
        return render_template('user_main.html')
    else:
        return render_template('index.html')


# Signin Done by: Dalia Ahmed Alzahrani - ID: 2190005273
@app.route('/signin', methods=["GET", "POST"])
def signin():
    if request.method == 'GET':
        return render_template('signin.html')
    else:
        session.pop("username", None)
        username = request.form['username']
        password = request.form['pass'].encode('utf-8')

        cur = mysql.connection.cursor()
        cur.execute("SELECT * FROM users WHERE Username=%s", (username,))
        user = cur.fetchone()
        cur.close()

        if user:
            if bcrypt.hashpw(password, user["Password"].encode('utf-8')) == user["Password"].encode('utf-8'):
                session['username'] = user['Username']
                if (user["Type"]== "User"):
                    return render_template("user_main.html") #return the sigend in user interface
                else:
                    session['admin_name'] = user['First_Name']
                    return redirect(url_for('admin')) #return the sigend in admin interface
            else:
                return render_template("signin.html", passmsg="Incorrect password")
        else:
            return render_template("signin.html", usermsg="Username does not exists")

# Signup Done by: Dalia Ahmed Alzahrani - ID: 2190005273
@app.route('/signup', methods=["GET", "POST"])
def signup():
    if request.method == 'GET':
        return render_template('signup.html')
    else:
        fname = request.form['fname']
        lname = request.form['lname']
        dob = request.form['dob']
        nat = request.form['nat']
        gender = request.form['gender']
        username = request.form['username']
        password = request.form['pass1'].encode('utf-8')
        hash_pass = bcrypt.hashpw(password, bcrypt.gensalt())
        email = request.form['email']

        cur = mysql.connection.cursor()
        cur.execute("SELECT * FROM users WHERE Username=%s", (username,))
        exist = cur.fetchone()

        if exist:
            return render_template("signup.html", msg="Username already exists")
        else:
            cur.execute("INSERT INTO users (Username, Password, First_Name, Last_Name, Email, Gender, DOB, Nationality, Type) VALUES (%s,%s,%s, %s, %s, %s, %s, %s, %s )",
                        (username, hash_pass, fname, lname, email, gender, dob, nat, "User"))
            mysql.connection.commit()
            session['username'] = username
            return render_template("user_main.html") #return the sigend in user interface
        
@app.route('/logout', methods=["GET", "POST"])
def logout():
    session.clear()
    return render_template('index.html') #redirect to guest homepage

#Upload Image Done by: Dalia Ahmed Alzahrani - ID: 2190005273
@app.route('/upload', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        # Get the file from post request
        f = request.files['file']

        # Save the file to ./uploads
        filename = secure_filename(f.filename)
        file_path=os.path.join(app.config['UPLOAD_FOLDER'], filename)
        f.save(file_path)
        # Make prediction
        preds = model_predict(file_path)

        classes = ['Beaus Lines', 'Eczema', 'Healthy', 'Melanoma']

        result = classes[preds]

        #medical advice
        if result == "Beaus Lines":
            advice="Avoid artificial nails or harsh nail products, and Keep blood sugar under control if you have diabetes. Please visit your healthcare provider if the condition worsen"
        if result == "Eczema":
            advice="Avoiding irritating products, ecessive water contact, and moistrize regularly. Please visit your healthcare provider if the condition worsen"
        if result == "Melanoma":
            advice="It is adviced to make an appointment to see a certified dermatologist to treat melanoma."
        if result == "Healthy":
            advice=""

        #check if user is signed in or not (to save results in database)
        if "username" in session:
            username= session["username"]
            date = datetime.now()
            date = date.strftime("%Y-%m-%d %I:%M:%S %p")
            cur = mysql.connection.cursor()
            cur.execute("INSERT INTO diagnosis (Username, Photo, Diagnosis, Date, Advice) VALUES (%s, %s, %s, %s, %s)",
                        (username, filename, result, date, advice)) 
            mysql.connection.commit()
            return render_template('result_user.html', pred=result, date1=date, advice1=advice, img=file_path)
        else:
            date = datetime.now()
            date = date.strftime("%Y-%m-%d %I:%M:%S %p")
            return render_template('result_guest.html', pred=result, date1=date, advice1=advice, img=file_path)
    return None


@app.route('/profile',methods=['GET','POST'])
def index_Profile():
    username= session["username"]
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM users WHERE Username=%s", (username,))
    userDetails = cur.fetchall()
    cur2 = mysql.connection.cursor()
    resultValue2 =cur2.execute("SELECT * FROM diagnosis WHERE Username=%s", (username,))
    if(resultValue2>0):
        userDetails2 = cur2.fetchall()
        return render_template('profile3.html',userDetails=userDetails,userDetails2=userDetails2)
    else:
        return render_template('profile3.html',userDetails=userDetails,msg="There is no past diagnosis avaliable")

@app.route("/index2")
def index2():
    username= session["username"]
    cur3 = mysql.connection.cursor()
    resultValue3 =cur3.execute("SELECT * FROM users WHERE Username= %s", (username,))
    userDetails3 = cur3.fetchall()
    cur4 = mysql.connection.cursor()
    resultValue4 =cur4.execute("SELECT * FROM diagnosis WHERE Username= %s", (username,))
    if(resultValue4>0):
        userDetails4 = cur4.fetchall()
        return render_template('profile_edit3.html',userDetails3=userDetails3,userDetails4=userDetails4)
    else:
        return render_template('profile_edit3.html',userDetails3=userDetails3,msg2="There is no past diagnosis avaliable")
    

@app.route("//", methods=['POST','GET'])
def form():
    if request.method == 'POST':
        userDetailsForm= request.form
        Fname=userDetailsForm['FName']
        Gen=userDetailsForm['gender']
        Lname=userDetailsForm['LName']
        useName=userDetailsForm['UName']
        dob=userDetailsForm['DOB']
        email=userDetailsForm['email']
        nat=userDetailsForm['Nat']
        sess_user= session["username"]
        cur_form = mysql.connection.cursor()
        cur_form.execute("UPDATE users SET Username=%s,First_Name=%s,Last_Name=%s,Email=%s,Gender=%s,DOB=%s,Nationality=%s WHERE Username=%s",(useName,Fname,Lname,email,Gen,dob,nat, sess_user,))
        mysql.connection.commit()
        cur_form.close()
        flash('Information has been updated successfully', 'success')
        return redirect(url_for('index_Profile'))
        
@app.route("/view/", methods=['POST','GET'])
def view_pd():
   diag_ID = request.form['diagnos_ID']
   session["diag_ID"]=diag_ID
   curD = mysql.connection.cursor()
   resultValueD =curD.execute("SELECT * FROM diagnosis WHERE Diagnosis_ID=%s",(diag_ID,))
   userDetailsD = curD.fetchall()
   return render_template('View_PD.html',userDetailsD=userDetailsD)

@app.route("/print/", methods=['POST','GET'])
def print_pd():
    if "diag_ID" in session:
        diag_ID=session["diag_ID"]
        curD = mysql.connection.cursor()
        resultValueD =curD.execute("SELECT * FROM diagnosis WHERE Diagnosis_ID=%s",(diag_ID,))
        userDetailsD = curD.fetchall()
        return render_template('View_PD.html',userDetailsD=userDetailsD)
    


# Generate Random Code Done by: Maram Lutfi Alfaraj - ID: 2190001583
def generateVerificationCode():
    source = string.ascii_letters + string.digits + string.ascii_uppercase
    verificationCode = ''.join((random.choice(source) for i in range(8)))
    return verificationCode


#Send Verificaiton Code To Email Done by: Maram Lutfi Alfaraj - ID: 2190001583
@app.route("/send", methods=['GET', 'POST'])
def sendCode():
    session['vCode'] = str(generateVerificationCode())
    msg = Message("NailScope Support", sender='nailscope2023@gmail.com', recipients=[session['vEmail']])
    msg.body = "\n\nHello, \nUse the below code to reset your account password:\n\n" + session['vCode'] + "\nDidn't ask for a new password? You can ignore this email." 
    mail.send(msg)
    #Redirect to verificaitonCode page
    return redirect(url_for('verificationCode'))


#forgotPassword page Done by: Maram Lutfi Alfaraj - ID: 2190001583
@app.route("/forgotPassword", methods=['GET', 'POST'])
def forgotPassword():
    if request.method == 'GET':
            return render_template('forgotPassword.html')
    if request.method == 'POST':
        email = request.form['email_fp']
        #Check if enterd email is valid
        if  email=='':
            return render_template('forgotPassword.html', errormsg="Email address cannot be blank")
        elif not re.fullmatch("[^@]+@[^@]+\.[^@]+", email):
            return render_template('forgotPassword.html', errormsg="Please enter a valid email address")
        #Check if email exists in the database
        else: 
            cur = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
            cur.execute("SELECT Email FROM users WHERE Email = %s", (email,))
            mailExist = cur.fetchone()
            #If email exists send verificaiton code
            if mailExist:
                cur.close()
                session['vEmail'] = email
                return redirect(url_for('sendCode'))
            else:
                return render_template("forgotPassword.html", errormsg="There is no account with this email")

#verificaitionCode page Done by: Maram Lutfi Alfaraj - ID: 2190001583
@app.route("/verificationCode", methods=['GET', 'POST'])
def verificationCode():
    if request.method == 'POST':
        vCodeField = request.form['vc_textbox']
        #Check verifiactionCode
        if vCodeField == '':
            return render_template('verificationCode.html', errormsg="Enter the verification code")
        elif not session['vCode'] == vCodeField:
            return render_template('verificationCode.html', errormsg="Invalid verification code")
        else:
            #if verifcation code is valid then redirect to resetPassword page
            return render_template('resetPassword.html', errormsg="")
    else:
        return render_template('verificationCode.html', errormsg="")


#resetPassword page Done by: Maram Lutfi Alfaraj - ID: 2190001583
@app.route("/resetPassword", methods=['GET', 'POST'])
def resetPassword():
    errormsg=""
    updateMsg=""
    if request.method == 'GET':
        return render_template('resetPassword.html')
    else:
        email = session['vEmail']
        newPass = request.form['rs_pass1']
        confirmPass = request.form['rs_pass2']
        #validate the new password
        if(newPass == '' or confirmPass == ''):
            return render_template('resetPassword.html', errormsg="Password and Confirm password fields can not be blank")
        elif not re.fullmatch("^(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[0-9])(?=.*?[#?!@$%^&*-_]).{8,}$", newPass):
            return render_template('resetPassword.html', errormsg="Please enter a valid password, click on the icon for instructions.")
        elif not newPass == confirmPass:
            return render_template('resetPassword.html', errormsg="Password and Confirm password fields must match")
        else:
            #encoding the new password
            password = newPass.encode('utf-8')
            hash_pass = bcrypt.hashpw(password, bcrypt.gensalt())
            cur = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
            #Store the new password in database
            cur.execute("UPDATE users SET Password = %s WHERE Email = %s", (hash_pass, email))
            mysql.connection.commit()
            cur.close()
            session.pop('vEmail',None)  
            session.pop('vCode',None) 
            # redirect the user to the login page
            return render_template('signin.html', updateMsg="Password Updated Successfully!")

@app.route('/admin', methods=["GET", "POST"])
def admin():
        cur = mysql.connection.cursor()
        cur.execute("SELECT * FROM blogs")
        blogs= cur.fetchall()
        return render_template('admin.html', blogs= blogs, name=session['admin_name'])

@app.route("/edt/<int:Blog_ID>")
def edt(Blog_ID):
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM blogs WHERE Blog_ID= %s", (Blog_ID,))
    blogDetails = cur.fetchone()
    return render_template('EditBlog.html',blogDetails=blogDetails)

# blog Detailes       
@app.route('/blogDetailes/<int:Blog_ID>')
def blogDet(Blog_ID):
   cur = mysql.connection.cursor()
   cur.execute("SELECT * FROM blogs WHERE Blog_ID=%s",(Blog_ID,))
   details= cur.fetchone()
   return render_template('blogDetailes.html', details = details)

# User blogs
@app.route('/blogUser/', methods=["GET", "POST"])
def blogUser():
        cur = mysql.connection.cursor()
        cur.execute("SELECT * FROM blogs")
        blogs= cur.fetchall()
        return render_template('blogUser.html', blogs= blogs)

# Delete blog
@app.route('/admin/<int:Blog_ID>')
def DelBlog(Blog_ID):
  cur = mysql.connection.cursor()
  cur.execute("DELETE FROM blogs WHERE Blog_ID=%s",(Blog_ID,))
  mysql.connection.commit()
  flash('Blog has been deleted successfully!', 'success')
  return redirect(url_for('admin'))
                #   , Delmsg="Blog Deleted Successfully!")

# Edit blog
@app.route('/EditBlog/<int:Blog_ID>', methods=["GET", "POST"])
def EditBlog(Blog_ID):
      if request.method == 'POST':
        Author_name = request.form['Author_name']
        Title = request.form['Title']
        Description = request.form['Description']
        Content = request.form['Content']
        Date = request.form['Date']
        Photo = request.form['Photo']
        Reference = request.form['Reference']
        
        cur = mysql.connection.cursor()
        cur.execute("UPDATE blogs SET Author_name=%s,Title=%s,Description=%s,Content=%s,Date=%s,Photo=%s,Reference=%s WHERE Blog_ID=%s",(Author_name,Title,Description,Content,Date,Photo,Reference,Blog_ID,))
        mysql.connection.commit()
        cur.close()
        flash('Blog has been updated successfully!', 'success')
        return redirect(url_for('admin'))


        
# Add a blog
@app.route('/AddBlog/', methods=["GET", "POST"])

def AddBlog():
      if request.method == 'GET':
        return render_template('AddBlog.html')
      else:
        Author_name = request.form['Author_name']
        Title = request.form['Title']
        Description = request.form['Description']
        Content = request.form['Content']
        Date = request.form['Date']
        Photo = request.form['Photo']
        Reference = request.form['Reference']

        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO blogs(Author_name, Title, Description, Content, Date, Photo, Reference) VALUES (%s,%s,%s, %s, %s, %s, %s)", (Author_name, Title, Description, Content, Date, Photo, Reference) )
        mysql.connection.commit()
        cur.close()
        flash('Information has been Added successfully!', 'success')
        return redirect(url_for('admin'))
     

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
