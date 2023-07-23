from setuptools import setup, find_packages

DEV = ["pre-commit>=3.3.3"]
TEST = ["pytest>=7.4.0"]
setup(
    name="regex-validator",
    author="Aleksander Fidelus",
    author_email="alek.fidelus@gmail.com",
    packages=find_packages(),
    install_requires=["github-action-utils==1.1.0", "pydantic==2.0.3"],
    extras_require={"all": DEV + TEST, "dev": DEV, "test": TEST},
)
