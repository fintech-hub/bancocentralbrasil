from setuptools import setup, find_packages

setup(
    name='bancocentralbrasil',
    version='1.2.0',
    url='https://github.com/leogregianin/bancocentralbrasil',
    license='LICENSE',
    author='Leonardo Gregianin',
    author_email='leogregianin@gmail.com',
    keywords='dolar money bancocentralbrasil tax brasil',
    description='Selic Rate, Inflation and Dollar Exchange from Brazil',
    packages=find_packages(),
    platforms='any',
    classifiers=[
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Development Status :: 5 - Production/Stable',
        'Natural Language :: English',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ],
    install_requires=[],
    test_suite='test',
)
