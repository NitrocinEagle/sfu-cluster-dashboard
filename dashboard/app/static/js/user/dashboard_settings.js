var $INPUTS = function () {
    return {
        select_node: $('#id_select_node'),
        select_plugin: $('#id_select_plugin'),
        select_param: $('#id_select_param'),
    }
};

var inputs = ['select_node', 'select_group', 'select_param'];


function setOptions(data, select) {
    $.each(data.data, function (k, v) {
        select.append($("<option></option>").attr("value", v).text(v))
    });
    select.val('');
}

$(document).ready(function () {
        var INPUTS = $INPUTS();
        MONITORING_SETTINS_API.getNodesList('', function (data) {
            setOptions(data, INPUTS.select_node);
        });

        INPUTS.select_node.on('change', function () {
            INPUTS.select_plugin.empty();
            INPUTS.select_param.empty();
            MONITORING_SETTINS_API.getPluginsByNode(INPUTS.select_node.val(), function (data) {
                setOptions(data, INPUTS.select_plugin);
            });
        });

        INPUTS.select_plugin.on('change', function () {
            INPUTS.select_param.empty();
            MONITORING_SETTINS_API.getParamsByNodePlugin(INPUTS.select_node.val() + '/' + INPUTS.select_plugin.val(), function (data) {
                setOptions(data, INPUTS.select_param);
            });
        });
    }
);