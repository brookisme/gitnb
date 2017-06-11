from distutils.core import setup
setup(
  name = 'gitnb',
  packages = ['gitnb'],
  version = '0.0.1.7',
  description = 'Git Tracking for Python Notebooks',
  author = 'Brookie Guzder-Williams',
  author_email = 'brook.williams@gmail.com',
  url = 'https://github.com/brookisme/gitnb',
  download_url = 'https://github.com/brookisme/gitnb/tarball/0.1',
  keywords = ['ipython', 'notebook','git'],
  include_package_data=True,
  data_files=[
    ('config',[
        'gitnb/default.config.yaml',
        'gitnb/dot_gitnb/notebooks',
        'gitnb/dot_gitnb/precommit',
        'gitnb/dot_gitnb/default_gitignore'
      ]
    )
  ],
  classifiers = [],
  entry_points={
      'console_scripts': [
          'gitnb=gitnb:main',
      ],
  }
)