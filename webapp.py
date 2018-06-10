# The flask application developed to perform face comparison between two human faces
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
import sys
import os
import logging
from datetime import datetime
import numpy as np
from flask import Flask, request, render_template, jsonify
from scipy import misc
from werkzeug import secure_filename

import json
import requests


import csv
csv_file = csv.reader(open('/home/sudheer/Downloads/test/Top_50_Products_ZipWise.csv', "rb"), delimiter=",")

flask_file_path = os.path.normpath(os.path.dirname(__file__)+'/../test/')
print(flask_file_path)
UPLOAD_FOLDER =   flask_file_path +  '/static/uploads'
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif', 'JPG', 'JPEG', 'GIF', 'PNG'])

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def index():
    return render_template("index_treemap_final.html")


@app.route("/map", methods=['GET', 'POST'])
def map_page():
    return render_template("map_hover.html")

@app.route("/response",methods=['POST'])
def process_data():
    print(str(request.form["zip"]),"test")
    my_response=[]
    csv_file = csv.reader(open('/home/sudheer/Downloads/test/Top_50_Products_ZipWise.csv', "rb"), delimiter=",")
    for row in csv_file:
        #print(row)
	print(request.form["zip"],row[0].strip())
    #if current rows 2nd value is equal to input, print that row
    	if request.form["zip"]== row[0].strip():
		print(row[1])
        	my_response=row
		break
    else:
        my_response=["Invalid Zip Code","NA","NA"]
    return render_template("response.html",my_response =my_response)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080, debug=True)
