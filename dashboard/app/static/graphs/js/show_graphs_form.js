$(document).ready(function () {
    var $select_node = $('#id_select_node');
    var $select_plugin = $('#id_select_plugin');
    var $select_param = $('#id_select_param');

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
            });
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
});