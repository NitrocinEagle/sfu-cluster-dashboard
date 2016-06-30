import psutil

PLUGIN_NAME = "HDD"


def disk_usage():
    du = psutil.disk_usage('/')
    data = {}
    for k in du.__dict__:
        data[k] = du.__dict__[k]
    return {'disk_usage': data}


def disk_partitions():
    return {'disk_partitions': psutil.disk_partitions()}

methods_hdd_usage = {
    PLUGIN_NAME + '~disk_usage': lambda: disk_usage(),
    PLUGIN_NAME + '~disk_partitions': lambda: disk_partitions(),
}
