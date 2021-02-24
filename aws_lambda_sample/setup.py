from setuptools import find_packages, setup  # type: ignore

setup(
    name="aws_lambda",
    version="0.0.0",
    packages=find_packages(),
    package_data={
        "aws_lambda": ["py.typed"],
    },
)
