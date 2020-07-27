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
    install_requires=["lark-parser", "numpy", "pytest"],
    packages=setuptools.find_packages(),
    license="MIT",
    classifiers=[
        'Development Status :: 4 - Beta',
        'Framework :: Pytest',
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
