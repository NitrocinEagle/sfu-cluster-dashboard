import psutil

PLUGIN_NAME = "CPU_LOAD_PLUGIN"

methods_cpu_load = {
    PLUGIN_NAME + '~cpu_load': lambda: {'data': psutil.cpu_percent()},
    PLUGIN_NAME + '~cpu_count': lambda: psutil.cpu_count(),
}
