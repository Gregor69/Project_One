from db.run_sql import run_sql

from models.trainer import Trainer
from models.client import Client


def save(trainer):
    sql = "INSERT INTO trainers (first_name, last_name) VALUES (%s, %s) RETURNING *"
    values = [trainer.first_name, trainer.last_name,]
    results = run_sql(sql, values)
    id = results[0]['id']
    trainer.id = id
    return trainer

def select_all():
    trainers = []

    sql = "SELECT * FROM trainers"
    results = run_sql(sql)

    for row in results:
        trainer = Trainer(row['first_name'], row['last_name'], row['id'])
        trainers.append(trainer)
    return trainers

def select(id):
    trainer = None
    sql = "SELECT * FROM trainers WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        trainer = Trainer(result['first_name'], result['last_name'], result['id'])
    return trainer

def delete_all():
    sql = "DELETE  FROM trainers"
    run_sql(sql)


def delete(id):
    sql = "DELETE  FROM trainers WHERE id = %s"
    values = [id]
    run_sql(sql, values)

def clients(trainer):
    clients = []

    sql = "SELECT * FROM clients WHERE trainer_id = %s"
    values = [trainer.id]
    results = run_sql(sql, values)

    for row in results:
        client = Client(row['first_name'], row['last_name'], row['age'], trainer, row['id'])
        clients.append(client)
    return clients

def update(trainer):
    sql = "UPDATE trainer (first_name, last_name VALUES (%s, %s) RETURNING *"
    values = [trainer.first_name, trainer.last_name]
    print(values)
    run_sql(sql, values)
