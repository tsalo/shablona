import sys
import os.path as op
import versioneer
from io import open
from inspect import getfile, currentframe
from setuptools import setup, find_packages


def main():
    """ Install entry-point """
    ver_file = op.join('shablona', 'info.py')
    with open(ver_file) as f:
        exec(f.read())
    vars = locals()

    root_dir = op.dirname(op.abspath(getfile(currentframe())))

    version = None
    cmdclass = {}
    if op.isfile(op.join(root_dir, 'shablona', 'VERSION')):
        with open(op.join(root_dir, 'shablona', 'VERSION')) as vfile:
            version = vfile.readline().strip()

    if version is None:
        version = versioneer.get_version()
        cmdclass = versioneer.get_cmdclass()

    # Get version and release info, which is all stored in shablona/version.py
    ver_file = op.join('shablona', 'info.py')
    with open(ver_file) as f:
        exec(f.read())

    # Give setuptools a hint to complain if it's too old a version
    # 24.2.0 added the python_requires option
    # Should match pyproject.toml
    SETUP_REQUIRES = ['setuptools >= 24.2.0']
    # This enables setuptools to install wheel on-the-fly
    SETUP_REQUIRES += ['wheel'] if 'bdist_wheel' in sys.argv else []

    setup(
        name=vars['NAME'],
        maintainer=vars['MAINTAINER'],
        maintainer_email=vars['MAINTAINER_EMAIL'],
        description=vars['DESCRIPTION'],
        long_description=vars['LONG_DESCRIPTION'],
        url=vars['URL'],
        download_url=vars['DOWNLOAD_URL'],
        license=vars['LICENSE'],
        classifiers=vars['CLASSIFIERS'],
        author=vars['AUTHOR'],
        author_email=vars['AUTHOR_EMAIL'],
        platforms=vars['PLATFORMS'],
        version=vars['VERSION'],
        packages=find_packages(exclude=("tests",)),
        package_data=vars['PACKAGE_DATA'],
        install_requires=vars['REQUIRES'],
        python_requires=vars['PYTHON_REQUIRES'],
        setup_requires=SETUP_REQUIRES,
        requires=vars['REQUIRES'],
        extras_require=vars['EXTRA_REQUIRES'],
        zip_safe=False,
        cmdclass=cmdclass
    )


if __name__ == '__main__':
    main()
