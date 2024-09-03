def merge_dicts(dict1, dict2):

    # Create a new dictionary to store the merged result
    merged_dict = dict1.copy()

    # Iterate through the second dictionary
    for key, value in dict2.items():
        # If the key exists in the merged dictionary, sum the values
        if key in merged_dict:
            merged_dict[key] += value
        # If the key doesn't exist, add it to the merged dictionary
        else:
            merged_dict[key] = value
    
    return merged_dict
