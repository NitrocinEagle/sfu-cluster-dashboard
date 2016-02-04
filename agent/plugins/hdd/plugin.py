import psutil


def hdd_usage():
    return {'data': psutil.disk_usage('/').used/(1024*1024)}