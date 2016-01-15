simple_types_set = {
    str,
    int,
    float,
    bool,
}


def keys_path_to_simple_values(d: dict, path=None):
    """

    >>> list(keys_path_to_simple_values({1:1}))
    [['1']]

    >>> list(keys_path_to_simple_values({1:1, 2:2}))
    [['1'], ['2']]

    >>> list(keys_path_to_simple_values({'app': {'services': 'v'}}))
    [['app', 'services']]

    >>> list(keys_path_to_simple_values({'app': {'services': 'v', 'port': 8}}))
    [['app', 'services'], ['app', 'port']]

    >>> list(keys_path_to_simple_values({'app': [1, 2]}))  # not supported
    []

    :param d: dict like object
    :param path: previous keys path as list
    :return:
    """
    if path is None:
        path = []

    for key, value in d.items():
        current_path = path + [str(key)]

        if type(value) in simple_types_set:
            yield current_path
        elif isinstance(value, dict):
            yield from keys_path_to_simple_values(value, current_path)
