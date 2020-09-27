from setuptools import setup


setup(
    name='geospatial-tools',
    version='0.0.1',
    description='Geospatial analysis python package example for my portfolio',
    url='https://github.com/JeffreyLambert/geospatial-analysis-package',
    author='Jeffrey Lambert',
    author_email='jeffreyrlambert@gmail.com',
    licnese='MIT',
    packages=['geospatial'],
    install_requires=['requests', 'numpy'],
    python_requires='>=3.6.0'
)