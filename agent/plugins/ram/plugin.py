import psutil

def ram_usage():
    return {'data': psutil.virtual_memory().used/(1024*1024)}