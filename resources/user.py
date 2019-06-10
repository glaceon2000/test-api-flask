import sqlite3
from flask_restful import Resource, reqparse
from models.user import UserModel


class UserRegister(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('username', type = str, required = True, help = 'CANT BE BLANK BITCH')
    parser.add_argument('password', type = str, required = True, help = 'CANT BE BLANK BITCH')

    def post(self):

        data = UserRegister.parser.parse_args()
        if UserModel.find_by_username(data['username']):
            return {"mess": "this has been already used"}, 400

        user = UserModel(**data)
        user.save_to_db()

        return {"ID": user.id, "NAME": user.username, "MESSAGE": 'SUCCEEDED'}, 201
