from bs4 import BeautifulSoup
import json
import requests


# Parse the html content


def get_student_data(url):
    studentCourses = {}

    # with open(url) as fp:
    #     soup = BeautifulSoup(fp, 'html.parser')
    page = requests.get(url)

    soup = BeautifulSoup(page.content, "html.parser")

    for index, table in enumerate(soup.find_all("table", {"class": "course-table-one"})):
        # Creates object to hold course information
        x = {
                "courseName": None,
                "courseSection": None,
        }

        # Finds the first span which contains the course name
        courseName = table.span.string
        # Finds the next span with class name "course section"
        courseSection = table.span.find_next("span", {"class": "course-section"}).string

        # assigns appropriate values to the course information object 'x'
        x["courseName"] = courseName
        x["courseSection"] = courseSection

        # Assigns the completed course information object to a location in the studentCourses Object
        studentCourses[index] = x

    for index, table in enumerate(soup.find_all("table", {"class": "course-table-two"})):
        studentCourses[index]["courseInstructor"] = table.find("span", {"class": "course-instructor"}).string
        studentCourses[index]["courseTime"] = table.find("span", {"class": "course-time"}).string
        studentCourses[index]["courseDays"] = table.find("span", {"class": "course-days"}).string
        studentCourses[index]["courseBuilding"] = table.find("span", {"class": "course-building"}).string
        studentCourses[index]["courseRoomNumber"] = table.find("span", {"class": "course-room-number"}).string
        studentCourses[index]["courseLength"] = table.find("span", {"class": "course-length"}).string

    return studentCourses

