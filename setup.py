import os
from setuptools import setup

def get_version():
    basedir = os.path.dirname(__file__)
    with open(os.path.join(basedir, 'rqweb/version.py')) as f:
        VERSION = None
        exec(f.read())
        return VERSION
    raise RuntimeError('No version info found.')

setup(
    name='rq-web',
    version=get_version(),
    url='https://github.com/nvie/rq-web/',
    license='BSD',
    author='Vincent Driessen',
    author_email='vincent@3rdcloud.com',
    description='rq-web is a general purpose, lightweight, web interface to '
                'monitor your RQ queues, jobs, and workers in realtime.',
    long_description=__doc__,
    packages=['rq-web'],
    include_package_data=True,
    zip_safe=False,
    platforms='any',
    install_requires=['rq'],
    scripts=['bin/rq-web'],
    classifiers=[
        # As from http://pypi.python.org/pypi?%3Aaction=list_classifiers
        #'Development Status :: 1 - Planning',
        'Development Status :: 2 - Pre-Alpha',
        #'Development Status :: 3 - Alpha',
        #'Development Status :: 4 - Beta',
        #'Development Status :: 5 - Production/Stable',
        #'Development Status :: 6 - Mature',
        #'Development Status :: 7 - Inactive',
        'Intended Audience :: Developers',
        'Intended Audience :: End Users/Desktop',
        'Intended Audience :: Information Technology',
        'Intended Audience :: Science/Research',
        'Intended Audience :: System Administrators',
        'License :: OSI Approved :: BSD License',
        'Operating System :: POSIX',
        'Operating System :: MacOS',
        'Operating System :: Unix',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Python Modules'
        'Topic :: Internet',
        'Topic :: Scientific/Engineering',
        'Topic :: System :: Distributed Computing',
        'Topic :: System :: Systems Administration',
        'Topic :: System :: Monitoring',
    ]
)

