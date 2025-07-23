from setuptools import find_packages, setup

with open("README.md", "r", encoding="utf-8") as readme_file:
    long_description = readme_file.read()

setup(
    name="n2yo-api-wrapper",
    version="0.0.2",
    description="Unofficial Wrapper for N2YO.com API",
    author="Giampy",
    author_email="g1ampy@proton.me",
    packages=find_packages(),
    url="https://github.com/g1ampy/n2yo-api-wrapper",
    python_requires=">=3.10",
    install_requires=["requests", "dacite", "beautifulsoup4"],
    long_description=long_description,
    long_description_content_type="text/markdown",
    license="MIT",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Programming Language :: Python",
        "Operating System :: OS Independent",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
)
