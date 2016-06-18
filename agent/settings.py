from plugins.cpu.plugin import methods_cpu_load
from plugins.ram.plugin import methods_ram_usage
from plugins.hdd.plugin import methods_hdd_usage

PORT = 3002
methods = {}
for k, v in methods_hdd_usage.iteritems():
    methods[k] = v

for k, v in methods_cpu_load.iteritems():
    methods[k] = v

for k, v in methods_ram_usage.iteritems():
    methods[k] = v
