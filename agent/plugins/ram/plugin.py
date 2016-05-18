import psutil

PLUGIN_NAME = "RAM_USAGE_PLUGIN"

methods_ram_usage = {
    PLUGIN_NAME + '~ram_usage': lambda: {'data': psutil.virtual_memory().used/(1024*1024)},
}