from setuptools import setup, find_packages

setup(
    name='CubeCAD',

    version="0.1",

    description='Cube-oriented CAD system.',

    long_description="""
    """,

    classifiers=[
    ],

    author='Matthew R. Scott',

    author_email='gldnspud@gmail.com',

    url='http://github.com/gldnspud/cubecad/',

    install_requires=[
    'Schevo == dev, >= 3.1a2dev-20090112',
    ],

    tests_require=[
    'nose >= 0.10.4',
    ],

    test_suite='nose.collector',

    extras_require={
    },

    dependency_links=[
    ],

    packages=find_packages(),

    include_package_data=True,

    package_data={},

    entry_points="""
    """,
    )
