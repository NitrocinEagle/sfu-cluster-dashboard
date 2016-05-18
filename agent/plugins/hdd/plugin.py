import psutil

PLUGIN_NAME = "HDD_USAGE_PLUGIN"

methods_hdd_usage = {
    PLUGIN_NAME + '~hdd_usage': lambda: {'data': psutil.disk_usage('/').used/(1024*1024)},
}