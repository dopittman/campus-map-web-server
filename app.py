import flask
from flask import Flask, jsonify, request

from DataParser import CourseDataParser
# from DataParser.CourseDataParser import get_student_data

app = Flask(__name__)


# we are importing our function from the colors.py file


@app.route("/", methods=['GET'])
def index():
    data = CourseDataParser.get_student_data("/Users/davidpittman/Documents/GitHub/campus-map-web-server/TestPage/TestPage.html")
    data = flask.jsonify(data)
    return data