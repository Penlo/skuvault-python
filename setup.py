from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name='skuvault',
    packages=find_packages(include=['skuvault', 'skuvault.*']),
    version='1.1.2',
    description='A Python library for the SkuVault API',
    author='Nathan Head',
    author_email="headn90@gmail.com",
    license='MIT',
    url="https://github.com/Penlo/skuvault-python",
    project_urls={
        "Bug Tracker": "https://github.com/Penlo/skuvault-python/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
