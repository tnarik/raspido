#!/usr/bin/env python
from distutils.core import setup

scripts=['simpledod', 'door_opener']

setup(name='simpledod',
      version='0.1',
      description='Simple daemon to keep control of a rfid door',
      author='David Francos Cuartero (XayOn)',
      author_email='xayon@davidfrancos.net',
      url='http://github.com/TheOtherNet/SimpleDO',
      download_url='http://github.com/TheOtherNet/SimpleDO',
      license='GPL2',
      classifiers=[
          'Development Status :: 5 - Production/Stable',
          'Environment :: Console',
      ],
      mantainer='David Francos Cuartero (XayOn)',
      mantainer_email='dfrancos@theothernet.co.uk',
      long_description="Simple daemon to keep control of a rfid door,"+
      "using a mysql db and a rfid HID",
      scripts=scripts,
     )
