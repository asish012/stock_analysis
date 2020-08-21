from pymongo import MongoClient
from utils import load_configuration


def get_mongo_client(db='informed_investing', connect=True):
    m_cfg = load_configuration('mongo')
    client = MongoClient(f"mongodb://{m_cfg['user']}:{m_cfg['password']}@{m_cfg['host']}:{m_cfg['port']}",
                         connect=connect)
    db = client[db]
    return db
