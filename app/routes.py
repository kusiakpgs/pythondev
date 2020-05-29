import requests

from app import app


@app.route('/redirect/users', methods=['GET'])
def users():
    return requests.get('{urlToYourApp}/db/api/users').content
