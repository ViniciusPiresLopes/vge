from setuptools import setup, find_packages


with open("README.md", "r") as readme_file:
    long_description = readme_file.read()


setup(
    name="vge",
    version="0.1",
    description="VGE (Vini Game Engine) is a 2D game engine made with pygame. It supports Scene and Nodes, each node with its facility.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Vinícius Pire Lopes",
    license="MIT",
    keywords="2D pygame game engine",
    packages=find_packages(),
    install_requires=["pygame>=1.9.6"],
    python_requires="~=3.6",
)