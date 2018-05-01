from setuptools import setup
import sys
from MozDir import (
    __author__,
    __app__,
    __version__,
    __release__,
)

# validation
if sys.version_info < (3, 4):
    print("Building mozdir requires at least Python 3.4 to run.")
    sys.exit(1)

setup(name=__app__,
      version= "{}.{}".format(__version__, __release__),
      description='mozer directory tool',
      long_description="""this supports to mozer.""",
      author=__author__,
      packages=[
          'MozDir' # __init__.pyを置いてあるので、これでモジュール化できる
          ],
      py_modules=[
          # 上記のpackagesで収まるので、特に使わない
          ],
      zip_safe = (sys.version>="2.5"), #2.5の頃はディレクトリとしてegg作らないとまずかった？
      scripts=[
          'bin/mozdir'
          ],
      license='MIT',
      keywords='',
      platforms='MacOS',
      )
