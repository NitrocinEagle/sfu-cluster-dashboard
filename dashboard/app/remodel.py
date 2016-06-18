from mongoengine import connect
connect("test_monitoring")
from mongo_models import MonitoringNodesData
from datetime import datetime
import json

import time
# mon_nod_data = MonitoringNodesData.objects()
# mon_nod_data.update(**{"unset__timestamp": 1})
# for i in mon_nod_data:
#     print i.timestamp
f = open('data.txt', 'rb+')
str = '['
# for i in mon_nod_data:
    # dt = datetime.strptime(i.timestamp.isoformat(), "%Y-%m-%dT%H:%M:%S.%f")
    # timstmp = time.mktime(dt.timetuple())
    # i.update(**{'timestamp': i.stamp})
    # print i





# print json.dumps(i.data)
#     # str += '%s, ' % datetime.strptime(i.timestamp.isoformat(), "%Y-%m-%dT%H:%M:%S.%f")
#     str += "{'node': %s, 'plugin': %s, 'param': %s, 'data': %s, 'timestamp': %s,}," % (
#     i.node, i.plugin, i.param, i.node, json.dumps(i.data), timstmp)
# # str += '%s\n' % datetime.strptime(i.timestamp.isoformat(), '%Y-%m-%dT%H:%M%S.%f')
# str += ']'
# f.write(str)
#
#
# # print time.mktime(datetime.strptime(i.timestamp.isoformat(), '%Y-%m-%dT%H:%M:%S.%f').timetuple())
#     # str += "{'node': %s, 'plugin': %s, 'param': %s, 'data': %s, 'timestamp': %s,}," % (
#     # i.node, i.plugin, i.param, i.node, i.data,