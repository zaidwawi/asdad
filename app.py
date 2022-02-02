#!/usr/bin/python
# -*- coding: utf-8 -*-
import os
from flask import (
    Flask,
    request,
    abort,
    jsonify,
    render_template, 
    redirect,
    url_for
    )
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from models import setup_db, data, db
def create_app(test_config=None):

    # create and configure the app

    app = Flask(__name__)
    setup_db(app)
    CORS(app)

    @app.route('/')
    def home():
        datas = data.query.all()

        return render_template('index.html', daat = datas)

    @app.route('/', methods = ['POST'])
    def home():
        name = request.form.get('name')
        ney_data = data(
            name = name
        )
        db.session.add(ney_data)
        db.session.commit()
        
        return redirect(url_for('home'))
    
    

    return app


APP = create_app()

if __name__ == '__main__':
    APP.run()
