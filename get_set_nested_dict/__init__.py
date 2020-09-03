import re


def get_set_nested_dict(nested_dict, path, **kwargs):
    """
    Get or Set a nested value of nested dict by path
    :param nested_dict: nested dict object
        {
          "club": [
            {
              "manager": {
                "last_name": "Lionel",
                "first_name": "Messi"
              }
            }
          ]
        }
    :param path: path to access the nested dict value
        "club[0].manager.first_name"
    :param kwargs: {setter_value: value}
        setter_value='Pulga'
    :return: <modified_nested_dict>, getter_value
        ({'club': [{'manager': {'last_name': 'Pulga', 'first_name': 'Messi'}}]}, 'Lionel')
    """

    regex_arr_mising_dot_prefix = r"([^\.])(\[)"
    regex_append_dot = r"\1.\2"
    regex_split_by_delimiter = r"[\$,\.]"
    regex_array_format = r"(\[)(\d+)(\])"
    normalized_path = re.sub(regex_arr_mising_dot_prefix, regex_append_dot, path)
    current_node = nested_dict
    getter_value = None
    has_setter = 'setter_value' in kwargs.keys() if kwargs else False
    setter_value = kwargs.get('setter_value')

    elements = re.split(regex_split_by_delimiter, normalized_path)
    elements = [element for element in elements if element]
    for index, element in enumerate(elements):
        array_format = re.search(regex_array_format, element)
        key = int(array_format.group(2)) if array_format else element
        getter_value = current_node[key]
        if len(elements) - 1 == index and has_setter:
            current_node[key] = setter_value
        else:
            current_node = getter_value
    return nested_dict, getter_value
