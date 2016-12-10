# Append index at the end of the label, unless it is already there.
# Example:
# foo   -> foo 2
# foo 1 -> foo 1
# bar   -> bar 1

import re

indices = {}
has_index = []
cores = []

for label in labels:
    core, index = re.match( '(.*?)(\\d*)$', label).groups()
    core = core.strip()
    has_index.append(bool(index))
    cores.append(core)
    if core not in indices:
        indices[core] = set()
    if index:
        indices[core].add(int(index))

current_index = {core: 1 for core in indices}

for label, core, index_str in zip(labels, cores, has_index):
    if index_str:
        print(label)
    else:
        while current_index[core] in indices[core]:
            current_index[core] += 1
        print(core + ' ' + str(current_index[core]))
        current_index[core] += 1
