import setuptools

def readme():
    try:
        with open('README.md') as f:
            return f.read()
    except IOError:
        return ''
    
setuptools.setup(
    name="Domoji",
    version="1.1",
    author="Max Bridgland",
    install_requires=[
        'requests==2.21.0',
        'terminaltables==3.1.0',
        'crayons==0.2.0',
        'colorama==0.4.1'
    ],
    author_email="mabridgland@protonmail.com",
    description="Find Emoji Domains From The Command Line (Works on MacOS and Terminals That Accept Emojis",
    long_description=readme(),
    long_description_content_type="text/markdown",
    entry_points = {
        'console_scripts': [
            'domoji = domoji.__main__:menu'
        ]
    },
    keywords="domains, api, wrapper, emoji, emojicode, macOS",
    url="https://github.com/M4cs/Domoji",
    packages=setuptools.find_packages(),
    classifiers=(
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Topic :: Multimedia :: Graphics"
    ),
)
