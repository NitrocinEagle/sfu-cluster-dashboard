$(document).ready(function () {
    var $operation = $('#id_operation');
    var $node_name = $('#id_node_name');
    var $node_os = $('#id_node_os');
    var $node_ip = $('#id_node_ip');
    var $plugins_list = $('#id_plugins_list');
    var $group_name = $('#id_group_name');
    var $select_node = $('#id_select_node');
    var $select_group = $('#id_select_group');
    var $select_plugin = $('#id_select_plugin');
    var $select_param = $('#id_select_param');

    var inputs = [
        'node_name', 'node_os', 'node_ip', 'plugins_list', 'group_name',
        'select_plugin', 'select_node', 'select_group', 'select_param'];

    $.each(inputs, function (key, item) {
        $('#id_' + item).parents('.form-group').hide()
    });
    $operation.val('');
    $operation.on('change', function () {
        console.log('d');
        $.each(inputs, function (key, item) {
            $('#id_' + item).parents('.form-group').hide()
        });

        var fieldName = $operation.val();
        if (fieldName == 'add_node') {
            $node_name.parents('.form-group').toggle();
            $node_os.parents('.form-group').toggle();
            $node_ip.parents('.form-group').toggle();
            $plugins_list.parents('.form-group').toggle();
        } else {
            if (fieldName == 'add_server_group') {
                $group_name.parents('.form-group').toggle();
            } else {
                if (fieldName == 'add_node_to_group' || fieldName == 'del_node_from_group') {
                    $select_node.parents('.form-group').toggle();
                    $select_group.parents('.form-group').toggle();
                    $select_node.empty()
                    $select_group.empty()

                    MONITORING_SETTINS_API.getNodesList('',
                        function (data) {
                            var nodes = data.nodes;
                            $.each(nodes, function (k, v) {
                                $select_node.append($("<option></option>").attr("value", v).text(v))
                            });
                            $select_node.val('');
                        }
                    );

                    MONITORING_SETTINS_API.getServerGroupsList('',
                        function (data) {
                            var groups = data.groups;
                            $.each(groups, function (k, v) {
                                $select_group.append($("<option></option>").attr("value", v).text(v))
                            });
                            $select_group.val('');
                        }
                    );
                } else {
                    if (fieldName == 'stop_to_monitor_node') {
                        $select_node.parents('.form-group').toggle();
                    } else {
                        if (fieldName == 'stop_to_monitor_param') {
                            $select_node.parents('.form-group').toggle();
                            $select_plugin.parents('.form-group').toggle();
                            $select_param.parents('.form-group').toggle();

                            $select_node.val('');
                            $select_node.on('change', function () {
                                $select_plugin.empty();
                                $select_param.empty();
                                MONITORING_SETTINS_API.getPluginsByNode($select_node.val(),
                                    function (data) {
                                        var plugins = data.plugins;
                                        $.each(plugins, function (k, v) {
                                            $select_plugin.append($("<option></option>").attr("value", v).text(v))
                                        });
                                        $select_plugin.val('');
                                    }
                                );
                            });
                            $select_plugin.on('change', function () {
                                $select_param.empty();
                                MONITORING_SETTINS_API.getParamsByNodePlugin($select_node.val() + '/' + $select_plugin.val(),
                                    function (data) {
                                        console.log(data);
                                        var params = data.params;
                                        $.each(params, function (k, v) {
                                            $select_param.append($("<option></option>").attr("value", v).text(v))
                                        });
                                        $select_param.val('');
                                    });
                            });

                        } else {
                            if (fieldName == 'change_param_timeout') {
                            }
                        }
                    }
                }
            }
        }
    })
    ;
})
;