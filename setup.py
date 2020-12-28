from setuptools import setup
import glob
import re


VERSION_FILE_PATH = 'concrete/version.py'
VERSION_RE = re.compile(
    r'^__version__ = (?P<quote>[\'"])(?P<version>[0-9]+\.[0-9]+\.[0-9]+(?:\.dev[0-9]+)?)(?P=quote)$'
)


with open("README.rst", "r", encoding="utf-8") as fh:
    long_description = fh.read()


def get_version():
    with open(VERSION_FILE_PATH) as f:
        for line in f:
            m = VERSION_RE.match(line.rstrip())
            if m is not None:
                return m.group('version')
    raise Exception('unable to determine version from %s' % VERSION_FILE_PATH)


if __name__ == '__main__':
    setup(
        name="concrete",
        version=get_version(),
        description="Python modules and scripts for working with Concrete",
        long_description=long_description,

        packages=[
            'concrete',

            # Python code generated by Thrift Compiler
            'concrete.access',
            'concrete.annotate',
            'concrete.audio',
            'concrete.clustering',
            'concrete.communication',
            'concrete.context',
            'concrete.email',
            'concrete.entities',
            'concrete.exceptions',
            'concrete.language',
            'concrete.learn',
            'concrete.linking',
            'concrete.metadata',
            'concrete.nitf',
            'concrete.search',
            'concrete.services',
            'concrete.services.results',
            'concrete.situations',
            'concrete.spans',
            'concrete.structure',
            'concrete.summarization',
            'concrete.twitter',
            'concrete.uuid',

            # Python code generated by people
            'concrete.util',
        ],

        scripts=glob.glob('scripts/*.py')
                  + glob.glob('concrete/services/*-remote'),

        install_requires=[
            'boto',
            'bottle',
            'humanfriendly',
            'networkx',
            'thrift==0.11.0',
            'redis>=2.10.0',
            'pycountry>=17.9.23',
            'requests',
        ],

        url="https://github.com/hltcoe/concrete-python",
        classifiers=[
            'Development Status :: 4 - Beta',
            #'Development Status :: 5 - Production/Stable',
            'Environment :: Console',
            'Environment :: No Input/Output (Daemon)',
            'Intended Audience :: Developers',
            'Intended Audience :: Education',
            'Intended Audience :: Science/Research',
            'License :: OSI Approved :: BSD License',
            'Natural Language :: English',
            'Operating System :: MacOS :: MacOS X',
            'Operating System :: Microsoft :: Windows',
            'Operating System :: POSIX :: Linux',
            'Programming Language :: Python :: 3.5',
            'Programming Language :: Python :: 3.6',
            'Programming Language :: Python :: 3.7',
            'Programming Language :: Python :: 3.8',
            'Programming Language :: Python :: 3.9',
            'Programming Language :: Python :: 3 :: Only',
            'Topic :: Database :: Front-Ends',
            'Topic :: Multimedia :: Sound/Audio :: Speech',
            'Topic :: Scientific/Engineering :: Artificial Intelligence',
            'Topic :: Scientific/Engineering :: Interface Engine/Protocol Translator',
            'Topic :: Text Processing :: Linguistic',
            'Topic :: Utilities',
        ],
    )
