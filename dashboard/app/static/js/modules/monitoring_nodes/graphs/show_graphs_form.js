$(document).ready(function () {
    var $select_graphs_node = $('#select-graphs-node'),
        $btn_graphs_node = $('#btn-graphs-node'),
        $select_graphs_plugin = $('#select-graphs-plugin'),
        $btn_graphs_plugin = $('#btn-graphs-plugin'),
        $select_graphs_param = $('#select-graphs-param'),
        $btn_graphs_param = $('#btn-graphs-param');

    MONITORING_API.getNodesList('', function (data) {
        $.each(data.data, function (i, item) {
            $select_graphs_node.append(
                $('<option>', {
                    value: item,
                    text: item
                }));
        });
    });

    MONITORING_API.getPluginList('', function (data) {
        $.each(data.data, function (i, item) {
            $select_graphs_plugin.append(
                $('<option>', {
                    value: item,
                    text: item
                }));
        });
    });

    MONITORING_API.getParamsList('', function (data) {
        $.each(data.data, function (i, item) {
            $select_graphs_param.append(
                $('<option>', {
                    value: item,
                    text: item
                }));
        });
    });


    $btn_graphs_node.on('click', function () {
        if ($select_graphs_node.val() == 'choose_node') {
            alert("Вы не выбрали узел");
            return;
        }
        window.location = '/modules/monitoring_nodes/graphs/node-graphs/' + $select_graphs_node.val() + '/';
    });

    $btn_graphs_plugin.on('click', function () {
        if ($select_graphs_plugin.val() == 'choose_plugin') {
            alert("Вы не выбрали плагин");
            return;
        }
        window.location = '/modules/monitoring_nodes/graphs/plugin-graphs/' + $select_graphs_plugin.val() + '/';
    });

    $btn_graphs_param.on('click', function () {
        if ($select_graphs_param.val() == 'choose_param') {
            alert("Вы не выбрали параметр");
            return;
        }
        window.location = '/modules/monitoring_nodes/graphs/param-graphs/' + $select_graphs_param.val() + '/';
    });



    var $select_node = $('#id_select_node');
    var $select_plugin = $('#id_select_plugin');
    var $select_param = $('#id_select_param');

    $select_node.val('');

    $select_node.on('change', function () {
        $select_plugin.empty();
        $select_param.empty();

        MONITORING_SETTINS_API.getPluginsByNode($select_node.val(),
            function (data) {
                var plugins = data.data;
                $.each(plugins, function (i, item) {
                    $select_plugin.append($('<option>', {
                    value: item,
                    text: item
                    }));
                });
                $select_plugin.val('');
            });
    });
    $select_plugin.on('change', function () {
        $select_param.empty();
        MONITORING_SETTINS_API.getParamsByNodePlugin($select_node.val() + '/' + $select_plugin.val(),
            function (data) {
                var params = data.data;
                $.each(params, function (i, item) {
                    $select_param.append($('<option>', {
                        value: item,
                        text: item
                    }));
                });
                $select_param.val('');
            });
    });
});