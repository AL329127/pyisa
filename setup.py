import setuptools


with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pyisa",
    version="1.0",
    author="Sagar Dawda",
    author_email="sagard21@gmail.com",
    description="Basic project structure creation for Data Science Projects",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/sagard21/pyisa",
    packages=setuptools.find_packages(),
    license="MIT License",
    classifiers=[
        "Programming Language :: Python :: 2.7",
        "Operating System :: OS Independent",
    ],
)


