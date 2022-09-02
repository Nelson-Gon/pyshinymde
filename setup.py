from pyshinymde.version import __version__
from setuptools import setup, find_packages
import os
# Change project to project name here
# Choose relevant license as required, add necessary install_requires
# Automate the process of reading from requirements.txt
install_requires_list = []
reqs_file = os.path.join(os.path.dirname(
    os.path.abspath(__file__)), "requirements.txt")
with open(reqs_file, "r") as input_file:
    for line in input_file:
        # rstrip to remove the newline character after appending to an empty list.
        install_requires_list.append(line.rstrip())
install_requires_list.append(
    "shiny @ git+https://github.com/rstudio/py-shiny.git@816846d377c2e4973c8b4fde81f88ad3600a2d80#egg=shiny")

print(install_requires_list)
link_to_use = "https://github.com/Nelson-Gon/pyshinymde/archive/refs/tags/v" + \
    __version__+".zip"
setup(name='project',
      version=__version__,
      description="Python Citations Generator",
      url="http://www.github.com/Nelson-Gon/pyshinymde",
      download_url=link_to_use,
      author='Nelson Gonzabato',
      author_email='gonzabato@hotmail.com',
      license='MIT',
      keywords="web html academics citation science",
      packages=find_packages(),
      long_description=open('README.md', encoding="utf-8").read(),
      long_description_content_type='text/markdown',
      install_requires=install_requires_list,
      python_requires='>=3.6',
      zip_safe=False)
