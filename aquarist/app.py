from flask import Flask, render_template, request, redirect, url_for
import os
import pymongo
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

MONGO_URI = os.environ.get('MONGO_URI')
DB_NAME = 'aquarist_resource_fish'

client = pymongo.MongoClient(MONGO_URI)
db = client[DB_NAME]

@app.route('/fish/create')
def show_create_fish():
    return render_template('create_fish.template.html')


# "magic code" -- boilerplate
if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)