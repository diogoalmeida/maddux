from distutils.core import setup

setup(
    name='maddux',
    version='0.1.0',
    author='Ben Caine & Colin Kohler',
    author_email='',
    packages=['maddux', 'maddux.examples', 'maddux.objects', 'maddux.robots', 'maddux.utils'],
    scripts=[],
    url='http://bencaine.me/maddux/overview.html',
    license='LICENSE',
    description='Maddux package.',
    long_description=open('README.md').read(),
    install_requires=[
        "numpy >= 1.14.3",
        "matplotlib >= 1.3.1",
    ],
)
