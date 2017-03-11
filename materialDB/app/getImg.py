def simple():
	import matplotlib.pyplot as plt
	import numpy as np
	import base64
	from io import BytesIO
	
	### Generating X,Y coordinaltes to be used in plot
	X = np.arange(0,100,5)
	Y = X*X
	### Generating The Plot
	plt.plot(X,Y)
	### Saving plot to disk in png format
	#plt.savefig('/home/AnandSatya/mysite/square_plot.png')


	### Rendering Plot in Html
	figfile = BytesIO()
	plt.savefig(figfile, format='png')
	figfile.seek(0)
	figdata_png = base64.b64encode(figfile.getvalue())
	#print figdata_png
	return figdata_png

if __name__=="__main__":
	simple()
