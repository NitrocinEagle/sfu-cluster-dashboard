function getCanvases() {
    return $('.graphs');
}
function getChartsInfo() {
    var chartsInfo = [];
    $.each(getCanvases(), function (key, value) {
        var canvasID = value.getAttribute('id');
        var node_name = value.getAttribute('node-name');
        var plugin_name = value.getAttribute('plugin-name');
        var param_name = value.getAttribute('param-name');
        chartsInfo.push(
            {
                'canvas_id': canvasID,
                'node_name': node_name,
                'plugin_name': plugin_name,
                'param_name': param_name,
            }
        );
    });
    return chartsInfo;
}

function buildGraphs(chartsInfo) {
    var graphAPI_URL = '/api/graphs/';
    console.log('chartsInfo --> ', chartsInfo);
    $.each(chartsInfo, function (k, v) {
        $.ajax({
            url: graphAPI_URL + v.node_name + '/' + v.plugin_name + '/' + v.param_name + '/?format=json',
            dataType: 'json',
            success: function (data) {
                renderGraph(v.canvas_id, data);
            }
        });
    });
};


function renderGraph(canvasElementID, graphInfo) {
    if (graphInfo.graph_type == 'line_chart') {
        renderLineChart(canvasElementID, graphInfo);
    }
    else
        renderPieChart(canvasElementID, graphInfo);
}

function renderLineChart(canvasElementID, graphInfo) {
    var dataPoints = [];
    $.each(graphInfo.data, function (k, v) {
        dataPoints.push({
            // TODO. Tranform x to time string with time in HH:MM
            'x': v.timestamp,
            'y': v.value
        })
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
    console.log (graphInfo);
    var dataPoints = [];
    $.each(graphInfo.data[0].data, function (k, v) {
        //TODO graphInfo.data[0] is a fast decision. Need to query only the last one object
        dataPoints.push({
            'y': v.value,
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

window.onload = function () {
    var chartsInfo = getChartsInfo();
    buildGraphs(chartsInfo);
};


