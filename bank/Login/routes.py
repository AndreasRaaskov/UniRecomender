from flask import render_template, url_for, flash, redirect, request, Blueprint
from bank import app, conn, bcrypt
from bank.forms import CustomerLoginForm, EmployeeLoginForm, UniversityForm, ReviewForm,LoginForm
from flask_login import login_user, current_user, logout_user, login_required
from bank.models import Customers, select_Customers, select_Employees
from bank.models import select_cus_accounts
#202212
from bank import roles, mysession

Login = Blueprint('Login', __name__)

#Put uni reviews here ARM
posts = [{}]


@Login.route("/", methods=['GET', 'POST'])
@Login.route("/home", methods=['GET', 'POST'])
def home():
    #202212
    mysession["state"]="home or /"
    print(mysession)
    #202212
    role =  mysession["role"]
    print('role: '+ role)

    form = UniversityForm()

    return render_template('home.html', form=form, posts=posts, role=role)

#ARM Select uni
@app.route('/university', methods=['POST'])
def show_uni():
    university = request.form.get('select')
    print(university)
    
    form = ReviewForm()

    #TODO Put new review in DB
    if form.validate_on_submit():
        title = form.title.data
        content = form.content.data
        score = form.score.data
        print(title)
        print(content)
        print(score)

    #TODO check if user has logged in and get username

    #TODO Find rating in DB
    rating = 4

    #TODO Find reviews in DB
    posts=[{"title": "Test1","user":"Andreas","content": "hay","score": 5,"vote":3},{"title": "Test2","user":"Andreas","content": "hay","score": 4,"vote":3},{"title": "Test3","user":"Andreas","content": "hay","score": 3,"vote":5}]
    return render_template('university.html', name=university, form=form ,rating=rating , posts=posts)


@Login.route("/about")
def about():
    #202212
    mysession["state"]="about"
    print(mysession)
    return render_template('about.html', title='About')


@Login.route("/login", methods=['GET', 'POST'])
def login():

    #202212
    mysession["state"]="login"
    print(mysession)
    role=None

    if current_user.is_authenticated:
        return redirect(url_for('Login.home'))

    
    form = LoginForm()

    
    if form.validate_on_submit():

        #"202212"
        user = form.id.data


        if user != None and bcrypt.check_password_hash(user[2], form.password.data):

            #202212
            mysession["role"] = roles[1] #Logged in


            mysession["id"] = form.id.data
            print(mysession)
            print(roles)

            login_user(user, remember=form.remember.data)
            flash('Login successful.','success')
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('Login.home'))
        else:
            flash('Login Unsuccessful. Please check identifier and password', 'danger')

    #202212
    role =  mysession["role"]
    print('role: '+ role)

    #return render_template('login.html', title='Login', is_employee=is_employee, form=form)
    return render_template('login.html', title='Login', form=form, role=role)


@Login.route("/logout")
def logout():
    #202212
    mysession["state"]="logout"
    print(mysession)

    logout_user()
    return redirect(url_for('Login.home'))



