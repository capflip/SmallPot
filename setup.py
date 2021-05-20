from setuptools import setup


def readme_file_contents():
    with open('README.rst') as readme_file:
        data = readme_file.read()
    return data


setup(
    name='smallpot',
    version='1.0.0',
    description='Simple TCP honeypot based off of DevDungeon NanoPot tutorial',
    long_description=readme_file_contents(),
    author='capflip',
    author_email='',
    license='MIT',
    packages=['smallpot'],
    zip_safe=False,
    install_requires=[]
)
