import re

from flask_wtf import FlaskForm
from flask_wtf.file import FileRequired, FileAllowed
from wtforms import StringField, PasswordField, SubmitField
from wtforms.fields.choices import SelectField, RadioField
from wtforms.fields.datetime import DateField
from wtforms.fields.simple import FileField, TextAreaField
from wtforms.validators import DataRequired, Length, Email, ValidationError

RE_PHONE = r"^((8|\+374|\+994|\+995|\+375|\+7|\+380|\+38|\+996|\+998|\+993)[\- ]?)?\(?\d{3,5}\)?[\- ]?\d{1}[\- ]?\d{1}[\- ]?\d{1}[\- ]?\d{1}[\- ]?\d{1}(([\- ]?\d{1})?[\- ]?\d{1})?$"


class Phone(object):
    def __init__(self, message=None):
        if message is None:
            message = 'Invalid phone number'
        self.message = message

    def __call__(self, form, field):
        phone_number = field.data
        if not re.match(RE_PHONE, phone_number):
            raise ValidationError(self.message)


class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')

# class RegistrationForm(FlaskForm):
#     username = StringField('Username', validators=[DataRequired(), Length(min=4, max=20)])
#     password = PasswordField('Password', validators=[DataRequired(), Length(min=6)])
#     confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
#     submit = SubmitField('Sign Up')


class DoctorForm(FlaskForm):
    firstname = StringField('Имя', validators=[
        DataRequired(message="Введите ваше имя")])
    surname = StringField('Фамилия', validators=[
        DataRequired(message="Введите вашу фамилию")])
    patronymic = StringField('Отчество', validators=[
        DataRequired(message="Введите ваше отчество")])
    dob = DateField('Дата рождения: dd.mm.yyyy', validators=[
        DataRequired(message="Введите вашу дату рождения")])
    education = StringField('Образование', validators=[
        DataRequired(message="Введите ваше образование")])
    workplace = StringField('Место работы', validators=[
        DataRequired(message="Введите ваше место работы")])
    practice_profile = StringField('Профиль врачебной практики', validators=[
        DataRequired(message="Введите ваш профиль врачебной практики")])
    phone = StringField('Номер телефона', validators=[
        DataRequired(message="Введите ваш номер телефона"),
        Phone(message="Неправильный формат номера телефона.")])
    email = StringField('Адрес электронной почты', validators=[
        DataRequired(message="Введите ваш адрес электронной почты"),
        Email(message="Неправильный формат адреса электронной почты")])
    password = PasswordField('Пароль', validators=[
        DataRequired(message="Введите ваш пароль"),
        Length(min=6, message="Пароль должен содержать как минимум 6 символов")])
    photo = FileField('Фотография', validators=[
        FileRequired(message="Загрузите вашу фотографию"),
        FileAllowed(['jpg', 'jpeg', 'png'], message="Разрешены только файлы с расширениями .jpg, .jpeg, .png")])


class PatientForm(FlaskForm):
    firstname = StringField('Имя', validators=[
        DataRequired(message="Введите ваше имя")])
    surname = StringField('Фамилия', validators=[
        DataRequired(message="Введите вашу фамилию")])
    dob = DateField('Дата рождения: dd.mm.yyyy', validators=[
        DataRequired(message="Введите вашу дату рождения")])
    CHOICES = [('', 'Выберите регион'), ('BY', 'BY'), ('RU', 'RU'), ('KZ', 'KZ')]
    region = SelectField('Регион', choices=CHOICES, validators=[
        DataRequired(message="Выберите ваш регион")])
    phone = StringField('Номер телефона', validators=[
        DataRequired(message="Введите ваш номер телефона"),
        Phone(message="Неправильный формат номера телефона.")])
    email = StringField('Адрес электронной почты', validators=[
        DataRequired(message="Введите ваш адрес электронной почты"),
        Email(message="Неправильный формат адреса электронной почты")])
    password = PasswordField('Пароль', validators=[
        DataRequired(message="Введите ваш пароль"),
        Length(min=6, message="Пароль должен содержать как минимум 6 символов")])
    photo = FileField('Фотография', validators=[
        FileRequired(message="Загрузите вашу фотографию"),
        FileAllowed(['jpg', 'jpeg', 'png'], message="Разрешены только файлы с расширениями .jpg, .jpeg, .png")])


class MedicalCardForm(FlaskForm):
    surname = StringField('Фамилия', validators=[
        DataRequired()])
    firstname = StringField('Имя', validators=[
        DataRequired()])
    patronymic = StringField('Отчество')
    gender = RadioField('Пол', choices=[('male', 'Мужской'), ('female', 'Женский')])
    dob = DateField('Дата рождения: dd.mm.yyyy', validators=[
        DataRequired()])
    passport = StringField('Личный Номер паспорта')
    family = StringField('Семейное положение')
    document_type = StringField('Документ')
    document_serial = StringField('Серия документа')
    document_number = StringField('Номер документа')
    document_authority = StringField('Кем выдан')
    document_issue_date = DateField('Дата выдачи: dd.mm.yyyy')
    region = StringField('Область')
    city = StringField('Населенный пункт')
    street = StringField('Улица/Переулок/Проезд')
    house = StringField('Дом')
    building = StringField('Корпус')
    entrance = StringField('Подъезд')
    apartment = StringField('Квартира')
    home_phone = StringField('Домашний телефон' ''', validators=[
        Phone(message="Неправильный формат номера телефона.")]''')
    registration_region = StringField('Область регистрации')
    registration_city = StringField('Населенный пункт регистрации')
    registration_street = StringField('Улица/Переулок/Проезд регистрации')
    registration_house = StringField('Дом регистрации')
    registration_building = StringField('Корпус регистрации')
    registration_entrance = StringField('Подъезд регистрации')
    registration_apartment = StringField('Квартира регистрации')
    insurance_serial = StringField('Серия страхового полиса')
    insurance_number = StringField('Номер страхового полиса')
    disability = StringField('Инвалидность')
    disability_group = StringField('Группа инвалидности')
    benefit_document = StringField('Документ на льготное обслуживание')
    payment_type = StringField('Вид оплаты')
    allergic_history = StringField('Аллергический анамнез')
    medication_intolerance = StringField('Лекарственная непереносимость')
    blood_group = StringField('Группа крови')
    rhesus = StringField('Резус')
    blood_belongs = StringField('Принадлежность крови')
    vaccine_reactions = StringField('Реакции на прививки')
    blood_transfusion = StringField('Переливание крови')
    surgical_intervention = StringField('Хирургическое вмешательство')
    previous_infectious_diseases = TextAreaField('Перенесенные инфекционные заболевания')


