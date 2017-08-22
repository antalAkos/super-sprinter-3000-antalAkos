from flask import Flask, render_template, redirect, request
import uuid
import csv
import data_manager

app = Flask(__name__)


@app.route("/story", methods=["POST", "GET"])
def route_story():
    title = "Super Sprinter 3000 - Add new Story"
    do = "Create"
    if request.method == "POST":
        ID = data_manager.generate_request_id()
        story_lst = list(data_manager.request_form(ID))
        data_manager.append_csv("a", story_lst)
        return redirect("/list")
    return render_template("form.html", title=title, do=do)


@app.route("/story/edit/<story_id>", methods=["GET"])
def story_id(story_id=0):
    action = ""
    title = "Super Sprinter 3000 - Edit Story"
    do = "Update"
    table = data_manager.open_csv()
    for sublist in table:
        if sublist[0] == story_id:
            action = "/story/" + story_id
            return render_template("form.html", username=sublist[1], user_story=sublist[2], criteria=sublist[3], business_value=sublist[4], estimation=sublist[5], status=sublist[6], title=title, do=do, action=action)
    return redirect("/story/<story_id>")


@app.route("/story/<story_id>", methods=["POST"])
def update(story_id=0):
    if request.method == "POST": 
        table = data_manager.open_csv() 
        ID = story_id
        story_lst = data_manager.request_form(ID)
        for index, sublist in enumerate(table):
            if sublist[0] == ID:
                table[index] = story_lst
        data_manager.write_csv(table)
    return redirect("/")
      

@app.route("/")
@app.route("/list", methods=["GET", "POST"])
def list_route():
    table = data_manager.open_csv()
    return render_template("list.html", table=table)


@app.route("/delete/<story_id>", methods=["POST"])
def delete(story_id):
    table = data_manager.open_csv()
    for sublist in table:
        if story_id in sublist:
            table.remove(sublist)
    data_manager.write_csv(table)
    return redirect('/')
        

if __name__ == "__main__":
    app.secret_key = "mysecretkey11"  # Change the content of this string
    app.run(
        debug=True,  # Allow verbose error reports
        port=5000  # Set custom port
    )


