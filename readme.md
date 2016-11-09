# pyCircleGridGenerator
OpenCV acceptable arbitrary circle grid calibration chart generator.

## Requirement
- Python2.7.x
- reportlab
```bash
pip install reportlab
```
## Configure
- write parameters to param.txt in JSON format.
```JSON
{
	"savefilepath":			"./smallCalibChart.pdf",

	"#comment":			"Set the paper size in [mm] as integer. (cf. A4: 297mm x 210mm)",
	"paper_x":			297,
	"paper_y":			210,
	
	"#comment":			"Set num of circles.",
	"num_x":			8,
	"num_y":			5,

	"#comment":			"Set interval in [mm]",
	"interval":			30,

	"#comment":			"0: symmetry circle Grid, 1: assymentry circle grid",
	"gridType":			"1",

	"#comment":			"If strings overlap on the circle, change this offset param[mm]",
	"stringoffset":			20
	}
```

## Run
- set param.txt
- run command below: 
```bash
$python circleGridGenerator.py
```