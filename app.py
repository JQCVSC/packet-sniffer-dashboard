from flask import Flask, jsonify, render_template
from google.cloud import firestore

app = Flask(__name__)
db = firestore.Client()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/packets')
def get_packets():
    packets = db.collection('packets').order_by('timestamp', direction=firestore.Query.DESCENDING).limit(100).stream()
    return jsonify([packet.to_dict() for packet in packets])

@app.route('/packets/<source>')
def get_source_packets(source):
    if source == 'rebex':
        query = db.collection('packets').where('dst', '==', 'test.rebex.net').order_by('timestamp', direction=firestore.Query.DESCENDING).limit(50)
    elif source == 'dns':
        query = db.collection('packets').where('dport', '==', 53).order_by('timestamp', direction=firestore.Query.DESCENDING).limit(50)
    elif source == 'jsonplaceholder':
        query = db.collection('packets').where('dst', '==', 'jsonplaceholder.typicode.com').order_by('timestamp', direction=firestore.Query.DESCENDING).limit(50)
    else:
        return jsonify([])
    
    packets = query.stream()
    return jsonify([packet.to_dict() for packet in packets])

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)