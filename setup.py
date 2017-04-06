from setuptools import setup

setup(name='tw_predict',
      version='0.1',
      description='Hopefully one day a functioning predictive framebork',
      url='http://github.com/storborg/tw-project',
      author='Matt Kelsh',
      author_email='mdkelsh@gmail.com',
      install_requires=[
          'textblob',
          'tweepy',
      ],
      zip_safe=False)