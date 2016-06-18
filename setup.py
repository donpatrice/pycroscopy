from setuptools import setup, find_packages
from codecs import open
from os import path


here = path.abspath(path.dirname(__file__))
with open(path.join(here, 'README.md')) as f:
    long_description=f.read()

setup(
    name='pyCroscopy',
    version='0.0a1',
    description='A suite of Python libraries for high performance scientific computing of microscopy data.',
    long_description= long_description,
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Environment :: Console',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Cython',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: Implementation :: CPython',
        'Topic :: Scientific/Engineering :: Chemistry',
        'Topic :: Scientific / Engineering :: Information Analysis',
        'Topic :: Scientific/Engineering :: Physics',
        ],
    packages=find_packages(exclude='tests'),
    url='http://github.com/pycroscopy/pyCroscopy',
    license='MIT',
    author='S. Somnath, C. Ryan, N. Laanait',
    author_email='pycroscopy@gmail.com',
    dependency='',
    dependency_links=[''],
    install_requires=[''],
    test_suite='nose.collector',
    tests_require='Nose',
    include_package_data=True,

    # If there are data files included in your packages that need to be
    # installed, specify them here.  If using Python 2.6 or less, then these
    # have to be included in MANIFEST.in as well.
    # package_data={
    #     'sample': ['package_data.dat'],
    # },

    # Although 'package_data' is the preferred approach, in some case you may
    # need to place data files outside of your packages. See:
    # http://docs.python.org/3.4/distutils/setupscript.html#installing-additional-files # noqa
    # In this case, 'data_file' will be installed into '<sys.prefix>/my_data'
    # data_files=[('my_data', ['data/data_file'])],

    # To provide executable scripts, use entry points in preference to the
    # "scripts" keyword. Entry points provide cross-platform support and allow
    # pip to create the appropriate form of executable for the target platform.
    # entry_points={
    #     'console_scripts': [
    #         'sample=sample:main',
    #     ],
    # },
)
