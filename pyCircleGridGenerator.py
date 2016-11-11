# -*- coding: utf-8 -*-

import json
from reportlab.pdfgen import canvas
from reportlab.lib.units import mm

f = open('./param.txt', 'r')
json_data = json.load(f)

# load params from json file
outfile_name    = str(json_data["savefilepath"])
num_x           = int(json_data["num_x"])
num_y           = int(json_data["num_y"])
interval        = float(json_data["interval"])
radius          = interval * 0.4
string_offset   = float(json_data["stringoffset"])
grid_type       = int(json_data["gridType"])
paper_x         = int(json_data["paper_x"])
paper_y         = int(json_data["paper_y"])

pdfFile = canvas.Canvas(outfile_name)
pdfFile.saveState()

pdfFile.setPageSize((paper_x * mm, paper_y * mm)) 

strdata =  "interval=" + str(interval) + "mm, "
strdata += str(num_x) + "x" + str(num_y) + " grids"
pdfFile.drawString(string_offset * mm, string_offset * mm, strdata)

# align grids center
chart_len_x = interval * (num_x - 1) + radius * 1.5 
chart_len_y = interval * (num_y - 1) + radius 

offset_x =  ( paper_x - chart_len_x ) / 2.0
offset_y =  ( paper_y - chart_len_y ) / 2.0 

for nx in xrange(num_x):
    for ny in xrange(num_y):
        if ny % 2 == 0 and grid_type == 1:
            assym_offset = interval / 2.0
        else:
            assym_offset = 0

        center_x = interval * nx + offset_x + assym_offset
        center_y = interval * ny + offset_y

        pdfFile.circle(center_x * mm, center_y * mm, radius * mm, fill=1)

pdfFile.save()

f.close()