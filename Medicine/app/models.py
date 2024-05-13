from sqlalchemy import Enum

from app import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)
    is_active = db.Column(db.Boolean, default=True)

    def __init__(self, username, password):
        self.username = username
        self.password = password

    def __repr__(self):
        return f"User('{self.username}')"

    @property
    def password(self):
        raise AttributeError('Password is not a readable attribute')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)


class Doctor(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    surname = db.Column(db.String(50), nullable=False)
    firstname = db.Column(db.String(50), nullable=False)
    patronymic = db.Column(db.String(50))
    dob = db.Column(db.Date)
    education = db.Column(db.String(100))
    workplace = db.Column(db.String(100))
    practice_profile = db.Column(db.String(100))
    phone = db.Column(db.String(15))
    photo_path = db.Column(db.String(255))  # Added field for storing photo filename

    user = db.relationship('User', backref=db.backref('doctor', uselist=False))

    def to_dict(self):
        return {
            'id': self.id,
            'surname': self.surname,
            'firstname': self.firstname,
            'patronymic': self.patronymic,
            'dob': self.dob.isoformat() if self.dob else None,
            'education': self.education,
            'workplace': self.workplace,
            'practice_profile': self.practice_profile,
            'phone': self.phone,
            'photo_path': self.photo_path
        }

    def __str__(self):
        return f"Doctor: {self.surname} {self.firstname} {self.patronymic}, ID: {self.id}"


class Patient(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    surname = db.Column(db.String(50), nullable=False)
    firstname = db.Column(db.String(50), nullable=False)
    dob = db.Column(db.Date)
    region = db.Column(db.String(2))
    phone = db.Column(db.String(15))
    photo_path = db.Column(db.String(255))  # Added field for storing photo filename

    user = db.relationship('User', backref=db.backref('patient', uselist=False))

    def __str__(self):
        return f"Patient: {self.surname} {self.firstname} {self.middle_name}, ID: {self.id}"


class Appointment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    doctor_id = db.Column(db.Integer, db.ForeignKey('doctor.id'), nullable=False)
    patient_id = db.Column(db.Integer, db.ForeignKey('patient.id'), nullable=True)
    appointment_date_time = db.Column(db.DateTime)
    appointment_details = db.Column(db.Text, nullable=True)

    doctor = db.relationship('Doctor', backref=db.backref('appointments'))
    patient = db.relationship('Patient', backref=db.backref('appointments'))

    def __str__(self):
        return (f"Appointment ID: {self.id}, "
                f"Doctor: {self.doctor.surname} {self.doctor.firstname}, "
                f"Patient: {self.patient.surname} {self.patient.firstname}, "
                f"Date and Time: {self.appointment_date_time}, "
                f"Details: {self.appointment_details}.")


class Gender(Enum):
    MALE = 'male'
    FEMALE = 'female'


class MedicalCard(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    patient_id = db.Column(db.Integer, db.ForeignKey('patient.id'), nullable=False)
    surname = db.Column(db.String(100))
    firstname = db.Column(db.String(100))
    patronymic = db.Column(db.String(100))
    gender = db.Column(db.String(10))
    dob = db.Column(db.Date)
    passport = db.Column(db.String(100))
    family = db.Column(db.String(100))
    document_type = db.Column(db.String(100))
    document_serial = db.Column(db.String(20))
    document_number = db.Column(db.String(20))
    document_authority = db.Column(db.String(100))
    document_issue_date = db.Column(db.Date)
    region = db.Column(db.String(100))
    city = db.Column(db.String(100))
    street = db.Column(db.String(100))
    house = db.Column(db.String(20))
    building = db.Column(db.String(20))
    entrance = db.Column(db.String(20))
    apartment = db.Column(db.String(20))
    home_phone = db.Column(db.String(20))
    registration_region = db.Column(db.String(100))
    registration_city = db.Column(db.String(100))
    registration_street = db.Column(db.String(100))
    registration_house = db.Column(db.String(20))
    registration_building = db.Column(db.String(20))
    registration_entrance = db.Column(db.String(20))
    registration_apartment = db.Column(db.String(20))
    insurance_serial = db.Column(db.String(20))
    insurance_number = db.Column(db.String(20))
    disability = db.Column(db.String(100))
    disability_group = db.Column(db.String(100))
    benefit_document = db.Column(db.String(100))
    payment_type = db.Column(db.String(100))
    allergic_history = db.Column(db.String(255))
    medication_intolerance = db.Column(db.String(255))
    blood_group = db.Column(db.String(10))
    rhesus = db.Column(db.String(10))
    blood_belongs = db.Column(db.String(100))
    vaccine_reactions = db.Column(db.String(255))
    blood_transfusion = db.Column(db.String(255))
    surgical_intervention = db.Column(db.String(255))
    previous_infectious_diseases = db.Column(db.String(1000))

    patient = db.relationship('Patient', backref=db.backref('medical_card', uselist=False))

    def __str__(self):
        return f"{self.surname} {self.firstname} {self.patronymic}"

#
# class Patient(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
#     last_name = db.Column(db.String(50), nullable=False)
#     first_name = db.Column(db.String(50), nullable=False)
#     date_of_birth = db.Column(db.Date)
#     region = db.Column(db.String(2))
#     phone_number = db.Column(db.String(15))
#
#     user = db.relationship('User', backref=db.backref('patient', uselist=False))