from setuptools import find_packages, setup

setup(
    name="your_package_name",  # Replace with your package name
    version="0.1.0",  # Replace with the initial version
    author="Your Name",  # Replace with the author's name
    author_email="your_email@example.com",  # Replace with the author's email
    description="A brief description of the package",  # Replace with a short description
    long_description=open("README.md").read(),  # Assumes you have a README.md file
    long_description_content_type="text/markdown",
    url="https://github.com/asynckeel-max/asynckeel",  # Replace with the URL of the project
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",  # Replace with the appropriate license
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",  # Replace with the required Python version
    install_requires=[
        "dependency1",  # Replace with your package dependencies
        "dependency2",  # Replace with your package dependencies
    ],
)
