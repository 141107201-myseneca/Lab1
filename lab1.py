#!/usr/bin/python 3

def age()
    try:
        age= input('What is your age? ')
        print('You are ' + age + ' years old')
    except TypeError:
        return 'Please enter an int'

def helloWord():
    print('Hello World')


if '__name__' == '__main__':
    age()
    helloWorld()

