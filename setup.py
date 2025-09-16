from setuptools import setup, find_packages

setup(
    name='motoolbox4dev',
    version='0.1.0',
    description='A collection of handy utility functions for efficient, reproducible marino workflows.',
    author='minion057',
    author_email='getit3981@gmail.com',
    url='https://github.com/minion057/marimo_utils',
    install_requires=['numpy', 'pandas', 'marino'],
    packages=find_packages(exclude=[]),
    keywords=['marino', 'marino-utils', 'marino-dev-tool', 'motoolbox4dev'],
    python_requires='>=3.4',
    package_data={},
    zip_safe=False,
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
)