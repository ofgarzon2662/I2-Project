from flask import Blueprint, jsonify, request

from ..commands.create import Create
from ..commands.get_by_offer_id import GetByOfferID
from ..commands.reset import Reset
from ..commands.delete import Delete

controller_blueprint = Blueprint('controller', __name__)


@controller_blueprint.route('/scores', methods=['POST'])
def create_score():
    request_json = request.get_json()
    result = Create(request_json.get('idOffer', None),
                    request_json.get('idPost', None),
                    request_json.get('idUserPosting', None),
                    request_json.get('idUserOffering', None),
                    request_json.get('ocupancy', None),
                    request_json.get('bagCost', None),
                    request_json.get('offer', None)).execute()
    return jsonify({
        'id': result['id'],
        'score': result['score'],
        'idUserOffering': result['idUserOffering'],
        'idOffer': result['idOffer'],
        'idPost': result['idPost'],
        'idUserPosting': result['idUserPosting'],
        'ocupancy': result['ocupancy'],
        'bagCost': result['bagCost'],
        'offer': result['offer']
    }), 201


@controller_blueprint.route('/scores/offers/<string:id>', methods=['GET'])
def get_scores_by_offer_id(id):
    result = GetByOfferID(id).execute()
    return {
        'id': result['id'],
        'score': result['score'],
        'idUserOffering': result['idUserOffering'],
        'idOffer': result['idOffer'],
        'idPost': result['idPost'],
        'idUserPosting': result['idUserPosting'],
        'ocupancy': result['ocupancy'],
        'bagCost': result['bagCost'],
        'offer': result['offer']
    }


@controller_blueprint.route('/scores/<string:id>', methods=['DELETE'])
def delete_score(id):
    Delete(id).execute()
    return {"msg": "Score eliminado"}


@controller_blueprint.route("/scores/ping", methods=['GET'])
def healthcheck():
    return jsonify('pong'), 200


@controller_blueprint.route("/scores/reset", methods=['POST'])
def reset():
    Reset().execute()
    return jsonify({"msg": "Todos los datos fueron eliminados"})
