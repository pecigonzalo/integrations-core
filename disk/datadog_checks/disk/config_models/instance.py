# (C) Datadog, Inc. 2021-present
# All rights reserved
# Licensed under a 3-clause BSD style license (see LICENSE)

# This file is autogenerated.
# To change this file you should edit assets/configuration/spec.yaml and then run the following commands:
#     ddev -x validate config -s <INTEGRATION_NAME>
#     ddev -x validate models -s <INTEGRATION_NAME>

from __future__ import annotations

from types import MappingProxyType
from typing import Any, Optional

from pydantic import BaseModel, ConfigDict, field_validator, model_validator

from datadog_checks.base.utils.functions import identity
from datadog_checks.base.utils.models import validation

from . import defaults, validators


class CreateMount(BaseModel):
    model_config = ConfigDict(
        arbitrary_types_allowed=True,
        frozen=True,
    )
    host: Optional[str] = None
    mountpoint: Optional[str] = None
    password: Optional[str] = None
    share: Optional[str] = None
    type: Optional[str] = None
    user: Optional[str] = None


class MetricPatterns(BaseModel):
    model_config = ConfigDict(
        arbitrary_types_allowed=True,
        frozen=True,
    )
    exclude: Optional[tuple[str, ...]] = None
    include: Optional[tuple[str, ...]] = None


class InstanceConfig(BaseModel):
    model_config = ConfigDict(
        validate_default=True,
        arbitrary_types_allowed=True,
        frozen=True,
    )
    all_partitions: Optional[bool] = None
    blkid_cache_file: Optional[str] = None
    create_mounts: Optional[tuple[CreateMount, ...]] = None
    device_exclude: Optional[tuple[str, ...]] = None
    device_include: Optional[tuple[str, ...]] = None
    device_tag_re: Optional[MappingProxyType[str, Any]] = None
    disable_generic_tags: Optional[bool] = None
    empty_default_hostname: Optional[bool] = None
    file_system_exclude: Optional[tuple[str, ...]] = None
    file_system_include: Optional[tuple[str, ...]] = None
    include_all_devices: Optional[bool] = None
    metric_patterns: Optional[MetricPatterns] = None
    min_collection_interval: Optional[float] = None
    min_disk_size: Optional[float] = None
    mount_point_exclude: Optional[tuple[str, ...]] = None
    mount_point_include: Optional[tuple[str, ...]] = None
    service: Optional[str] = None
    service_check_rw: Optional[bool] = None
    tag_by_filesystem: Optional[bool] = None
    tag_by_label: Optional[bool] = None
    tags: Optional[tuple[str, ...]] = None
    timeout: Optional[int] = None
    use_lsblk: Optional[bool] = None
    use_mount: Optional[bool] = None

    @model_validator(mode='before')
    def _initial_validation(cls, values):
        return validation.core.initialize_config(getattr(validators, 'initialize_instance', identity)(values))

    @field_validator('*', mode='before')
    def _validate(cls, value, info):
        field = cls.model_fields[info.field_name]
        field_name = field.alias or info.field_name
        if field_name in info.context['configured_fields']:
            value = getattr(validators, f'instance_{info.field_name}', identity)(value, field=field)
        else:
            value = getattr(defaults, f'instance_{info.field_name}', lambda: value)()

        return validation.utils.make_immutable(value)

    @model_validator(mode='after')
    def _final_validation(cls, model):
        return validation.core.check_model(getattr(validators, 'check_instance', identity)(model))
