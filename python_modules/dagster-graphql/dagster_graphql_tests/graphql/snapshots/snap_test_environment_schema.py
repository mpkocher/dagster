# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot

snapshots = Snapshot()

snapshots['TestEnvironmentSchema.test_basic_valid_config_on_run_config_schema[readonly_in_memory_instance_in_process_env] 1'] = {
    'runConfigSchemaOrError': {
        'isRunConfigValid': {
            '__typename': 'PipelineConfigValidationValid',
            'pipelineName': 'csv_hello_world'
        }
    }
}

snapshots['TestEnvironmentSchema.test_basic_valid_config_on_run_config_schema[readonly_in_memory_instance_out_of_process_env] 1'] = {
    'runConfigSchemaOrError': {
        'isRunConfigValid': {
            '__typename': 'PipelineConfigValidationValid',
            'pipelineName': 'csv_hello_world'
        }
    }
}

snapshots['TestEnvironmentSchema.test_basic_valid_config_on_run_config_schema[readonly_in_memory_instance_multi_location] 1'] = {
    'runConfigSchemaOrError': {
        'isRunConfigValid': {
            '__typename': 'PipelineConfigValidationValid',
            'pipelineName': 'csv_hello_world'
        }
    }
}

snapshots['TestEnvironmentSchema.test_basic_valid_config_on_run_config_schema[readonly_sqlite_instance_in_process_env] 1'] = {
    'runConfigSchemaOrError': {
        'isRunConfigValid': {
            '__typename': 'PipelineConfigValidationValid',
            'pipelineName': 'csv_hello_world'
        }
    }
}

snapshots['TestEnvironmentSchema.test_basic_valid_config_on_run_config_schema[readonly_sqlite_instance_out_of_process_env] 1'] = {
    'runConfigSchemaOrError': {
        'isRunConfigValid': {
            '__typename': 'PipelineConfigValidationValid',
            'pipelineName': 'csv_hello_world'
        }
    }
}

snapshots['TestEnvironmentSchema.test_basic_valid_config_on_run_config_schema[readonly_sqlite_instance_multi_location] 1'] = {
    'runConfigSchemaOrError': {
        'isRunConfigValid': {
            '__typename': 'PipelineConfigValidationValid',
            'pipelineName': 'csv_hello_world'
        }
    }
}

snapshots['TestEnvironmentSchema.test_basic_invalid_config_on_run_config_schema[readonly_in_memory_instance_in_process_env] 1'] = {
    'runConfigSchemaOrError': {
        'isRunConfigValid': {
            '__typename': 'PipelineConfigValidationInvalid',
            'errors': [
                {
                    '__typename': 'FieldNotDefinedConfigError',
                    'fieldName': 'nope',
                    'message': 'Undefined field "nope" at the root. Expected: "{ execution?: { in_process?: { config?: { marker_to_close?: String retries?: { disabled?: { } enabled?: { } } } } multiprocess?: { config?: { max_concurrent?: Int retries?: { disabled?: { } enabled?: { } } } } } intermediate_storage?: { filesystem?: { config?: { base_dir?: String } } in_memory?: { } } loggers?: { console?: { config?: { log_level?: String name?: String } } } resources?: { } solids: { sum_solid: { inputs: { num: String } outputs?: [{ result?: String }] } sum_sq_solid?: { outputs?: [{ result?: String }] } } storage?: { filesystem?: { config?: { base_dir?: String } } in_memory?: { } } }".',
                    'reason': 'FIELD_NOT_DEFINED',
                    'stack': {
                        'entries': [
                        ]
                    }
                },
                {
                    '__typename': 'MissingFieldConfigError',
                    'field': {
                        'name': 'solids'
                    },
                    'message': 'Missing required field "solids" at the root. Available Fields: "[\'execution\', \'intermediate_storage\', \'loggers\', \'resources\', \'solids\', \'storage\']".',
                    'reason': 'MISSING_REQUIRED_FIELD',
                    'stack': {
                        'entries': [
                        ]
                    }
                }
            ],
            'pipelineName': 'csv_hello_world'
        }
    }
}

snapshots['TestEnvironmentSchema.test_basic_invalid_config_on_run_config_schema[readonly_in_memory_instance_out_of_process_env] 1'] = {
    'runConfigSchemaOrError': {
        'isRunConfigValid': {
            '__typename': 'PipelineConfigValidationInvalid',
            'errors': [
                {
                    '__typename': 'FieldNotDefinedConfigError',
                    'fieldName': 'nope',
                    'message': 'Undefined field "nope" at the root. Expected: "{ execution?: { in_process?: { config?: { marker_to_close?: String retries?: { disabled?: { } enabled?: { } } } } multiprocess?: { config?: { max_concurrent?: Int retries?: { disabled?: { } enabled?: { } } } } } intermediate_storage?: { filesystem?: { config?: { base_dir?: String } } in_memory?: { } } loggers?: { console?: { config?: { log_level?: String name?: String } } } resources?: { } solids: { sum_solid: { inputs: { num: String } outputs?: [{ result?: String }] } sum_sq_solid?: { outputs?: [{ result?: String }] } } storage?: { filesystem?: { config?: { base_dir?: String } } in_memory?: { } } }".',
                    'reason': 'FIELD_NOT_DEFINED',
                    'stack': {
                        'entries': [
                        ]
                    }
                },
                {
                    '__typename': 'MissingFieldConfigError',
                    'field': {
                        'name': 'solids'
                    },
                    'message': 'Missing required field "solids" at the root. Available Fields: "[\'execution\', \'intermediate_storage\', \'loggers\', \'resources\', \'solids\', \'storage\']".',
                    'reason': 'MISSING_REQUIRED_FIELD',
                    'stack': {
                        'entries': [
                        ]
                    }
                }
            ],
            'pipelineName': 'csv_hello_world'
        }
    }
}

snapshots['TestEnvironmentSchema.test_basic_invalid_config_on_run_config_schema[readonly_in_memory_instance_multi_location] 1'] = {
    'runConfigSchemaOrError': {
        'isRunConfigValid': {
            '__typename': 'PipelineConfigValidationInvalid',
            'errors': [
                {
                    '__typename': 'FieldNotDefinedConfigError',
                    'fieldName': 'nope',
                    'message': 'Undefined field "nope" at the root. Expected: "{ execution?: { in_process?: { config?: { marker_to_close?: String retries?: { disabled?: { } enabled?: { } } } } multiprocess?: { config?: { max_concurrent?: Int retries?: { disabled?: { } enabled?: { } } } } } intermediate_storage?: { filesystem?: { config?: { base_dir?: String } } in_memory?: { } } loggers?: { console?: { config?: { log_level?: String name?: String } } } resources?: { } solids: { sum_solid: { inputs: { num: String } outputs?: [{ result?: String }] } sum_sq_solid?: { outputs?: [{ result?: String }] } } storage?: { filesystem?: { config?: { base_dir?: String } } in_memory?: { } } }".',
                    'reason': 'FIELD_NOT_DEFINED',
                    'stack': {
                        'entries': [
                        ]
                    }
                },
                {
                    '__typename': 'MissingFieldConfigError',
                    'field': {
                        'name': 'solids'
                    },
                    'message': 'Missing required field "solids" at the root. Available Fields: "[\'execution\', \'intermediate_storage\', \'loggers\', \'resources\', \'solids\', \'storage\']".',
                    'reason': 'MISSING_REQUIRED_FIELD',
                    'stack': {
                        'entries': [
                        ]
                    }
                }
            ],
            'pipelineName': 'csv_hello_world'
        }
    }
}

snapshots['TestEnvironmentSchema.test_basic_invalid_config_on_run_config_schema[readonly_sqlite_instance_in_process_env] 1'] = {
    'runConfigSchemaOrError': {
        'isRunConfigValid': {
            '__typename': 'PipelineConfigValidationInvalid',
            'errors': [
                {
                    '__typename': 'FieldNotDefinedConfigError',
                    'fieldName': 'nope',
                    'message': 'Undefined field "nope" at the root. Expected: "{ execution?: { in_process?: { config?: { marker_to_close?: String retries?: { disabled?: { } enabled?: { } } } } multiprocess?: { config?: { max_concurrent?: Int retries?: { disabled?: { } enabled?: { } } } } } intermediate_storage?: { filesystem?: { config?: { base_dir?: String } } in_memory?: { } } loggers?: { console?: { config?: { log_level?: String name?: String } } } resources?: { } solids: { sum_solid: { inputs: { num: String } outputs?: [{ result?: String }] } sum_sq_solid?: { outputs?: [{ result?: String }] } } storage?: { filesystem?: { config?: { base_dir?: String } } in_memory?: { } } }".',
                    'reason': 'FIELD_NOT_DEFINED',
                    'stack': {
                        'entries': [
                        ]
                    }
                },
                {
                    '__typename': 'MissingFieldConfigError',
                    'field': {
                        'name': 'solids'
                    },
                    'message': 'Missing required field "solids" at the root. Available Fields: "[\'execution\', \'intermediate_storage\', \'loggers\', \'resources\', \'solids\', \'storage\']".',
                    'reason': 'MISSING_REQUIRED_FIELD',
                    'stack': {
                        'entries': [
                        ]
                    }
                }
            ],
            'pipelineName': 'csv_hello_world'
        }
    }
}

snapshots['TestEnvironmentSchema.test_basic_invalid_config_on_run_config_schema[readonly_sqlite_instance_out_of_process_env] 1'] = {
    'runConfigSchemaOrError': {
        'isRunConfigValid': {
            '__typename': 'PipelineConfigValidationInvalid',
            'errors': [
                {
                    '__typename': 'FieldNotDefinedConfigError',
                    'fieldName': 'nope',
                    'message': 'Undefined field "nope" at the root. Expected: "{ execution?: { in_process?: { config?: { marker_to_close?: String retries?: { disabled?: { } enabled?: { } } } } multiprocess?: { config?: { max_concurrent?: Int retries?: { disabled?: { } enabled?: { } } } } } intermediate_storage?: { filesystem?: { config?: { base_dir?: String } } in_memory?: { } } loggers?: { console?: { config?: { log_level?: String name?: String } } } resources?: { } solids: { sum_solid: { inputs: { num: String } outputs?: [{ result?: String }] } sum_sq_solid?: { outputs?: [{ result?: String }] } } storage?: { filesystem?: { config?: { base_dir?: String } } in_memory?: { } } }".',
                    'reason': 'FIELD_NOT_DEFINED',
                    'stack': {
                        'entries': [
                        ]
                    }
                },
                {
                    '__typename': 'MissingFieldConfigError',
                    'field': {
                        'name': 'solids'
                    },
                    'message': 'Missing required field "solids" at the root. Available Fields: "[\'execution\', \'intermediate_storage\', \'loggers\', \'resources\', \'solids\', \'storage\']".',
                    'reason': 'MISSING_REQUIRED_FIELD',
                    'stack': {
                        'entries': [
                        ]
                    }
                }
            ],
            'pipelineName': 'csv_hello_world'
        }
    }
}

snapshots['TestEnvironmentSchema.test_basic_invalid_config_on_run_config_schema[readonly_sqlite_instance_multi_location] 1'] = {
    'runConfigSchemaOrError': {
        'isRunConfigValid': {
            '__typename': 'PipelineConfigValidationInvalid',
            'errors': [
                {
                    '__typename': 'FieldNotDefinedConfigError',
                    'fieldName': 'nope',
                    'message': 'Undefined field "nope" at the root. Expected: "{ execution?: { in_process?: { config?: { marker_to_close?: String retries?: { disabled?: { } enabled?: { } } } } multiprocess?: { config?: { max_concurrent?: Int retries?: { disabled?: { } enabled?: { } } } } } intermediate_storage?: { filesystem?: { config?: { base_dir?: String } } in_memory?: { } } loggers?: { console?: { config?: { log_level?: String name?: String } } } resources?: { } solids: { sum_solid: { inputs: { num: String } outputs?: [{ result?: String }] } sum_sq_solid?: { outputs?: [{ result?: String }] } } storage?: { filesystem?: { config?: { base_dir?: String } } in_memory?: { } } }".',
                    'reason': 'FIELD_NOT_DEFINED',
                    'stack': {
                        'entries': [
                        ]
                    }
                },
                {
                    '__typename': 'MissingFieldConfigError',
                    'field': {
                        'name': 'solids'
                    },
                    'message': 'Missing required field "solids" at the root. Available Fields: "[\'execution\', \'intermediate_storage\', \'loggers\', \'resources\', \'solids\', \'storage\']".',
                    'reason': 'MISSING_REQUIRED_FIELD',
                    'stack': {
                        'entries': [
                        ]
                    }
                }
            ],
            'pipelineName': 'csv_hello_world'
        }
    }
}

snapshots['TestEnvironmentSchema.test_basic_valid_config_on_run_config_schema[readonly_postgres_instance_in_process_env] 1'] = {
    'runConfigSchemaOrError': {
        'isRunConfigValid': {
            '__typename': 'PipelineConfigValidationValid',
            'pipelineName': 'csv_hello_world'
        }
    }
}

snapshots['TestEnvironmentSchema.test_basic_valid_config_on_run_config_schema[readonly_postgres_instance_out_of_process_env] 1'] = {
    'runConfigSchemaOrError': {
        'isRunConfigValid': {
            '__typename': 'PipelineConfigValidationValid',
            'pipelineName': 'csv_hello_world'
        }
    }
}

snapshots['TestEnvironmentSchema.test_basic_valid_config_on_run_config_schema[readonly_postgres_instance_multi_location] 1'] = {
    'runConfigSchemaOrError': {
        'isRunConfigValid': {
            '__typename': 'PipelineConfigValidationValid',
            'pipelineName': 'csv_hello_world'
        }
    }
}

snapshots['TestEnvironmentSchema.test_basic_invalid_config_on_run_config_schema[readonly_postgres_instance_in_process_env] 1'] = {
    'runConfigSchemaOrError': {
        'isRunConfigValid': {
            '__typename': 'PipelineConfigValidationInvalid',
            'errors': [
                {
                    '__typename': 'FieldNotDefinedConfigError',
                    'fieldName': 'nope',
                    'message': 'Undefined field "nope" at the root. Expected: "{ execution?: { in_process?: { config?: { marker_to_close?: String retries?: { disabled?: { } enabled?: { } } } } multiprocess?: { config?: { max_concurrent?: Int retries?: { disabled?: { } enabled?: { } } } } } intermediate_storage?: { filesystem?: { config?: { base_dir?: String } } in_memory?: { } } loggers?: { console?: { config?: { log_level?: String name?: String } } } resources?: { } solids: { sum_solid: { inputs: { num: String } outputs?: [{ result?: String }] } sum_sq_solid?: { outputs?: [{ result?: String }] } } storage?: { filesystem?: { config?: { base_dir?: String } } in_memory?: { } } }".',
                    'reason': 'FIELD_NOT_DEFINED',
                    'stack': {
                        'entries': [
                        ]
                    }
                },
                {
                    '__typename': 'MissingFieldConfigError',
                    'field': {
                        'name': 'solids'
                    },
                    'message': 'Missing required field "solids" at the root. Available Fields: "[\'execution\', \'intermediate_storage\', \'loggers\', \'resources\', \'solids\', \'storage\']".',
                    'reason': 'MISSING_REQUIRED_FIELD',
                    'stack': {
                        'entries': [
                        ]
                    }
                }
            ],
            'pipelineName': 'csv_hello_world'
        }
    }
}

snapshots['TestEnvironmentSchema.test_basic_invalid_config_on_run_config_schema[readonly_postgres_instance_out_of_process_env] 1'] = {
    'runConfigSchemaOrError': {
        'isRunConfigValid': {
            '__typename': 'PipelineConfigValidationInvalid',
            'errors': [
                {
                    '__typename': 'FieldNotDefinedConfigError',
                    'fieldName': 'nope',
                    'message': 'Undefined field "nope" at the root. Expected: "{ execution?: { in_process?: { config?: { marker_to_close?: String retries?: { disabled?: { } enabled?: { } } } } multiprocess?: { config?: { max_concurrent?: Int retries?: { disabled?: { } enabled?: { } } } } } intermediate_storage?: { filesystem?: { config?: { base_dir?: String } } in_memory?: { } } loggers?: { console?: { config?: { log_level?: String name?: String } } } resources?: { } solids: { sum_solid: { inputs: { num: String } outputs?: [{ result?: String }] } sum_sq_solid?: { outputs?: [{ result?: String }] } } storage?: { filesystem?: { config?: { base_dir?: String } } in_memory?: { } } }".',
                    'reason': 'FIELD_NOT_DEFINED',
                    'stack': {
                        'entries': [
                        ]
                    }
                },
                {
                    '__typename': 'MissingFieldConfigError',
                    'field': {
                        'name': 'solids'
                    },
                    'message': 'Missing required field "solids" at the root. Available Fields: "[\'execution\', \'intermediate_storage\', \'loggers\', \'resources\', \'solids\', \'storage\']".',
                    'reason': 'MISSING_REQUIRED_FIELD',
                    'stack': {
                        'entries': [
                        ]
                    }
                }
            ],
            'pipelineName': 'csv_hello_world'
        }
    }
}

snapshots['TestEnvironmentSchema.test_basic_invalid_config_on_run_config_schema[readonly_postgres_instance_multi_location] 1'] = {
    'runConfigSchemaOrError': {
        'isRunConfigValid': {
            '__typename': 'PipelineConfigValidationInvalid',
            'errors': [
                {
                    '__typename': 'FieldNotDefinedConfigError',
                    'fieldName': 'nope',
                    'message': 'Undefined field "nope" at the root. Expected: "{ execution?: { in_process?: { config?: { marker_to_close?: String retries?: { disabled?: { } enabled?: { } } } } multiprocess?: { config?: { max_concurrent?: Int retries?: { disabled?: { } enabled?: { } } } } } intermediate_storage?: { filesystem?: { config?: { base_dir?: String } } in_memory?: { } } loggers?: { console?: { config?: { log_level?: String name?: String } } } resources?: { } solids: { sum_solid: { inputs: { num: String } outputs?: [{ result?: String }] } sum_sq_solid?: { outputs?: [{ result?: String }] } } storage?: { filesystem?: { config?: { base_dir?: String } } in_memory?: { } } }".',
                    'reason': 'FIELD_NOT_DEFINED',
                    'stack': {
                        'entries': [
                        ]
                    }
                },
                {
                    '__typename': 'MissingFieldConfigError',
                    'field': {
                        'name': 'solids'
                    },
                    'message': 'Missing required field "solids" at the root. Available Fields: "[\'execution\', \'intermediate_storage\', \'loggers\', \'resources\', \'solids\', \'storage\']".',
                    'reason': 'MISSING_REQUIRED_FIELD',
                    'stack': {
                        'entries': [
                        ]
                    }
                }
            ],
            'pipelineName': 'csv_hello_world'
        }
    }
}

snapshots['TestEnvironmentSchema.test_basic_valid_config_on_run_config_schema[readonly_in_memory_instance_grpc] 1'] = {
    'runConfigSchemaOrError': {
        'isRunConfigValid': {
            '__typename': 'PipelineConfigValidationValid',
            'pipelineName': 'csv_hello_world'
        }
    }
}

snapshots['TestEnvironmentSchema.test_basic_invalid_config_on_run_config_schema[readonly_in_memory_instance_grpc] 1'] = {
    'runConfigSchemaOrError': {
        'isRunConfigValid': {
            '__typename': 'PipelineConfigValidationInvalid',
            'errors': [
                {
                    '__typename': 'FieldNotDefinedConfigError',
                    'fieldName': 'nope',
                    'message': 'Undefined field "nope" at the root. Expected: "{ execution?: { in_process?: { config?: { marker_to_close?: String retries?: { disabled?: { } enabled?: { } } } } multiprocess?: { config?: { max_concurrent?: Int retries?: { disabled?: { } enabled?: { } } } } } intermediate_storage?: { filesystem?: { config?: { base_dir?: String } } in_memory?: { } } loggers?: { console?: { config?: { log_level?: String name?: String } } } resources?: { } solids: { sum_solid: { inputs: { num: String } outputs?: [{ result?: String }] } sum_sq_solid?: { outputs?: [{ result?: String }] } } storage?: { filesystem?: { config?: { base_dir?: String } } in_memory?: { } } }".',
                    'reason': 'FIELD_NOT_DEFINED',
                    'stack': {
                        'entries': [
                        ]
                    }
                },
                {
                    '__typename': 'MissingFieldConfigError',
                    'field': {
                        'name': 'solids'
                    },
                    'message': 'Missing required field "solids" at the root. Available Fields: "[\'execution\', \'intermediate_storage\', \'loggers\', \'resources\', \'solids\', \'storage\']".',
                    'reason': 'MISSING_REQUIRED_FIELD',
                    'stack': {
                        'entries': [
                        ]
                    }
                }
            ],
            'pipelineName': 'csv_hello_world'
        }
    }
}

snapshots['TestEnvironmentSchema.test_basic_valid_config_on_run_config_schema[readonly_sqlite_instance_external_grpc_server] 1'] = {
    'runConfigSchemaOrError': {
        'isRunConfigValid': {
            '__typename': 'PipelineConfigValidationValid',
            'pipelineName': 'csv_hello_world'
        }
    }
}

snapshots['TestEnvironmentSchema.test_basic_invalid_config_on_run_config_schema[readonly_sqlite_instance_external_grpc_server] 1'] = {
    'runConfigSchemaOrError': {
        'isRunConfigValid': {
            '__typename': 'PipelineConfigValidationInvalid',
            'errors': [
                {
                    '__typename': 'FieldNotDefinedConfigError',
                    'fieldName': 'nope',
                    'message': 'Undefined field "nope" at the root. Expected: "{ execution?: { in_process?: { config?: { marker_to_close?: String retries?: { disabled?: { } enabled?: { } } } } multiprocess?: { config?: { max_concurrent?: Int retries?: { disabled?: { } enabled?: { } } } } } intermediate_storage?: { filesystem?: { config?: { base_dir?: String } } in_memory?: { } } loggers?: { console?: { config?: { log_level?: String name?: String } } } resources?: { } solids: { sum_solid: { inputs: { num: String } outputs?: [{ result?: String }] } sum_sq_solid?: { outputs?: [{ result?: String }] } } storage?: { filesystem?: { config?: { base_dir?: String } } in_memory?: { } } }".',
                    'reason': 'FIELD_NOT_DEFINED',
                    'stack': {
                        'entries': [
                        ]
                    }
                },
                {
                    '__typename': 'MissingFieldConfigError',
                    'field': {
                        'name': 'solids'
                    },
                    'message': 'Missing required field "solids" at the root. Available Fields: "[\'execution\', \'intermediate_storage\', \'loggers\', \'resources\', \'solids\', \'storage\']".',
                    'reason': 'MISSING_REQUIRED_FIELD',
                    'stack': {
                        'entries': [
                        ]
                    }
                }
            ],
            'pipelineName': 'csv_hello_world'
        }
    }
}

snapshots['TestEnvironmentSchema.test_basic_valid_config_on_run_config_schema[readonly_sqlite_instance_grpc] 1'] = {
    'runConfigSchemaOrError': {
        'isRunConfigValid': {
            '__typename': 'PipelineConfigValidationValid',
            'pipelineName': 'csv_hello_world'
        }
    }
}

snapshots['TestEnvironmentSchema.test_basic_invalid_config_on_run_config_schema[readonly_sqlite_instance_grpc] 1'] = {
    'runConfigSchemaOrError': {
        'isRunConfigValid': {
            '__typename': 'PipelineConfigValidationInvalid',
            'errors': [
                {
                    '__typename': 'FieldNotDefinedConfigError',
                    'fieldName': 'nope',
                    'message': 'Undefined field "nope" at the root. Expected: "{ execution?: { in_process?: { config?: { marker_to_close?: String retries?: { disabled?: { } enabled?: { } } } } multiprocess?: { config?: { max_concurrent?: Int retries?: { disabled?: { } enabled?: { } } } } } intermediate_storage?: { filesystem?: { config?: { base_dir?: String } } in_memory?: { } } loggers?: { console?: { config?: { log_level?: String name?: String } } } resources?: { } solids: { sum_solid: { inputs: { num: String } outputs?: [{ result?: String }] } sum_sq_solid?: { outputs?: [{ result?: String }] } } storage?: { filesystem?: { config?: { base_dir?: String } } in_memory?: { } } }".',
                    'reason': 'FIELD_NOT_DEFINED',
                    'stack': {
                        'entries': [
                        ]
                    }
                },
                {
                    '__typename': 'MissingFieldConfigError',
                    'field': {
                        'name': 'solids'
                    },
                    'message': 'Missing required field "solids" at the root. Available Fields: "[\'execution\', \'intermediate_storage\', \'loggers\', \'resources\', \'solids\', \'storage\']".',
                    'reason': 'MISSING_REQUIRED_FIELD',
                    'stack': {
                        'entries': [
                        ]
                    }
                }
            ],
            'pipelineName': 'csv_hello_world'
        }
    }
}

snapshots['TestEnvironmentSchema.test_basic_valid_config_on_run_config_schema[readonly_postgres_instance_grpc] 1'] = {
    'runConfigSchemaOrError': {
        'isRunConfigValid': {
            '__typename': 'PipelineConfigValidationValid',
            'pipelineName': 'csv_hello_world'
        }
    }
}

snapshots['TestEnvironmentSchema.test_basic_invalid_config_on_run_config_schema[readonly_postgres_instance_grpc] 1'] = {
    'runConfigSchemaOrError': {
        'isRunConfigValid': {
            '__typename': 'PipelineConfigValidationInvalid',
            'errors': [
                {
                    '__typename': 'FieldNotDefinedConfigError',
                    'fieldName': 'nope',
                    'message': 'Undefined field "nope" at the root. Expected: "{ execution?: { in_process?: { config?: { marker_to_close?: String retries?: { disabled?: { } enabled?: { } } } } multiprocess?: { config?: { max_concurrent?: Int retries?: { disabled?: { } enabled?: { } } } } } intermediate_storage?: { filesystem?: { config?: { base_dir?: String } } in_memory?: { } } loggers?: { console?: { config?: { log_level?: String name?: String } } } resources?: { } solids: { sum_solid: { inputs: { num: String } outputs?: [{ result?: String }] } sum_sq_solid?: { outputs?: [{ result?: String }] } } storage?: { filesystem?: { config?: { base_dir?: String } } in_memory?: { } } }".',
                    'reason': 'FIELD_NOT_DEFINED',
                    'stack': {
                        'entries': [
                        ]
                    }
                },
                {
                    '__typename': 'MissingFieldConfigError',
                    'field': {
                        'name': 'solids'
                    },
                    'message': 'Missing required field "solids" at the root. Available Fields: "[\'execution\', \'intermediate_storage\', \'loggers\', \'resources\', \'solids\', \'storage\']".',
                    'reason': 'MISSING_REQUIRED_FIELD',
                    'stack': {
                        'entries': [
                        ]
                    }
                }
            ],
            'pipelineName': 'csv_hello_world'
        }
    }
}
