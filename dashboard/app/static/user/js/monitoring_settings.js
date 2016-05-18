var $INPUTS = function () {
    return {
        operation: $('#id_operation'),
        node_name: $('#id_node_name'),
        node_os: $('#id_node_os'),
        node_ip: $('#id_node_ip'),
        plugins_list: $('#id_plugins_list'),
        group_name: $('#id_group_name'),
        select_node: $('#id_select_node'),
        select_group: $('#id_select_group'),
        select_plugin: $('#id_select_plugin'),
        select_param: $('#id_select_param'),
        timeout: $('#id_timeout')
    }
};

var inputs = [
    'node_name', 'node_os', 'node_ip', 'plugins_list', 'group_name', 'select_plugin',
    'select_node', 'select_group', 'select_param', 'timeout'];

function hideAllInputs(inputs) {
    $.each(inputs, function (key, item) {
        $('#id_' + item).parents('.form-group').hide()
    });
}


var OPERATION_RELATED_INPUTS = {
    'add_node': ['node_name', 'node_os', 'node_ip', 'plugins_list'],
    'add_server_group': ['group_name'],
    'del_server_group': ['select_group'],
    'add_node_to_group': ['select_node', 'select_group'],
    'del_node_from_group': ['select_node', 'select_group'],
    'add_node_to_monitor': ['select_node'],
    'stop_to_monitor_node': ['select_node'],
    'stop_to_monitor_param': ['select_node', 'select_plugin', 'select_param'],
    'change_param_timeout': ['select_node', 'select_plugin', 'select_param', 'timeout'],
};

function inputsToggler(inputs) {
    $.each(inputs, function (key, item) {
        $('#id_' + item).parents('.form-group').toggle();
    });
}

function setOptions(data, select) {
    $.each(data.data, function (k, v) {
        select.append($("<option></option>").attr("value", v).text(v))
    });
    select.val('');
}

$(document).ready(function () {
    var INPUTS = $INPUTS();
    MONITORING_SETTINS_API.getPluginList('', function (data) {
        setOptions(data, INPUTS.select_plugin);
    });
    hideAllInputs(inputs);
    INPUTS.operation.val('');
    INPUTS.operation.on('change', function () {
        hideAllInputs(inputs)
        var operation = INPUTS.operation.val();
        inputsToggler(OPERATION_RELATED_INPUTS[operation]);

        if (operation == 'add_node') {
        }
        if (operation == 'add_server_group') {
        }
        if (operation == 'add_node_to_group' || operation == 'del_node_from_group') {
            INPUTS.select_node.empty();
            INPUTS.select_group.empty();

            MONITORING_SETTINS_API.getServerGroupsList('', function (data) {
                setOptions(data, INPUTS.select_group);
            });

            if (operation == 'del_node_from_group') {
                INPUTS.select_group.on('change', function () {
                    INPUTS.select_node.empty()
                    MONITORING_SETTINS_API.getNodesByGroup(INPUTS.select_group.val(), function (data) {
                        setOptions(data, INPUTS.select_node);
                    });
                })
            }
            if (operation == 'add_node_to_group') {
                INPUTS.select_node.empty();
                MONITORING_SETTINS_API.getNodesList('', function (data) {
                    setOptions(data, INPUTS.select_node);
                });
            }
        }
        if (operation == 'stop_to_monitor_node') {
        }
        if (operation == 'stop_to_monitor_param') {
            INPUTS.select_plugin.empty();
            INPUTS.select_param.empty();

            INPUTS.select_node.val('');
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
        if (operation == 'change_param_timeout') {
            INPUTS.select_node.empty();
            INPUTS.select_plugin.empty();
            INPUTS.select_param.empty();
            INPUTS.select_node.val('');
            MONITORING_SETTINS_API.getNodesList('', function (data) {
                setOptions(data, INPUTS.select_node);
            });

            INPUTS.select_node.on('change', function () {
                MONITORING_SETTINS_API.getPluginsByNode(INPUTS.select_node.val(), function (data) {
                    setOptions(data, INPUTS.select_plugin);
                });
            });

            INPUTS.select_plugin.on('change', function () {
                MONITORING_SETTINS_API.getParamsByNodePlugin(INPUTS.select_node.val() + '/' + INPUTS.select_plugin.val(), function (data) {
                    setOptions(data, INPUTS.select_param);
                });
            });

            INPUTS.select_param.on('change', function () {
                INPUTS.timeout.empty();
                MONITORING_SETTINS_API.getParamTimeout(INPUTS.select_node.val() + '/' + INPUTS.select_plugin.val() + '/' + INPUTS.select_param.val(), function (data) {
                    INPUTS.timeout.val(data.data)
                })
            });
        }
        if (operation == 'del_server_group') {
            MONITORING_SETTINS_API.getServerGroupsList('', function (data) {
                setOptions(data, INPUTS.select_group);
            });
        }
        if (operation == 'add_node_to_monitor') {
            INPUTS.select_node.empty();
            MONITORING_SETTINS_API.getNodesList('', function (data) {
                setOptions(data, INPUTS.select_node);
            });
        }
    });
});