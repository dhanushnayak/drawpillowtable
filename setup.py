import pathlib
from setuptools import setup, find_packages

HERE = pathlib.Path(__file__).parent

README = (HERE / "README.md").read_text()

setup(
    name='pillowdrawtable',
    version='0.1.4.1',
    license='MIT',
    description="Draw a table in pillow image",
    long_description=README,
    long_description_content_type='text/markdown',
    author="Dhanush Nayak",
    author_email='dhanushnayak.pythonnotebook@gmail.com',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    python_requires='>=3.6',
    url='https://github.com/dhanushnayak/drawpillowtable',
    keywords='Pillow,Table',
    install_requires=[
          'Pillow==9.0.1',
      ],

)