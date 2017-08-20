from flask import Flask, render_template, redirect, request, session, url_for
import uuid
import csv

app = Flask(__name__)
'''
@app.route('/')
def route_index():
    return render_template('list.html')

@app.route('/story')
def route_edit():
    note_text = Noneo
    if 'note'in session:
        note_text = session['note']
    return render_template('form.html', note=note_text)
'''
@app.route('/story', methods=['POST', 'GET'])
def route_story():
    title = "Super Sprinter 3000 - Add new Story"
    do = "Create"
    if request.method == 'POST':
       
        username = request.form['username']
        user_story = request.form['user_story']
        criteria = request.form['criteria']
        business_value = request.form['business_value']
        estimation = request.form['estimation']
        status = request.form['status']
        fieldnames = ['ID', 'username', 'user_story', "criteria", 
                      "business_value", "estimation", "status"]
        
        with open('story.csv', 'a') as file:
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writerow({'ID': ID, 'username': username, 'user_story': user_story,
                             'criteria': criteria, 'business_value': business_value, 
                             'estimation': estimation, 'status': status
                             })
        return redirect('/list')
    elif request.method == 'GET':
        redirect('/list')
    return render_template('form.html', title=title, do=do)


@app.route('/story/<story_id>')
def story_id(story_id=0):
    title = "Super Sprinter 3000 - Edit Story"
    do = "Update"
    table = open_csv()
    for sublist in table:
        if sublist[0] == story_id:
            return render_template('form.html', username=sublist[1], 
                                   user_story=sublist[2], criteria=sublist[3], 
                                   business_value=sublist[4], estimation=sublist[5],
                                   status=sublist[6], title=title, do=do
                                   )


@app.route('/')
@app.route('/list', methods=['GET', 'POST'])
def list_route():
    table = open_csv()
    if request.method == 'POST':
        for index, sublist in enumerate(table):
            if table[index][0] == sublist[0]:
                table = table.remove(sublist)
        write_csv(table)
    return render_template('list.html', table=table)


def generate_request_id():
    new_id = uuid.uuid4()
    return str(new_id)


def open_csv():
    with open("story.csv", "r") as file:
        lines = file.readlines()
        table = [element.replace("\n", "").split(",") for element in lines]
        return table


def write_csv(table):
    with open("story.csv", "w") as file:
        for record in table:
            row = ','.join(record)
            file.write(row + "\n")

 



if __name__ == "__main__":
    app.secret_key = 'mysecretkey11'  # Change the content of this string
    app.run(
        debug=True,  # Allow verbose error reports
        port=5000  # Set custom port
    )


