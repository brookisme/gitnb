from distutils.core import setup
setup(
  name = 'nb_git',
  packages = ['nb_git'],
  version = '0.0.0.6',
  description = 'Git Tracking for Python Notebooks',
  author = 'Brookie Guzder-Williams',
  author_email = 'brook.williams@gmail.com',
  url = 'https://github.com/brookisme/nb_git',
  download_url = 'https://github.com/brookisme/nb_git/tarball/0.1',
  keywords = ['ipython', 'notebook','git'],
  include_package_data=True,
  data_files=[('config',['nb_git/default.config.yaml','nb_git/dot_nb_git/*'])],
  classifiers = [],
  entry_points={
      'console_scripts': [
          'nb_git=nb_git:main',
      ],
  }
)