from setuptools import setup

import apidoc2markdown

def readme():
    try:
        with open("README.rst") as f:
            return f.read()
    except IOError:
        pass


setup(
    name="apidoc2markdown",
    version=apidoc2markdown.__version__,
    url="https://github.com/moigagoo/apidoc2markdown",
    download_url="https://pypi.org/project/apidoc2markdown",
    license="MIT",
    author="Konstantin Molchanov",
    author_email="moigagoo@live.com",
    description="Converter from Apidoc JSON to Markdown.",
    long_description=readme(),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Environment :: Console",
        "Environment :: Web Environment",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Topic :: Documentation",
        "Topic :: Utilities",
    ],
    py_modules=["apidoc2markdown.apidoc2markdown"],
    packages=["apidoc2markdown"],
    package_dir={"apidoc2markdown": "."},
    package_data={"apidoc2markdown": ["apidoc.md.j2"]},
    platforms="any",
    install_requires=["Jinja2"],
    entry_points={
        "console_scripts": [
            "apidoc2markdown=apidoc2markdown.apidoc2markdown:main"
        ]
    }
)
