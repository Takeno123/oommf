# -*- coding: utf-8 -*-
"""
Created on Tue Jul 16 09:36:14 2019

@author: 15t50
"""

import subprocess
import os

path_oommf = r'absolute path of oommf.tcl'
mif_file = os.path.abspath('../examples/squarecubic_scripted.mif')

sizes = [100,200,300,400]

for size in sizes:
    oommf_string = 'tclsh' + ' ' + path_oommf + ' boxsi -parameters \"xsize %s ysize %s\" -- %s' % (size, size, mif_file)
    print (oommf_string)
    subprocess.call(oommf_string,shell=True)