function createOldGetter(url) {
    return function(path_args, callback) {
        $.ajax({
            url: '/api/configs/' + url + path_args,
            dataType: 'json',
//            data: options,
            success: callback
        });
    };
};

function createGetter(url) {
    return function(path_args, callback) {
        $.ajax({
            url: '/api/modules/' + url + path_args,
            dataType: 'json',
//            data: options,
            success: callback
        });
    };
};

MONITORING_SETTINS_API = {
    getServerGroupsList: createOldGetter('get_server_groups/'),
    getNodesList: createOldGetter('get_nodes/'),
    getPluginList: createOldGetter('get_plugins/'),

    getParamsList: createGetter('monitoring-nodes/get-params/'),

    getPluginsByNode: createOldGetter('get_node_plugins/'),
    getParamsByNodePlugin: createOldGetter('get_params_by_node_plugin/'),
    getNodesByGroup: createOldGetter('get_nodes_by_group/'),
    getParamTimeout: createOldGetter('get_param_timeout/'),
};


MONITORING_API = {
    getNodesList: createGetter('monitoring-nodes/get-nodes-list/'),
    getPluginList: createGetter('monitoring-nodes/get-plugins-list/'),
    getParamsList: createGetter('monitoring-nodes/get-params-list/'),
};
