from setuptools import setup

setup(
    name='whatshere',
    version='1.0.0',
    packages=['whatshere'],
    entry_points={
        'console_scripts': [
            'whatshere = whatshere.__main__:main',
        ],
    },
    author='Wazazky',
    description='Genera un archivo lista_archivos.txt con todos los archivos visibles del proyecto',
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    url='https://github.com/wazazky/whatshere',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: Microsoft :: Windows',
    ],
    python_requires='>=3.6',
)
