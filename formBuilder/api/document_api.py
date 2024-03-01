# Blueprint for document-related API routes
from flask import Blueprint

document_blueprint = Blueprint('document', __name__)


@document_blueprint.route('/', methods=['GET'])
def get_documents():
    return "List of documents"
