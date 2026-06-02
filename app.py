import os
import json
import base64
from flask import Flask, request, jsonify
from flask_cors import CORS
import firebase_admin
from firebase_admin import credentials, firestore
from questions import QUESTIONS

app = Flask(__name__)
CORS(app)

# Firebase Admin – use environment variable on Render
firebase_creds_base64 = os.environ.get('FIREBASE_CREDENTIALS')
if firebase_creds_base64:
    cred_json = base64.b64decode(firebase_creds_base64).decode('utf-8')
    cred_dict = json.loads(cred_json)
    cred = credentials.Certificate(cred_dict)
else:
    # local development
    if os.path.exists("serviceAccountKey.json"):
        cred = credentials.Certificate("serviceAccountKey.json")
    else:
        raise Exception("Firebase credentials not found.")
firebase_admin.initialize_app(cred)
db = firestore.client()

@app.route('/api/questions', methods=['GET'])
def get_questions():
    safe = [{'id': q['id'], 'text': q['text'], 'options': q['options']} for q in QUESTIONS]
    return jsonify(safe)

@app.route('/api/correct-answers', methods=['GET'])
def correct_answers():
    answers = {str(q['id']): q['answer'] for q in QUESTIONS}
    return jsonify(answers)

@app.route('/api/explanations', methods=['GET'])
def explanations():
    expl = {str(q['id']): q['explanation'] for q in QUESTIONS}
    return jsonify(expl)

@app.route('/api/submit', methods=['POST'])
def submit_score():
    data = request.json
    uid = data.get('uid')
    name = data.get('name')
    score = data.get('score')
    total = data.get('total')
    if not uid or score is None:
        return jsonify({'error': 'Missing data'}), 400
    db.collection('results').document(uid).set({
        'name': name,
        'score': score,
        'total': total,
        'timestamp': firestore.SERVER_TIMESTAMP
    })
    return jsonify({'message': 'Score saved'}), 200

@app.route('/api/leaderboard', methods=['GET'])
def leaderboard():
    results = db.collection('results').order_by('score', direction=firestore.Query.DESCENDING).limit(20).stream()
    board = [{'name': doc.to_dict().get('name'), 'score': doc.to_dict().get('score'), 'total': doc.to_dict().get('total')} for doc in results]
    return jsonify(board)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
