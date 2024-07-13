import setuptools

setuptools.setup(
    name='fruceapi',
    version='0.1',
    description='Module for Fruitspace interaction',
    author='nosleep, kot_v_palto',
    packages=['FruceAPI'],
    requires=['aiohttp', 'zlib'],
)