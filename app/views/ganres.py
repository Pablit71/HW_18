from flask_restx import Resource, Namespace

from app.models import GenreSchema, Genre
from app.database import db

genres_ns = Namespace('genres')

genre_schema = GenreSchema()
genres_schema = GenreSchema(many=True)


@genres_ns.route('/')
class GenresView(Resource):
    def get(self):
        all_genres = Genre.query.all()
        return genres_schema.dump(all_genres), 200


@genres_ns.route('/<int:gid>')
class GenreView(Resource):
    def get(self, gid):
        try:
            genre = db.session.query(Genre).filter(Genre.id == gid).one()
            return genre_schema.dump(genre), 200
        except Exception as e:
            return str(e), 404
