from distutils.core import setup
setup(
  name = 'nbgit',
  packages = ['nbgit'],
  version = '0.0.0.1',
  description = 'Lanuches and manages F250 biweekly/daily runs',
  author = 'Brookie Guzder-Williams',
  author_email = 'brook.williams@gmail.com',
  url = 'https://github.com/brookisme/nbgit',
  download_url = 'https://github.com/brookisme/nbgit/tarball/0.1',
  keywords = ['ipython', 'notebook','git'],
  classifiers = [],
  entry_points={
      'console_scripts': [
          'nbgit=nbgit:main',
      ],
  }
)