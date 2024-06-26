import matplotlib.pyplot as plt

def rainbowprint(input_string,cmap_name='cool'):
	"""Prints a string with a color gradient.
	
	Args:
		input_string (:obj:`str`): The string to be printed.
		cmap_name (:obj:`str`, optional): Matplotlib map to use (default: `cool`).
	
	Returns:
		None

  	Raises:
   		TypeError: if `input_string` is not a string.
	
	"""
	try: # catch incorrect map names:
		colormap = plt.get_cmap(cmap_name)
	except:
		colormap = plt.get_cmap('cool')
	
	NNN = len(input_string)
	# no coloring if len==1 or less:
	if NNN<2:
		print(input_string)
		return None
	
	colored_string = ''
	for iii,char in enumerate(input_string):
		rgb_tuple =  colormap(iii/(NNN-1))
		r_val = int(255*rgb_tuple[0])
		g_val = int(255*rgb_tuple[1])
		b_val = int(255*rgb_tuple[2])
		prefix = '\033[38;2;%i;%i;%im' % (r_val,g_val,b_val)
		colored_char = prefix+char
		colored_string += colored_char
		
	print(colored_string+'\033[0m')
	return None
