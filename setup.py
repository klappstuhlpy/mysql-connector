from setuptools import setup

with open('README.md') as fp:
    long_description = fp.read()

setup(
    name='mysql-connector',
    version='0.0.1',
    url='https://github.com/klappstuhlpy/mysql-connector',
    project_urls={
        'Source': 'https://github.com/klappstuhlpy/mysql-connector',
        'Support': 'https://claude-bot.de/',
        'Issue Tracker': 'https://github.com/klappstuhlpy/mysql-connector/issues'
    },
    license='MIT',
    description='A custom mysql connector package for easy to handle mysql databases.',
    long_description=long_description,
    author='klappstuhlpy',
    author_email='info@claude-bot.de',
    include_package_data=True,
    packages=['mysql-connector'],
    classifiers=[
        'Development Status :: 4 - Beta',
        'License :: OSI Approved :: MIT License',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Topic :: Printing',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Utilities',
        'Typing :: Typed'
    ]
)
