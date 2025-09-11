from setuptools import setup, find_packages

setup(
    name='PyGameRules',
    version='0.1.0',
    author='AdanCR1',
    author_email='your_email@example.com',
    description='A library for managing counters, timers, and game states compatible with Pygame.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/yourusername/PyGameRules',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
    install_requires=[
        'pygame',
    ],
)