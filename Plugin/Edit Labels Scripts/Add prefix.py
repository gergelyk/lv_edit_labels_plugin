# Add prefix at the beginning of the label.
# Example:
# bar -> foo.bar

import re

prefix_sep = '.'
prefix = 'foo'

for label in labels:
    print(prefix + prefix_sep + label)