import pdb
from models.trainer import Trainer
from models.client import Client

import repositories.trainer_repository as trainer_repository
import repositories.client_repository as client_repository

trainer_repository.delete_all()
client_repository.delete_all()


trainer1 = Trainer("Neil", "Fraser", "clients")
trainer_repository.save(trainer1)
trainer2 = Trainer("Ally", "Hamilton", "clients")
trainer_repository.save(trainer2)



client1 = Client("Alison", "Cheasa", 35)
client_repository.save(client1)

client2 = Client("John", "Smith", 42)
client_repository.save(client2)

client3 = Client("Joe", "McDonald", 56)
client_repository.save(client3)