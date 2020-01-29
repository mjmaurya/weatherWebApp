from flask import Flask, render_template
import re
app=Flask(__name__)
@app.route("/")
def index(request):
    return render_template("index.html")