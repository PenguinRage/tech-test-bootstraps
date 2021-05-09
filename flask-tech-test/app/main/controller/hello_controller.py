from flask import request
from flask_restx import Resource, Namespace

api = Namespace('hello', description='helloWorld related operations')


@api.route('/')
class HelloWorld(Resource):
    @api.doc("Obiwon just making a friendly Hello World request")
    def get(self):
        return "Obiwon says: Hello there"
