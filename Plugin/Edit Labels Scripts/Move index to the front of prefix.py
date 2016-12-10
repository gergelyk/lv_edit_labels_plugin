# Move index from the end of label to the end of prefix.
# Example:
# foo.bar 1 -> foo1.bar

import re

prefix_sep = '.'
index_sep = ''
strip_index = True

if strip_index:
    prepare = lambda s: s.strip()
else:
    prepare = lambda s: s
    
for label in labels:
    prefix, core, index = re.match( '([^\\' + prefix_sep +']*)(.*?)( *\\d*)$', label).groups()
    print(prefix + index_sep + prepare(index) + core)
