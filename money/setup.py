from setuptools import setup

setup(
	name='money',
	version='0.1',
	py_modules=['money'],
	install_requires=[
	    'Click',
	],
	entry_points='''
	    [console_scripts]
	    money=money:cli
	''',
)
