DATETIME_FORMAT = 'YYYY-MM-DD hh:mm:ss';

function toUnix(dateString) {
    if (dateString)
        return moment(dateString, DATETIME_FORMAT).unix();
    return null;
}

function setDefaultTimes(graph) {
    //var offset = 7;
    //var timeTo_stamp = new Date(new Date().getTime() + offset * 3600 * 1000).getTime() / 1000;
    //var timeFrom_stamp = new Date(new Date().getTime() + offset * 3600 * 1000).getTime() / 1000 - 7200;
    $(graph).find('.graph-actions-from input').val(moment().subtract(3600, 's').format(DATETIME_FORMAT));
    $(graph).find('.graph-actions-to input').val(moment().format(DATETIME_FORMAT));
}

$(document).ready(function () {
    moment.locale('ru');
    $.datetimepicker.setLocale('ru');
    $('.date-time-input').datetimepicker({
        format: 'Y-m-d H:i:s',
        lang: 'ru',
        maxDate: '+1970/01/01'
    });

    $.each(getGraphBlocks(), function (k, graph) {
        setDefaultTimes(graph);
    });

    $('.btn-graph-refresh').on('click', function (e) {
        var graph = $(e.currentTarget).parents('.graph');
        var graph_type = $(graph).find('.graph-actions-type select').val();
        var selected_time = $(graph).find('.graph-actions-select-time select').val();
        var time_from = toUnix($(graph).find('.graph-actions-from input').val());
        var time_to = toUnix($(graph).find('.graph-actions-to input').val());
        var node_name = $(graph).attr('node-name');
        var plugin_name = $(graph).attr('plugin-name');
        var param_name = $(graph).attr('param-name');

        var options = {
            node_name: node_name,
            plugin_name: plugin_name,
            param_name: param_name,
            time_from: time_from,
            time_to: time_to,
            selected_time: selected_time,
            selected_graph_type: graph_type
        };

        console.log("options: ", options);
        $.ajax({
            url: '/api/modules/monitoring-nodes/get-monitoring-data/',
            dataType: 'json',
            data: options,
            success: function (data) {
                console.log("data: ", data);
                renderGraph(graph, graph_type, data);
            }
        });
    });

    var chartsInfo = getChartsInfo();
    buildGraphs(chartsInfo);
});

function getGraphBlocks() {
    return $('.graph');
}
function getChartsInfo() {
    var chartsInfo = [];
    $.each(getGraphBlocks(), function (key, value) {
        var node_name = $(value).attr('node-name');
        var plugin_name = $(value).attr('plugin-name');
        var param_name = $(value).attr('param-name');
        var time_from = toUnix($(value).find('.graph-actions-from input').val());
        var time_to = toUnix($(value).find('.graph-actions-to input').val());
        var selected_time = $(value).find('.graph-actions-select-time input').val();
        var selected_graph_type = $(value).find('.graph-actions-select-time input').val();
        chartsInfo.push({
            'graph': value,
            'node_name': node_name,
            'plugin_name': plugin_name,
            'param_name': param_name,
            'time_from': time_from,
            'time_to': time_to,
            'selected_time': selected_time,
            'selected_graph_type': $(value).find('.graph-actions-type select').val(),
        });
    });
    return chartsInfo;
}

function buildGraphs(chartsInfo) {
    $.each(chartsInfo, function (k, v) {
        var options = {
            node_name: v.node_name,
            plugin_name: v.plugin_name,
            param_name: v.param_name,
            time_from: v.time_from,
            time_to: v.time_to,
            selected_time: v.selected_time,
            selected_graph_type: v.selected_graph_type
        };
        $.ajax({
            url: '/api/modules/monitoring-nodes/get-monitoring-data/',
            dataType: 'json',
            data: options,
            success: function (data) {
                renderGraph(v.graph, v.selected_graph_type, data);
            }
        });
    });
};


function renderGraph(graphElement, type, graphInfo) {
    var canvas = $(graphElement).find('.graphs').attr('id')
    if (type == 'line_chart')
        renderLineChart(canvas, graphInfo);
    if (type == 'pie_chart')
        renderPieChart(canvas, graphInfo);
    return;
}

function renderLineChart(canvasElementID, graphInfo) {
    var dataPoints = [];
    $.each(graphInfo.data, function (k, v) {
        dataPoints.push({
            'label': moment.unix(v.timestamp).format("hh:mm"),
            'y': (v.value.percent ? v.value.percent: v.value)
        });
    });
    var chart = new CanvasJS.Chart(canvasElementID, {
        zoomEnabled: true,
        title: {
            text: graphInfo.graph_name
        },
        axisX: {
            title: graphInfo.axis_x,
            gridThickness: 2
        },
        axisY: {
            title: graphInfo.axis_y
        },
        data: [
            {
                type: "area",
                dataPoints: dataPoints
            }
        ]
    });
    chart.render();
}

function renderPieChart(canvasElementID, graphInfo) {
    var dataPoints = [];
    $.each(graphInfo.data, function (k, v) {
        dataPoints.push({
            'y': parseInt(v.value/1024/1024),
            'indexLabel': v.sector_name
        })
    });
    var chart = new CanvasJS.Chart(canvasElementID, {
        title: {
            text: graphInfo.graph_name
        },
        data: [{
            type: "doughnut",
            dataPoints: dataPoints
        }]
    });

    chart.render();
}