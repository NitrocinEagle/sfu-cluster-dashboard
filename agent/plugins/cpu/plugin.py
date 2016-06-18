import psutil

PLUGIN_NAME = "CPU"


def cpu_percent():
    return {'cpu_percent': psutil.cpu_percent()}

def cpu_count():
    return {'cpu_count': psutil.cpu_count()}

def cpu_stats():
    return {'cpu_stats': psutil.cpu_stats()}

methods_cpu_load = {
    PLUGIN_NAME + '~cpu_percent': lambda: cpu_percent(),
    PLUGIN_NAME + '~cpu_count': lambda: cpu_count(),
    PLUGIN_NAME + '~cpu_stats': lambda: cpu_stats(),
}
