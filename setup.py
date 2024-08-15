from setuptools import setup, find_packages

with open('requirements.txt') as f:
    requirements = f.read().splitlines()

setup(
    name="searchbot",
    version="1.0.0",
    author="xialeistudio",
    author_email="xialeistudio@gmail.com",
    description="An AI-powered information retrieval assistant helps users answer questions based on provided context. ",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/xialeistudio/SearchBot",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    install_requires=requirements,
    entry_points={
        'console_scripts': [
            'search-bot=cli:main',
        ],
    },
)
