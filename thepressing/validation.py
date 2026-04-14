import inspect


def empty_validation_results(cls) -> dict:
    v_keys = list(inspect.signature(cls.__init__).parameters.keys())[1:]
    validation_results = dict(zip(v_keys, map(lambda k: [], v_keys)))
    return validation_results


def valid(validation_results) -> bool:
    return not any(0 < len(validation_result) for validation_result in validation_results.values())


class ValidationError(Exception):
    'Validation Error'
    pass
