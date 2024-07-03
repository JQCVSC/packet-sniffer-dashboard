from flask import Flask, jsonify, render_template
from datetime import datetime
import random

app = Flask(__name__)

# Mock database
mock_packets = []

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/packets')
def get_packets():
    return jsonify(mock_packets)

@app.route('/packets/<source>')
def get_source_packets(source):
    return jsonify([p for p in mock_packets if p.get('source') == source])

# Mock packet generation for testing
def generate_mock_packet():
    sources = ['rebex', 'dns', 'jsonplaceholder']
    return {
        "timestamp": datetime.now().isoformat(),
        "source": random.choice(sources),
        "src": f"192.168.0.{random.randint(1, 255)}",
        "dst": f"10.0.0.{random.randint(1, 255)}",
        "proto": random.choice(['TCP', 'UDP']),
        "length": random.randint(64, 1500)
    }

# Generate some mock packets
for _ in range(50):
    mock_packets.append(generate_mock_packet())

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)