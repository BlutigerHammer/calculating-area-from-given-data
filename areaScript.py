# -*- coding: utf-8-*-

'''
comentario
'''

import sys
import codecs
import json
import argparse
# Add path to the folder with your modules. Use sys.append

from pathlib import Path
# import area counting function from your module
# from ....

from matplotlib import pyplot as plt
import jinja2
import datetime

description = '''
Create a description of how your script works
'''

#--------------------------------------------------------------------------------------------

def parserFunction():
	'''Function parsing command line arguments'''
	parser = argparse.ArgumentParser(description = description)

	# Add arguments to your module: mandatory, i.e. positional and optional i.e.
	# parser.add_argument('someArg, 	type=str,	help=u'''help text''')


	args = parser.parse_args()
	return args

#--------------------------------------------------------------------------------------------

def validArgs(args):
	'''validates file addresses and other arguments, for example:
	args.someAddres = Path(args.someAddres).resolve()
	'''

	return args

#--------------------------------------------------------------------------------------------

def readData(path):
	# Write a code to read the data from the file

	return data

#--------------------------------------------------------------------------------------------

def makeFigure(xy,name,ax,color):
	'''	Bonus:
		This function creates a single chart.
		Args:
			-xx:     coordinates of a single polygon
			- name:  name / label of a single polygon
			- ax:    matplotlib object (check in class materials)
			- color: what color should the polygon points plot be

	'''
	x,y = zip(*xy)
	labels = list(range(1,len(xy)+1))
	ax.plot(x,y,'.',c=color)
	#for i,no in enumerate(labels):
		#ax.annotate(no,(x[i],y[i]))
	ax.set_title(f"Polygon '{name}'.")
	ax.set_yticklabels([])
	ax.set_xticklabels([])
	ax.axis('off')


#--------------------------------------------------------------------------------------------

def createReport(head,results):
	''' Creates a report.
		Args:
			- head:     dictionary, data type general, author
			- results:  dictionary, like {'no': training ground number, 'label': training ground label, 'area': calculated area}

		Returns:
			ready report, html file
	'''

	# create template loader, Environment, template
	# complete (render) the template

	return report


#--------------------------------------------------------------------------------------------


if __name__ == '__main__':

	#... load command line arguments .............
	args = parserFunction()
	args = validArgs(args)

	#... load point coordinates ..................
	data = readData(data file address)

	#... calculate the area of polygons ..........
	# data - it should be a dictionary, you can iterate over it
	# item is a key: value pair
	# enumerate(): look here https://book.pythontips.com/en/latest/enumerate.html
	results = []
	for i,(kl,val) in enumerate(data.items(),1):
		results.append({'no': i, 'label': kl, 'area': areanp(val)})


	# bonus!!
	#... create polygon charts ...................
	# k - black, b - blue, g - green, r -red
	color = ['k','b', 'g', 'r', 'k', 'g']
	fig, ax = plt.subplots(2,3,figsize=(6, 6))
	ax = ax.ravel()
	for i,(kl,val) in enumerate(data.items()):
		makeFigure(val,kl,ax[i],color[i])
	# tight_layout automatically adjusts subplot params so that the subplot(s) fits in to the figure area.
	#This is an experimental feature and may not work for some cases. It only checks the extents of ticklabels, axis labels, and titles.
	plt.tight_layout()
	plt.savefig(args.figAdd,dpi=fig.dpi)



	#... create a report ........................
	#    get current date - second bonus :)
	date = datetime.datetime.now()
	date = date.strftime('%Y.%m.%d')

	#    create a header dictionary with general data
	#    date, title, author, department, img address

	report = createReport(head=header,results=results)

	# ... save the report file to disk ...........
	with codecs.open(....

	print(f'\nReport saved to file {insert variable - report file address}.\n')


	# !! end :)
