from db.run_sql import run_sql

from models.client import Client
from models.trainer import Trainer
import repositories.trainer_repository as trainer_repository

def save(client):
    sql = "INSERT INTO clients (first_name, last_name, age) VALUES (%s, %s, %s) RETURNING *"
    values = [client.first_name, client.last_name, client.age]
    results = run_sql(sql, values)
    id = results[0]['id']
    client.id = id
    return client