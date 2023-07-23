from setuptools import setup, find_packages

setup(
    name="regex-validator",
    author="Aleksander Fidelus",
    author_email="alek.fidelus@gmail.com",
    packages=find_packages(),
    install_requires=["github-action-utils==1.1.0"],
    extras_require={"dev": ["pre-commit>=3.3.3"], "test": ["pytest>=7.4.0"]},
)
