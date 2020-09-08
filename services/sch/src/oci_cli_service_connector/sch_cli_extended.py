# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates. All rights reserved.

from services.sch.src.oci_cli_service_connector.generated import serviceconnector_cli

serviceconnector_cli.service_connector_group.commands.pop(serviceconnector_cli.create_service_connector_functions_target_details.name)
serviceconnector_cli.service_connector_group.commands.pop(serviceconnector_cli.create_service_connector_logging_source_details.name)
serviceconnector_cli.service_connector_group.commands.pop(serviceconnector_cli.create_service_connector_monitoring_target_details.name)
serviceconnector_cli.service_connector_group.commands.pop(serviceconnector_cli.create_service_connector_notifications_target_details.name)
serviceconnector_cli.service_connector_group.commands.pop(serviceconnector_cli.create_service_connector_object_storage_target_details.name)
serviceconnector_cli.service_connector_group.commands.pop(serviceconnector_cli.create_service_connector_streaming_target_details.name)
serviceconnector_cli.service_connector_group.commands.pop(serviceconnector_cli.update_service_connector_functions_target_details.name)
serviceconnector_cli.service_connector_group.commands.pop(serviceconnector_cli.update_service_connector_logging_source_details.name)
serviceconnector_cli.service_connector_group.commands.pop(serviceconnector_cli.update_service_connector_monitoring_target_details.name)
serviceconnector_cli.service_connector_group.commands.pop(serviceconnector_cli.update_service_connector_notifications_target_details.name)
serviceconnector_cli.service_connector_group.commands.pop(serviceconnector_cli.update_service_connector_object_storage_target_details.name)
serviceconnector_cli.service_connector_group.commands.pop(serviceconnector_cli.update_service_connector_streaming_target_details.name)
