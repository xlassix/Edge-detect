from flask import Flask, Response, jsonify 
from flask_restplus import Api, Resource, fields, reqparse 
from flask_cors import CORS, cross_origin import os 
# the app 
app = Flask(__name__) 
CORS(app) 
api = Api(app, version='1.0', title='APIs for Python Functions', validate=False) ns = api.namespace('primality', 'Returns a list of all primes below a given upper bound') 
# load the algo 
import conv as algo 
''' We import our function `Erasosthenes` from the file prime_sieve.py. You create all the classes and functions that you want in that file, and import them into the app. ''' 


# model the input data 
model_input = api.model('Enter the upper bound:', { "UPPER_BOUND": fields.Integer(maximum=10e16)}) 
