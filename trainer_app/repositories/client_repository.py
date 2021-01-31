from db.run_sql import run_sql

from models.client import Client
from models.trainer import Trainer
import repositories.trainer_repository as trainer_repository

def save(client):
    sql = "INSERT INTO clients (first_name, last_name, age, trainer_id) VALUES (%s, %s, %s, %s) RETURNING *"
    values = [client.first_name, client.last_name, client.age, client.trainer.id]
    results = run_sql(sql, values)
    id = results[0]['id']
    client.id = id
    return client


def select_all():
    clients = []

    sql = "SELECT * FROM clients"
    results = run_sql(sql)

    for row in results:
        trainer = trainer_repository.select(row['trainer_id'])
        client = Client(row['first_name'], row['last_name'], row['age'], trainer, row['id'])
        clients.append(client)
    return clients


def select(id):
    client = None
    sql = "SELECT * FROM clients WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        trainer = trainer_repository.select(result['trainer_id'])
        client = Client(result['first_name'], result['last_name'], result['age'], trainer, result['id'])
    return client


def delete_all():
    sql = "DELETE  FROM clients"
    run_sql(sql)

# def delete(id):
#     sql = "DELETE  FROM clients WHERE id = %s"
#     values = [id]
#     run_sql(sql, values)

# def clients(trainer):
#     clients = []

#     sql = "SELECT * FROM clients WHERE trainer_id = %s"
#     values = [trainer.id]
#     results = run_sql(sql, values)

#     for row in results:
#         client = Client(row['first_name'], row['last_name'], row['age'], trainer, row['id'])
#         clients.append(client)
#     return clients
