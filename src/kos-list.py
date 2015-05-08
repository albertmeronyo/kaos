#!/usr/bin/env python

# KOS list generator

from os import walk

kos_path = "../kos/"
kos_exceptions = [ "ConceptDrift-data/src/common",
                   "ConceptDrift-data/src",
                   "ConceptDrift-data"
               ]
table_output = unicode()
table_output += '<table class="table table-condensed table-hover">'
table_output += '<tr><td><b>KOS name</b></td><td><b>Download</b></td></tr>'

for (dirpath, dirnames, filenames) in walk(kos_path):
    norm_dirpath = dirpath.split(kos_path)[-1]
    if filenames and norm_dirpath not in kos_exceptions:
        print norm_dirpath
        print filenames
        table_output += '<tr><td>' + norm_dirpath + '</td><td><a href="kos/' + norm_dirpath  +'">List files</a></td></tr>'

table_output += '</table>'

print table_output
