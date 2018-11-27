from flask import Flask
from flask_restful import Resource, Api
from contextlib import closing
from flask import jsonify
import sqlite3

db_name = 'twitch.db'
app = Flask(__name__)
api = Api(app)


class Account(Resource):
    def get(self):
        with closing(sqlite3.connect(db_name)) as con:
            with con:
                account = con.execute('SELECT * FROM romique_lol').fetchone()
        return {account[0]: account[1]}

class Stats(Resource):
    def get(self):
        with closing(sqlite3.connect(db_name)) as con:
            with con:
                data = con.execute('SELECT * FROM howtoplayad_counters').fetchall()
        result = {'data': data}
        return jsonify(result)

api.add_resource(Account, '/account')  # Route_1
api.add_resource(Stats, '/stats')  # Route_2


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5002')
