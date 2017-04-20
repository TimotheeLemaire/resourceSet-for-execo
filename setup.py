from distutils.core import setup
setup(
  name = 'resourceSet_for_execo',
  packages = find_packages(exclude=['testing', 'docs', 'UML']), # this must be the same as the name above
  version = '0.1',
  description = 'resourceSet for http://execo.gforge.inria.fr/doc/latest-stable/ | School project at Polytech Grenoble : http://air.imag.fr/index.php/ExperimentControl',
  author = 'Timothee Lemaire and Nicolas Homberg',
  author_email = 'nshg117@gmail.com',
  url = 'https://github.com/TimotheeLemaire/resourceSet_for_execo', # use the URL to the github repo
  download_url = 'https://github.com/peterldowns/mypackage/archive/0.1.tar.gz', # I'll explain this in a second
  keywords = ['testing', 'logging', 'Execo','grid5000','tak tuk'], # arbitrary keywords
  classifiers = [],
)

