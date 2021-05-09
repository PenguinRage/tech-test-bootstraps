from flask_restx import Api
from flask import Blueprint

from .main.controller.hello_controller import api as hello_ns

blueprint = Blueprint('api', __name__)

api = Api(blueprint,
          title='FLASK RESTX API WITH JWT',
          version='1.0',
          description='Tech Test REST API'
          )

api.add_namespace(hello_ns, path='/hello')