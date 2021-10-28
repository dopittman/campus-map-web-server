import flask
from flask import Flask, jsonify, request

from DataParser import CourseDataParser
# from DataParser.CourseDataParser import get_student_data

app = Flask(__name__)

test_url = "http://campusmapuncp.s3-website-us-east-1.amazonaws.com/"


@app.route("/", methods=['GET'])
def index():
    data = CourseDataParser.get_student_data("http://campusmapuncp.s3-website-us-east-1.amazonaws.com/")
    data = flask.jsonify(data)
    return data
