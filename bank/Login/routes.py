from flask import render_template, url_for, flash, redirect, request, Blueprint
from bank import app, conn, bcrypt
from bank.forms import CustomerLoginForm, EmployeeLoginForm, UniversityForm, ReviewForm,LoginForm
from flask_login import login_user, current_user, logout_user, login_required
from bank.models import select_Users, get_unis
import psycopg2
#202212
from bank import roles, mysession
from flask_login import current_user

Login = Blueprint('Login', __name__)

#Put uni reviews here ARM
posts = [{}]

user_login = None


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
    
    #Connetct to db
    conn = get_db_connection()
    cur = conn.cursor()
    
    form = ReviewForm()
    #form2 = LoginForm()

    #TODO Put new review in DB
    if form.validate_on_submit():
        title = form.title.data
        content = form.content.data
        score = form.score.data
        print(university)
        print(title)
        print(content)
        print(score)

        #SQL command for inserting review
        #insert id below instead of uniID 1
        cur.execute('insert into reviews values (1, ' + str(score) + ', \'' + content + '\', \'' + title + '\', 0)')

    #TODO check if user has logged in and get username

    if current_user.is_authenticated:
        flash('You are logged in!', 'success')
    else:
        flash('Login in order to post a review', 'danger')

    #Find rating in db
    rating = cur.execute(f'select u.average_rating from universities as u where u.university_name=\'{university}\';')
    #get reviews from db
    cur.execute(f'SELECT r.title AS title, us.username AS user, r.comment AS content, r.rating AS score, r.votes_no AS vote FROM review_of ro JOIN universities u ON ro.university_id = u.id JOIN reviews r ON ro.review_id = r.id JOIN gave_review gr ON ro.review_id = r.id JOIN users us ON gr.user_id = us.id WHERE u.university_name=\'{university}\';')
    posts = cur.fetchall()
    #posts=[{"title": "Test1","user":"Andreas","content": "hay","score": 5,"vote":3},{"title": "Test2","user":"Andreas","content": "hay","score": 4,"vote":3},{"title": "Test3","user":"Andreas","content": "hay","score": 3,"vote":5}]
    
    return render_template('university.html', name=university, form=form ,rating=rating , posts=posts)




@Login.route("/login", methods=['GET', 'POST'])
def login():

    #202212
    mysession["state"]="login"
    print(mysession)
    role=None

    if current_user.is_authenticated:
        return redirect(url_for('Log in.home'))

    
    form = LoginForm()

    
    if form.validate_on_submit():
        # select users i model.py finder user baseret på email, dette kan ændres efter ønske
        user = select_Users(form.id.data)

        # tjek om 4. felt i user er lig form.password
        if user != None and user[3] == form.password.data:

            #202212
            mysession["role"] = roles[1] #Logged in


            mysession["id"] = form.id.data
            print(mysession)
            print(roles)

            login_user(user, remember=form.remember.data)
            flash('Login successful.','success')
            next_page = request.args.get('next')
            user_login  = user
            return redirect(next_page) if next_page else redirect(url_for('Login.home'))
        else:
            flash('Login Unsuccessful. Please check identifier and password', 'danger')
        
        #cur.close()
        #conn.close()

    #202212
    role =  mysession["role"]
    print('role: '+ role)

    #return render_template('login.html', title='Login', is_employee=is_employee, form=form)
    return render_template('login.html', title='Login', form=form, role=role)

def get_db_connection():
    conn = psycopg2.connect(host='localhost',
                            database='unirecommender',
                            user='postgres',
                            password='1234')
    return conn

@Login.route("/logout")
def logout():
    #202212
    mysession["state"]="logout"
    print(mysession)
    user_login = None
    logout_user()
    return redirect(url_for('Login.home'))


@app.route('/post_review', methods=['GET', 'POST'])
def post_review():
    form = ReviewForm()
    posts = []  # Initialize the variable outside the if statement
    #print(form)
    if form.validate_on_submit():
        # Store the review in the database (using appropriate SQL queries or ORM)
        # ...
        
        flash('Review posted successfully', 'success')  # Optional: Display a success message
        
        return redirect(url_for('post_review'))  # Redirect to the same page to prevent form resubmission
    
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('SELECT * FROM Reviews')
    posts = cur.fetchall()
    cur.close()
    conn.close()
    
    return render_template('review.html', name="Your", posts=posts, form=form)
