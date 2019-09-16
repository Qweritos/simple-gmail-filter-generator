#!/usr/bin/env python

import sys

unimportant_label = "Неважное"

atom = """<?xml version='1.0' encoding='UTF-8'?><feed xmlns='http://www.w3.org/2005/Atom' 
xmlns:apps='http://schemas.google.com/apps/2006'>
	<title>Mail Filters</title>
	<author>
		<name>Андрей А.</name>
		<email>qweritos@gmail.com</email>
	</author>
"""

label = "Misc"
for line in sys.stdin:
  li = line.strip()
  if li.startswith("#"):
    label = li[1:].strip()
  else:
    if line.strip():
      atom += """<entry>
	<category term='filter'></category>
	<title>Mail Filter</title>
	<content></content>
	<apps:property name='from' value='{}'/>
	<apps:property name='label' value='{}'/>
	<apps:property name='sizeOperator' value='s_sl'/>
        <apps:property name="shouldMarkAsRead" value="true"/>
	<apps:property name='sizeUnit' value='s_smb'/>
</entry>
""".format(line.strip(), unimportant_label)


atom += "</feed>"

print(atom)
