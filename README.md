# get_set_nested_dict
Get or Set a nested value of nested dict by path

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

#####Installation:
https://pypi.org/project/get_set_nested_dict/

    pip install get_set_nested_dict

#####Usage:

    nested_dict = {
      "key": [
        {
          "sub_key": {
            "sub_sub_key_1": "Value_1",
            "sub_sub_key_2": "Value_2"
          }
        }
      ]
    }


`before:`

    sub_sub_value_1 = nested_dict['key'][0]['sub_key']['sub_sub_key_1']

`after:`

    from get_set_nested_dict import get_set_nested_dict
    nested_dict, sub_sub_value_1 = get_set_nested_dict(nested_dict, "key[0].sub_key.sub_sub_key_1")
        
#####Example:

    nested_dict = {
      "club": [
        {
          "manager": {
            "last_name": "Lionel",
            "first_name": "Messi"
          }
        }
      ]
    }


`before:`

    manager_last_name = nested_dict['club'][0]['manager']['last_name']
    nested_dict['club'][0]['manager']['last_name'] = 'Pulga'

`after:`

    from get_set_nested_dict import get_set_nested_dict
    path = "club[0].manager.last_name"
    nested_dict, manager_last_name = get_set_nested_dict(nested_dict, path, setter_value='Pulga')

    >>> nested_dict
    {'club': [{'manager': {'last_name': 'Pulga', 'first_name': 'Messi'}}]}
    >>> manager_last_name
    'Lionel'
