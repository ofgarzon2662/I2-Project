from flask import jsonify, request, Blueprint
from ..commands.create  import  Create
from ..commands.reset import Reset
from ..commands.list import List
from ..commands.detail import Detail
from ..commands.delete import Delete

routes_blueprint  = Blueprint('routes', __name__)

@routes_blueprint.route('/routes', methods=['POST'])
def create_route():
    request_json = request.get_json()
    result = Create(request_json.get('flightId', None), request_json.get('sourceAirportCode', None),
                    request_json.get('sourceCountry', None), request_json.get('destinyAirportCode', None),
                    request_json.get('destinyCountry', None), request_json.get('bagCost', None),
                    request_json.get('plannedStartDate', None), request_json.get('plannedEndDate', None),
                    request.headers.get('Authorization', None)).execute()
    return jsonify({'id': result['id'], 'createdAt': result['createdAt']}), 201

@routes_blueprint.route('/routes', methods = ['GET'])
def viewFilter():
    if request.args.get('flight') is None:
        flightId = None
    else:
        flightId = request.args.get('flight')
    result = List(flightId, request.headers.get('Authorization', None)).execute() 
    return jsonify(result)

@routes_blueprint.route('/routes/<string:id>', methods = ['GET'])
def view(id):
    print(id)
    result = Detail(id, request.headers.get('Authorization', None)).execute()
    return jsonify(result) 

@routes_blueprint.route('/routes/<string:id>', methods = ['DELETE'])
def delete(id):
    result = Delete(id, request.headers.get('Authorization', None)).execute()
    return jsonify({ 'msg': result['msg'] }), 200

@routes_blueprint.route("/routes/ping", methods=['GET'])
def healthcheck():
    return jsonify('pong'), 200

@routes_blueprint.route("/routes/reset", methods=['POST'])
def reset():
    Reset().execute()
    return jsonify({"msg": "Todos los datos fueron eliminados"})
