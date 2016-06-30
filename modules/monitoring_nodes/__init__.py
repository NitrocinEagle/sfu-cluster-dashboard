from server.module import start_monitoring_nodes
from server.init_db import init_db


def start():
    init_db()
    start_monitoring_nodes()
