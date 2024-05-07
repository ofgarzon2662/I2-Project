from flask import Flask, jsonify, request, Blueprint
from ..commands.createOffer import createOffer
from ..commands.viewFilterOffers import viewFilterOffers
from ..commands.viewOffer import viewOffer
from ..commands.deleteOffer import deleteOffer
import os
from ..commands.reset import Reset

operations_blueprint = Blueprint('operations', __name__)

@operations_blueprint.route('/offers', methods = ['POST'])
def create():
    json = request.get_json()
    result = createOffer(json.get('postId', None), json.get('description', None), json.get('size', None), json.get('fragile', None), 
                         json.get('offer', None), request.headers.get('Authorization', None)).execute()
    return jsonify({ 'id': result['id'], 'userId':result['userId'], 'createdAt':result['createdAt'] }), 201

@operations_blueprint.route('/offers', methods = ['GET'])
def viewFilter():
    if request.args.get('post') is None:
        postId = None
    else:
        postId = request.args.get('post')
    if request.args.get('owner') is None:
        owner = None
    else:
        owner = request.args.get('owner')
    result = viewFilterOffers(postId, owner, request.headers.get('Authorization', None)).execute()
    
    # Return the list of offers as JSON
    return jsonify(result) 

@operations_blueprint.route('/offers/<string:id>', methods = ['GET'])
def view(id):
    result = viewOffer(id, request.headers.get('Authorization', None)).execute()
    return jsonify(result)

@operations_blueprint.route('/offers/<string:id>', methods = ['DELETE'])
def delete(id):
    result = deleteOffer(id, request.headers.get('Authorization', None)).execute()
    return jsonify({ 'msg': result['msg'] })

@operations_blueprint.route("/offers/ping", methods=['GET'])
def healthcheck():
    return jsonify('pong'), 200

@operations_blueprint.route("/offers/reset", methods=['POST'])
def reset():
    Reset().execute()
    return jsonify({"msg": "Todos los datos fueron eliminados"})
