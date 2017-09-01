from distutils.core import setup

setup(
    name='bancocentralbrasil',
    version='1.1.0',
    author='Leonardo Gregianin',
    author_email='leogregianin@gmail.com',
    scripts=['bancocentral.py', 'test_bancocentral.py', 'sample.py', 'README.md', 'LICENSE'],
    url='https://github.com/leogregianin/bancocentralbrasil',
    license='LICENSE',
    description='Selic Rate, Inflation and Dollar Exchange from Brazil',
    platforms = 'any',
    classifiers = [
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Development Status :: 4 - Beta',
        'Natural Language :: English',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ],	
)