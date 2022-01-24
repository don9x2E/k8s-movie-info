from flask import Flask, request, Response
from flask_restx import Resource, Api, fields
from flask import abort, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
api = Api(app)

movieinfo_ns = api.namespace('movieinfo_ns', description='Flask REST APIs for Movie Information')

movie_data = api.model(
    'Movie Info',
    {
      "title": fields.String(description="title", required=True),
      "summary": fields.String(description="summary", required=True),
      "runningtime": fields.Integer(description="runningtime", required=True)
    }
)

movie_info = {}

@movieinfo_ns.route('/movies')
class movies(Resource):
  def get(self):
    return {
        'MOVIE': movie_info
    }

@movieinfo_ns.route('/movies/<string:title>')
class movies_name(Resource):
  # READ
  def get(self, title):
    data = movie_info[title]
    return {
        'data': data
    }

  @api.expect(movie_data)
  # CREATE
  def post(self, title):
    params = request.get_json()
    movie_info[title] = params
    return Response(status=200)

  # UPDATE
  @api.expect(movie_data)
  def put(self, title):
    params = request.get_json()
    movie_info[title] = params
    return Response(status=200)

  # DELETE
  def delete(self, title):
    del movie_info[title]
    return Response(status=200)
if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)
