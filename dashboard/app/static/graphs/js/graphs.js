function getCanvases() {
    return $('.graphs');
}
function getChartsInfo() {
    var chartsInfo = [];
    $.each(getCanvases(), function (key, value) {
        //id = value.getAttribute('id');
        var node_name = value.getAttribute('node-name');
        var plugin_name = value.getAttribute('plugin-name');
        var param_name = value.getAttribute('param-name');
        chartsInfo.push(
            {
                'node_name': node_name,
                'plugin_name': plugin_name,
                'param_name': param_name,
            }
        );
    });
    return chartsInfo;
}

function getGraphsInfo(chartsInfo) {
    var graphsInfo = [];
    var graphAPI_URL = ''
    $.each(chartsInfo, function (k, v) {
        var graphsInfoResponse = JSON.parse($.get(graphAPI_URL + v.node_name + '/' + v.plugin_name +  '/' + v.param_name + '/'));
        graphsInfo.push(
            {
                'dataset': graphsInfoResponse.dataset,
                'description': graphsInfoResponse.param_description
            }
        )
    });
    return graphsInfo;
}

function renderGraph(canvasElements, graphsInfo) {

}

$(function () {
    var chartsInfo = getChartsInfo();
    renderGraph(getCanvases(), getGraphsInfo(chartsInfo));
});