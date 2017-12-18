#########
# Copyright (c) 2016 GigaSpaces Technologies Ltd. All rights reserved
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

from manager_rest.storage import models
from manager_rest.security import SecuredResource
from manager_rest.security.authorization import authorize
from manager_rest.resource_manager import get_resource_manager
from manager_rest.storage.models_states import AvailabilityState
from manager_rest.upload_manager import UploadedBlueprintsManager
from manager_rest.rest import (rest_utils,
                               resources_v2,
                               rest_decorators)


class BlueprintsSetGlobal(SecuredResource):

    @rest_decorators.exceptions_handled
    @authorize('resource_set_global')
    @rest_decorators.marshal_with(models.Blueprint)
    def patch(self, blueprint_id):
        """
        Set the blueprint's availability to global
        """
        return get_resource_manager().set_availability(
            models.Blueprint,
            blueprint_id,
            AvailabilityState.GLOBAL
        )


class BlueprintsSetAvailability(SecuredResource):

    @rest_decorators.exceptions_handled
    @authorize('resource_set_availability')
    @rest_decorators.marshal_with(models.Blueprint)
    def patch(self, blueprint_id):
        """
        Set the blueprint's availability
        """
        availability = rest_utils.get_availability_parameter()
        return get_resource_manager().set_availability(models.Blueprint,
                                                       blueprint_id,
                                                       availability)


class BlueprintsId(resources_v2.BlueprintsId):
    @rest_decorators.exceptions_handled
    @authorize('blueprint_upload')
    @rest_decorators.marshal_with(models.Blueprint)
    def put(self, blueprint_id, **kwargs):
        """
        Upload a blueprint (id specified)
        """
        availability = rest_utils.get_availability_parameter(
            optional=True,
            is_argument=True,
            valid_values=AvailabilityState.STATES
        )
        return UploadedBlueprintsManager().\
            receive_uploaded_data(data_id=blueprint_id,
                                  availability=availability)
