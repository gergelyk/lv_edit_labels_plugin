# Increase index by one.
# Example:
# foo 1 -> foo 2
labels = ['foo']
import re

for label in labels:
    core, index = re.match( '(.*?)(\\d*)$', label).groups()
    if index:
        new_index = max(0, int(index)+1)
        print(core + str(new_index))
    else:
        print(label)
