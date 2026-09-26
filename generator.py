from random import randint


def email_generation(name, surname):

    num = randint(100, 999)
    email = f"{name}-{surname}{num}@gmail.com"
    return email

def valid_password_generator():

    password = randint(100000, 999999)
    return password

def invalid_password_generator():

    inv_password = randint(10000, 99999)
    return inv_password
