from flask import Flask
from flask_restful import Api
from vistas import VistaGenerar


# ----------> FLASK APP
app = Flask(__name__)


app.config['PROPAGATE_EXCEPTIONS'] = True

app.app_context().push()

api = Api(app)

api.add_resource(VistaGenerar, '/conv')
