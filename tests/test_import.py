def test1():
	try:
		from rainbowprint.functions import rainbowprint
		passed = True
	except ImportError:
		passed = False
	assert passed