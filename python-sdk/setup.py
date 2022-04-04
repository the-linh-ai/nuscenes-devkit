from setuptools import setup, find_packages


setup(
    name="nuscenes",
    version="1.0.0",
    author="nutonomy",
    packages=find_packages(),
    include_package_data=True,
    package_data={
        "": ["../README.md"],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
)
