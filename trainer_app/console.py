import pdb
from models.trainer import Trainer
from models.client import Client

import repositories.trainer_repository as trainer_repository
import repositories.client_repository as client_repository


trainer1 = Trainer("Neil", "Fraser", "clients")
trainer_repository.save(trainer1)

client1 = Client("Alison", "Cheasa", 35)
client_repository.save(client1)