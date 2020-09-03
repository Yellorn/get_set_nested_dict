import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="get_set_nested_dict",
    version="0.1.0",
    author="Hoang Yell",
    author_email="ngohoang.yell@gmail.com",
    description="Get or Set a nested value of nested dict by path",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ngohoangyell/get_set_nested_dict",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.0',
)
