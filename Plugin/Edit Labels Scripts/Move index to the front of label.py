# Move index from the end of prefix to the end of label.
# Example:
# foo1.bar -> foo.bar 1

import re

prefix_sep = '.'
index_sep = ' '
strip_index = True

if strip_index:
    prepare = lambda s: s.strip()
else:
    prepare = lambda s: s
    
for label in labels:
    m = re.match( '([^\\' + prefix_sep +']*)(\\' + prefix_sep + '.*?)$', label)
    if m:
        pref_idx, core = m.groups()
        pref, index = re.match('(.*?)( *\\d*)$', pref_idx).groups()
        if index:
            print(pref + core + index_sep + prepare(index))
        else:
            print(label)
    else:
        print(label)
