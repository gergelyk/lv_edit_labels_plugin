# Remove prefix from the beginning of the label.
# Example:
# foo.bar -> bar

import re

prefix_sep = '.'
    
for label in labels:
    m = re.match( '([^\\' + prefix_sep +']*)\\' + prefix_sep + '(.*)$', label)
    if m:
        print(m.groups()[1])
    else:
        print(label)
