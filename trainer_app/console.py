import pdb
from models.client import Client
from models.trainer import Trainer

import repositories.client_repository as client_repository
import repositories.trainer_repository as trainer_repository

client_repository.delete_all()
trainer_repository.delete_all()


trainer1 = Trainer("Neil", "Fraser", "clients")
trainer_repository.save(trainer1)
trainer2 = Trainer("Ally", "Hamilton", "clients")
trainer_repository.save(trainer2)



client1 = Client("Alison", "Cheasa", 35, trainer1)
client_repository.save(client1)

client2 = Client("John", "Smith", 42, trainer2)
client_repository.save(client2)

client3 = Client("Joe", "McDonald", 56, trainer2)
client_repository.save(client3)











pdb.set_trace()