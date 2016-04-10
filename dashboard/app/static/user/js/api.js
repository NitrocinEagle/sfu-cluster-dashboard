function createGetter(url) {
    return function(path_args, callback) {
        $.ajax({
            url: '/api/configs/' + url + path_args,
            dataType: 'json',
//            data: options,
            success: callback
        });
    };
};

// MONITORING_SETTINS_API.getNodesList(path_args, function(data) { alert(2); });
MONITORING_SETTINS_API = {
    getServerGroupsList: createGetter('get_server_groups/'),
    getNodesList: createGetter('get_nodes/'),
    getPluginList: createGetter('get_plugins/'),
    getPluginsByNode: createGetter('get_node_plugins/'),
    getParamsByNodePlugin: createGetter('get_params_by_node_plugin/'),
};
