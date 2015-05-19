from flask import Blueprint, request, jsonify, abort, current_app

from ..auth import requires_auth
from ..zw import zsend


mod = Blueprint('ctl', __name__, url_prefix='/ctl')


@mod.route('/raw', methods=['POST'])
@requires_auth
def raw():
    data = request.get_json()
    if data is None:
        abort(400, "invalid json")
    return jsonify(success=True, request=data), 200


@mod.route('/<int:node>/on')
@requires_auth
def node_on(node):
    return set_node(node, True)


@mod.route('/<int:node>/off')
@requires_auth
def node_off(node):
    return set_node(node, False)


def set_node(node, state):
    payload = {'node': node, 'state': state}
    try:
        reply = zsend(current_app.config.get("ZHOST","localhost:1234"), payload)
        status = 200
    except Exception as e:
        reply = {'exception': e.__class__.__name__ + ": " + str(e)}
        status = 502
    return jsonify(success=True, payload=payload, reply=reply), status
