# `random_dict` has been defined
# the input is in the variable `word`
# write the rest of the code here
value = random_dict.setdefault(word, None)
if value is None:
    print("Not in the dictionary")
else:
    print(value)
