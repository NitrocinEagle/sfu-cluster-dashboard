from plugins.cpu.plugin import cpu_percent
from plugins.ram.plugin import ram_usage
from plugins.hdd.plugin import hdd_usage

PORT = 3001

methods = {
    "cpu_load": cpu_percent,
    "ram_usage": ram_usage,
    "hdd_usage": hdd_usage
}