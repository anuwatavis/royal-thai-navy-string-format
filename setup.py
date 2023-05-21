from setuptools import find_packages, setup

with open("app/README.md", "r") as f:
    long_description = f.read()


setup(
    name="rtnf",
    version="1.0.0",
    description="Royal Thai Navy string format manipulation tools",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/anuwatavis/royal-thai-navy-string-format",
    author="anuwataravis",
    author_email="anuwat.avis@gmail.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.10",
        "Operating System :: OS Independent",
    ],
    keywords="rtnf royal thai navy string format",
    package_dir={"": "app"},
    packages=find_packages(where="app"),
    python_requires=">=3.8",
    install_requires=[],
    extras_require={
        "dev": ["twine>=4.0.2"],
    },
)
