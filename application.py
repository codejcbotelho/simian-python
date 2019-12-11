import settings
from flask import Flask, jsonify, make_response, request, current_app, g
from app.service.SimianService import SimianService
from app.service.StatsService import StatsService
from app.service.DynamoService import DynamoService
import os

application = Flask(__name__)


@application.before_request
def init():
    g.table = DynamoService.table(os.environ['DYNAMO_TABLE'])


@application.route('/simian', methods=['POST'])
def is_simian():
    simian_service = SimianService(request.json['dna'])

    if simian_service.is_simian():
        return make_response(jsonify({'simian': True}), 200)
    return make_response(jsonify({'simian': False}), 403)


@application.route('/stats', methods=['GET'])
def stats():
    return make_response(jsonify(StatsService.stats()))


@application.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)


if __name__ == '__main__':
    application.debug = True
    application.run()
