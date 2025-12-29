# In-memory storage (list of records)
data_store = []

def add_record(record):
    data_store.append(record)

def get_all_records():
    return data_store
