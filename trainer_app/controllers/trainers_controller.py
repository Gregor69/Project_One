from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.client import Client
from models.trainer import Trainer
import repositories.client_repository as client_repository
import repositories.trainer_repository as trainer_repository

trainers_blueprint = Blueprint("trainers", __name__)

@trainers_blueprint.route("/trainers")
def trainers():
    trainers = trainer_repository.select_all()
    return render_template("trainers/index.html", all_trainers = trainers)

@trainers_blueprint.route("/trainers/new", methods=['GET'])
def new_trainer():
    clients = client_repository.select_all()
    return render_template("trainers/new.html", all_clients = clients)

@trainers_blueprint.route("/trainers",  methods=['POST'])
def create_trainer():
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    
    trainer = Trainer(first_name, last_name)
    trainer_repository.save(trainer)
    return redirect('/trainers')

@trainers_blueprint.route("/trainers/<id>", methods=['GET'])
def show_trainer(id):
    trainer = trainer_repository.select(id)
    return render_template('trainers/show.html', trainer = trainer)

@trainers_blueprint.route("/trainers/<id>/edit", methods=['GET'])
def edit_trainer(id):
    trainer= trainer_repository.select(id)
    clients = client_repository.select_all()
    return render_template('/trainers/edit.html', trainer = trainer, all_clients = clients)

@trainers_blueprint.route("/trainers/<id>",  methods=['POST'])
def update_trainer(id):
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    trainer = Trainer(first_name, last_name, id)
    print(trainer)
    trainer_repository.update(trainer)
    return redirect('/trainers')

@trainers_blueprint.route("/trainers/<id>/delete", methods=["POST"])
def delete_trainer(id):
    trainer_repository.delete(id)
    return redirect('/trainers')