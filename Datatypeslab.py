def data_type(x):
    if isinstance(x, str):
        res = len(x)
        return res
    elif x is None:
        return 'no value'
    elif isinstance(x, bool):
        return x
    elif isinstance(x, int):
        if x < 100:
            return 'less than 100'
        elif x == 100:
            return 'equal than 100'
        elif x > 100:
            return 'more than 100'

    elif isinstance(x, list):
      length = len(x)
      if length < 3:
        return None
      else:
        return x[2]
