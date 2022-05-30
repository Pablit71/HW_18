from flask_restx import Resource, Namespace

from app.models import DirectorSchema, Director
from app.database import db

directors_ns = Namespace('directors')

director_schema = DirectorSchema()
directors_schema = DirectorSchema(many=True)


@directors_ns.route('/')
class DirectorsView(Resource):
    def get(self):
        all_directors = Director.query.all()
        return directors_schema.dump(all_directors), 200


@directors_ns.route('/<int:did>')
class DirectorView(Resource):
    def get(self, did):
        try:
            director = db.session.query(Director).filter(Director.id == did).one()
            return director_schema.dump(director), 200
        except Exception as e:
            return str(e), 404
