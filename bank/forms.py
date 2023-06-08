from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, IntegerField, SelectField,SelectMultipleField
from wtforms.validators import DataRequired, Length, EqualTo, ValidationError


class UniversityForm(FlaskForm):
    select = SelectMultipleField('Select Universtity'  , choices=["Uni1","Uni2","Uni3"], validators=[DataRequired()])
    #select = SelectField('From Account:'  , choices=[], coerce = int, validators=[DataRequired()])
    submit = SubmitField('Select')

class ReviewForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    content = StringField('Content', validators=[DataRequired()])
    score = IntegerField('Score', validators=[DataRequired()])
    submit = SubmitField('Post')

class LoginForm(FlaskForm):
    id = StringField('UserName', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')

class AddCustomerForm(FlaskForm):
    username = StringField('Username',
                           validators=[DataRequired(), Length(min=2, max=20)])
    CPR_number = IntegerField('CPR_number',
                        validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Add')


class CustomerLoginForm(FlaskForm):
    id = IntegerField('CPR_number', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')

class EmployeeLoginForm(FlaskForm):
    id = IntegerField('Id', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')

class TransferForm(FlaskForm):
    amount = IntegerField('amount', 
                        validators=[DataRequired()])
    #sourceAccountTest = SelectField('From Account test:', choices=dropdown_choices, validators=[DataRequired()])
    sourceAccount = SelectField('From Account:'  , choices=[], coerce = int, validators=[DataRequired()])
    targetAccount = SelectField('Target Account:', choices=[], coerce = int, validators=[DataRequired()])
    submit = SubmitField('Confirm')

class DepositForm(FlaskForm):
    amount = IntegerField('amount', 
                       validators=[DataRequired()])
    submit = SubmitField('Confirm')
    
class InvestForm(FlaskForm):
    submit = SubmitField('Confirm')