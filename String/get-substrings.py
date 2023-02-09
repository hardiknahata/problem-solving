def get_substrings(s):
  '''Returns all possible contiiguous subarrays/substrings for a given string/array'''

    # base case when length is zero
    if(len(s) == 0):
        return []
    
    substrings = []
    # append the string
    substrings.append(s)
    # append all substrings by removing first character
    substrings.extend(get_substrings(s[1:]))
    # append all substrings by removing last character    
    substrings.extend(get_substrings(s[:-1]))
    # remove duplicates
    substrings = list(set(substrings))

    return substrings
