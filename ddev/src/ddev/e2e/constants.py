# (C) Datadog, Inc. 2024-present
# All rights reserved
# Licensed under a 3-clause BSD style license (see LICENSE)

DEFAULT_AGENT_TYPE = 'docker'
DEFAULT_DOGSTATSD_PORT = 8125
ENV_VAR_PREFIX = 'DDEV_E2E_ENV_'


class E2EEnvVars:
    AGENT_BUILD = 'DDEV_E2E_AGENT'
    AGENT_BUILD_PY2 = 'DDEV_E2E_AGENT_PY2'
    SET_UP = 'DDEV_E2E_UP'
    TEAR_DOWN = 'DDEV_E2E_DOWN'
    PARENT_PYTHON = 'DDEV_E2E_PYTHON_PATH'
    RESULT_FILE = 'DDEV_E2E_RESULT_FILE'
    LOGS_DIR_PREFIX = 'DDEV_E2E_ENV_TEMP_DIR_DD_LOG_'
    DOCKER_VOLUMES = 'DDEV_E2E_ENV_docker_volumes'


class E2EMetadata:
    AGENT_TYPE = 'agent_type'
    ENV_VARS = 'e2e_env_vars'
    DOCKER_VOLUMES = 'docker_volumes'
