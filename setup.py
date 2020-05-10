import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="github-file-downloader", # Replace with your own username
    version="1.0.3",
    author="Abhishek Kushwaha",
    author_email="thecrazycoderabhi@gmail.com",
    description="A small cli based utility, to download individual files from public repos in Github",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/abhishekkushwaha4u/Github-Cli-File-Downloader",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)