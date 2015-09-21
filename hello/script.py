#!/usr/bin/python
import sys
parts= (sys.argv[1]).split("/")
apiLink=parts[0]+"//api."+parts[2]+"/repos/"+("/".join(parts[3:]))
import shipy
shipy.getDays(apiLink)
