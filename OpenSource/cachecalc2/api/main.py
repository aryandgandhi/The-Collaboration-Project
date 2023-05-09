from flask import Flask, render_template, request, jsonify
import math
from math import floor
import pandas as pd  # Import pandas library

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('miscellaneous.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    data = request.get_json()
    sets = int(data['sets'])
    byte_blocks = int(data['byte_blocks'])
    hex_string = data['hex_string'].split(',')

    results = []

    for i in hex_string:
        an_integer = int(i.strip(), 16)

        offset = floor(an_integer % byte_blocks)
        index = (floor(an_integer / byte_blocks) % sets)
        tag = floor(floor(an_integer / byte_blocks) / sets)

        results.append({'offset': offset, 'index': index, 'tag': hex(tag)})

    # Create a pandas DataFrame from the results list

    # Return the string representation of the DataFrame
    return jsonify(results)