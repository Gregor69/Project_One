from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.client import Client
import repositories.client_repository as client_repository
import repositories.trainer_repository as trainer_repository

clients_blueprint = Blueprint("clients", __name__)



@clients_blueprint.route("/clients")
def clients():
    clients = client_repository.select_all()
    return render_template("clients/index.html", all_clients = clients)

@clients_blueprint.route("/clients/new", methods=['GET'])
def new_client():
    trainers = trainer_repository.select_all()
    return render_template("clients/new.html", all_trainers = trainers)

@clients_blueprint.route("/clients",  methods=['POST'])
def create_client():
    first_name = request.form['first_name']
    second_name = request.form['last_name']
    age = request.form['age']
    trainer = trainer_repository.select(request.form['trainer_id'])
    client = Client(first_name, last_name, age, trainer)
    client_repository.save(client)
    return redirect('/clients')