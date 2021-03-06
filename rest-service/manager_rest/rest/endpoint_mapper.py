#########
# Copyright (c) 2015 GigaSpaces Technologies Ltd. All rights reserved
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
#  * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  * See the License for the specific language governing permissions and
#  * limitations under the License.

from . import (swagger, resources_v1, resources_v2,
               resources_v2_1, resources_v3, resources_v3_1)

SUPPORTED_API_VERSIONS = [('v1', resources_v1),
                          ('v2', resources_v2),
                          ('v2.1', resources_v2_1),
                          ('v3', resources_v3),
                          ('v3.1', resources_v3_1)]


def setup_resources(api):
    resources_endpoints = {
        'Blueprints': 'blueprints',
        'BlueprintsId': 'blueprints/<string:blueprint_id>',
        'BlueprintsIdValidate': 'blueprints/<string:blueprint_id>/validate',
        'BlueprintsIdArchive': 'blueprints/<string:blueprint_id>/archive',
        'BlueprintsSetGlobal': 'blueprints/<string:blueprint_id>/set-global',
        'BlueprintsSetVisibility': 'blueprints/<string:blueprint_id>/'
                                   'set-visibility',
        'Snapshots': 'snapshots',
        'SnapshotsId': 'snapshots/<string:snapshot_id>',
        'SnapshotsIdArchive': 'snapshots/<string:snapshot_id>/archive',
        'SnapshotsIdRestore': 'snapshots/<string:snapshot_id>/restore',
        'SnapshotsStatus': 'snapshot-status',
        'Executions': 'executions',
        'ExecutionsId': 'executions/<string:execution_id>',
        'Deployments': 'deployments',
        'DeploymentsId': 'deployments/<string:deployment_id>',
        'DeploymentsSetSite': 'deployments/<string:deployment_id>/set-site',
        'DeploymentsIdOutputs': 'deployments/<string:deployment_id>/outputs',
        'DeploymentsIdCapabilities':
            'deployments/<string:deployment_id>/capabilities',
        'DeploymentsSetVisibility': 'deployments/<string:deployment_id>/'
                                    'set-visibility',
        'DeploymentModifications': 'deployment-modifications',
        'DeploymentModificationsId': 'deployment-modifications/'
                                     '<string:modification_id>',
        'DeploymentModificationsIdFinish': 'deployment-modifications/'
                                           '<string:modification_id>/finish',
        'DeploymentModificationsIdRollback': 'deployment-modifications/'
                                             '<string:modification_id>/'
                                             'rollback',
        'Nodes': 'nodes',
        'NodeInstances': 'node-instances',
        'NodeInstancesId': 'node-instances/<string:node_instance_id>',
        'Events': 'events',
        'Status': 'status',
        'ProviderContext': 'provider/context',
        'Version': 'version',
        'EvaluateFunctions': 'evaluate/functions',
        'Tokens': 'tokens',
        'Plugins': 'plugins',
        'PluginsId': 'plugins/<string:plugin_id>',
        'PluginsUpdate':
            'plugins-updates/<string:id>/update/<string:phase>',
        'PluginsUpdateId': 'plugins-updates/<string:update_id>',
        'PluginsUpdates': 'plugins-updates',
        'PluginsArchive': 'plugins/<string:plugin_id>/archive',
        'PluginsSetGlobal': 'plugins/<string:plugin_id>/set-global',
        'PluginsSetVisibility': 'plugins/<string:plugin_id>/set-visibility',
        'MaintenanceMode': 'maintenance',
        'MaintenanceModeAction': 'maintenance/<string:maintenance_action>',

        'DeploymentUpdate':
            'deployment-updates/<string:id>/update/<string:phase>',
        'DeploymentUpdateId': 'deployment-updates/<string:update_id>',
        'DeploymentUpdates': 'deployment-updates',
        'Tenants': 'tenants',
        'TenantsId': 'tenants/<string:tenant_name>',
        'TenantUsers': 'tenants/users',
        'TenantGroups': 'tenants/user-groups',
        'UserGroups': 'user-groups',
        'UserGroupsId': 'user-groups/<string:group_name>',
        'UserGroupsUsers': 'user-groups/users',
        'User': 'user',
        'Users': 'users',
        'UsersId': 'users/<string:username>',
        'UsersActive': 'users/active/<string:username>',
        'UsersUnlock': 'users/unlock/<string:username>',
        'FileServerAuth': 'file-server-auth',
        'LdapAuthentication': 'ldap',
        'SSLConfig': 'ssl',
        'Secrets': 'secrets',
        'SecretsExport': 'secrets/share/export',
        'SecretsImport': 'secrets/share/import',
        'SecretsKey': 'secrets/<string:key>',
        'SecretsSetGlobal': 'secrets/<string:key>/set-global',
        'SecretsSetVisibility': 'secrets/<string:key>/set-visibility',
        'ManagerConfig': 'config',
        'ManagerConfigId': 'config/<string:name>',
        'Managers': 'managers',
        'ManagersId': 'managers/<string:name>',
        'Agents': 'agents',
        'AgentsName': 'agents/<string:name>',
        'SummarizeDeployments': 'summary/deployments',
        'SummarizeNodes': 'summary/nodes',
        'SummarizeNodeInstances': 'summary/node_instances',
        'SummarizeExecutions': 'summary/executions',
        'SummarizeBlueprints': 'summary/blueprints',
        'UserTokens': 'user-tokens/<string:user_id>',
        'Operations': 'operations',
        'OperationsId': 'operations/<string:operation_id>',
        'TasksGraphs': 'tasks_graphs',
        'TasksGraphsId': 'tasks_graphs/<string:tasks_graph_id>',
        'ExecutionsCheck': 'executions/<execution_id>/should-start',
        'RabbitMQBrokers': 'brokers',
        'DBNodes': 'db-nodes',
        'RabbitMQBrokersId': 'brokers/<string:name>',
        'License': 'license',
        'Sites': 'sites',
        'SitesName': 'sites/<string:name>',
        'ClusterStatus': 'cluster-status',
        'ManagerClusterStatus': 'cluster-status/manager/<string:node_id>',
        'DBClusterStatus': 'cluster-status/db/<string:node_id>',
        'BrokerClusterStatus': 'cluster-status/broker/<string:node_id>'
    }

    # Set version endpoint as a non versioned endpoint
    api.add_resource(resources_v1.Version, '/api/version', endpoint='version')
    for resource, endpoint_suffix in resources_endpoints.iteritems():
        _set_versioned_urls(api, resource, endpoint_suffix)


def _set_versioned_urls(api, resource_name, endpoint_suffix):
    resource = None
    for version in SUPPORTED_API_VERSIONS:
        version_name, resources_impl = version
        if hasattr(resources_impl, resource_name):
            resource = getattr(resources_impl, resource_name)
        # 'resource' will persist throughout iterations, holding a reference
        # to the latest impl.
        if resource:
            endpoint = '{0}/{1}'.format(version_name, endpoint_suffix)
            url = '/api/{0}'.format(endpoint)
            api.add_resource(resource, url, endpoint=endpoint)

            swagger.add_swagger_resource(api, version_name, resource, url)
