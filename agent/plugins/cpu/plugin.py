import psutil


def cpu_percent():
    return {'data': psutil.cpu_percent()}


def cpu_count():
    return psutil.cpu_count()