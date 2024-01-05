def flatten_dictionary(dictionary):
  def flatten_helper(current_key, current_value):
      if isinstance(current_value, dict):
          if current_key:
              current_key += "."
          for nested_key, nested_value in current_value.items():
              flatten_helper(current_key + str(nested_key), nested_value)
      elif current_value is not None:
          flattened_dict[current_key] = current_value

  flattened_dict = {}
  flatten_helper("", dictionary)
  return flattened_dict