
from setuptools import setup, find_packages

setup(
    name="futures",
    description="Deep learning based financial modeling",
    author="Junyoung Sim",
    author_email="eden920.dev@gmail.com",
    url="https://github.com/junyoung-sim/futures/",
    python_requires=">=3.8",
    scripts=["futures.py"],
    packages=find_packages(),
)
