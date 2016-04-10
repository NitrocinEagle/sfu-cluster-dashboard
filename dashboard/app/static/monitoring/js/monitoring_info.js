$(document).ready(function () {
    $.ajax({
        url: '/api/monitoring/info/',
        dataType: 'json',
        success: function (data) {
            data = data.data;
            var nodes = [data[0].node];
            data.forEach(function (val) {
                if (nodes.indexOf(val.node) == -1) {
                    nodes.push(val.node);
                }
            });
            var monitoringInfo = [];
            nodes.forEach(function (node) {
                monitoringInfo.push({
                    header: node,
                    ip: '',
                    open: false,
                    data: []
                });
            })

            data.forEach(function (info) {
                monitoringInfo.forEach(function (node) {
                    if (node.header == info.node) {
                        node.ip = info.ip;
                        node.data.push({
                            header: info.plugin,
                            open: !true,
                            data: []
                        });
                    }
                })
            });

            data.forEach(function (info) {
                monitoringInfo.forEach(function (node) {
                    if (node.header == info.node) {
                        node.data.forEach(function (plugin) {
                            if (plugin.header == info.plugin) {
                                plugin.data.push({
                                    header: info.param,
                                    graph: '<a href="/graphs/show/' + info.node + '/' + info.plugin + '/' + info.param + '"><i class="fa fa-2x fa-bar-chart"></i></a>',
                                    timeout: info.timeout + ' сек.'
                                });
                            }
                        })
                    }
                })
            })

            webix.ui({
                view: "treetable",
                container: "treetable",
                columns: [
                    {id: "header", header: "", template: "{common.treetable()} #header#", width: 400},
                    {id: "ip", header: "IP-адрес", width: 110},
                    {id: "timeout", header: "Таймаут", width: 100},
                    {id: "graph", header: "График", width: 80}
                ],
                scroll: false,
                data: [{header: 'Узлы', open: true, data: monitoringInfo}]
            });
        }
    });
});