import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="uon-parser",
    version="0.0.1",
    author="Stephane Selim",
    author_email="stephane.selim@heig-vd.ch",
    description="A uon parser package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/uon-language/uon-parser",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
