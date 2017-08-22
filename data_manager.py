from flask import Flask, render_template, redirect, request
import uuid
import csv


def generate_request_id():
    new_id = uuid.uuid4()
    return str(new_id)


def open_csv():
    lst = []
    with open("story.csv", "r") as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            lst.append(row)
    return lst


def append_csv(mode, lst):
    with open("story.csv", mode) as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(lst)


def write_csv(table):
    with open('story.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerows(table)  


def request_form(ID):
    story_lst = []                             
    story_lst.append(ID)
    story_lst.append(request.form["username"])
    story_lst.append(request.form["user_story"])
    story_lst.append(request.form["criteria"])
    story_lst.append(request.form["business_value"])
    story_lst.append(request.form["estimation"])
    story_lst.append(request.form["status"])
    return story_lst
