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