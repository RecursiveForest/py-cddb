#!/usr/bin/env python

"""Setup script for the CDDB module distribution."""

__revision__ = "$Id: setup.py,v 1.5 2003/08/31 23:19:11 che_fox Exp $"

from distutils.core import setup, Extension

setup (# Distribution meta-data
       name = "CDDB",
       version = "1.4",
       description = "Module for retrieving track information about audio CDs from CDDB",
       author = "Ben Gertzfield",
       author_email = "che@debian.org",
       url = "http://cddb-py.sourceforge.net/",

       # Description of the modules and packages in the distribution
       py_modules = ['CDDB', 'DiscID'],
       ext_modules = [ Extension('cdrom', ['unix/cdrommodule.c']) ]
      )
