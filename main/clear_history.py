import pickle
from llm import picklepath

with open(picklepath, 'wb+') as f:
    pickle.dump([], f)
