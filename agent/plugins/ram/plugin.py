import psutil

PLUGIN_NAME = "RAM"


def virtual_memory():
    vm = psutil.virtual_memory()
    data = {}
    for k in vm.__dict__:
        data[k] = vm.__dict__[k]
    return {'virtual_memory': data}

def swap_memory():
    return {'swap_memory': psutil.swap_memory()}



methods_ram_usage = {
    PLUGIN_NAME + '~virtual_memory': lambda: virtual_memory(),
    PLUGIN_NAME + '~swap_memory': lambda: swap_memory(),
}
