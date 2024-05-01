def get_list_from_string(text):
  """
  This function takes a string and returns a list of elements separated by commas.

  Args:
      text: The string to be converted to a list.

  Returns:
      A list of elements from the string, or an empty list if the string is empty.
  """
  if not text:
    return []
  return text.split(",")