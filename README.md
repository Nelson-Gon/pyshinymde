# Our Project: What the project does 

[![PyPI version fury.io](https://badge.fury.io/our_project.svg)](https://pypi.python.org/pypi/our_project/)
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.3764453.svg)](https://doi.org/10.5281/zenodo.3764453)
[![Project Status](http://www.repostatus.org/badges/latest/active.svg)](http://www.repostatus.org/#active) 
[![Codecov](https://codecov.io/gh/Nelson-Gon/pytemplates/branch/main/graph/badge.svg)](https://codecov.io/gh/Nelson-Gon/pytemplates?branch=main)
![Test-Package](https://github.com/Nelson-Gon/pytemplates/workflows/Test-Package/badge.svg)
[![PyPI license](https://img.shields.io/pypi/l/our_project.svg)](https://pypi.python.org/pypi/our_project/)
[![Documentation Status](https://readthedocs.org/projects/pytemplates/badge/?version=latest)](https://pytemplates.readthedocs.io/en/latest/?badge=latest)
[![Total Downloads](https://pepy.tech/badge/our_project)](https://pepy.tech/project/our_project)
[![Monthly Downloads](https://pepy.tech/badge/our_project/month)](https://pepy.tech/project/our_project)
[![Weekly Downloads](https://pepy.tech/badge/our_project/week)](https://pepy.tech/project/our_project)
[![Maintenance](https://img.shields.io/badge/Maintained%3F-yes-green.svg)](https://GitHub.com/Nelson-Gon/pytemplates/graphs/commit-activity)
[![GitHub last commit](https://img.shields.io/github/last-commit/Nelson-Gon/pytemplates.svg)](https://github.com/Nelson-Gon/pytemplates/commits/main)
[![GitHub issues](https://img.shields.io/github/issues/Nelson-Gon/pytemplates.svg)](https://GitHub.com/Nelson-Gon/pytemplates/issues/)
[![GitHub issues-closed](https://img.shields.io/github/issues-closed/Nelson-Gon/pytemplates.svg)](https://GitHub.com/Nelson-Gon/pytemplates/issues?q=is%3Aissue+is%3Aclosed)


Welcome to `our_project`. 

**Please note that this is a template repository, click use template (do not fork unless suggesting an improvement) to use in a new project and edit files as required**. Also, see important notes at the end of this file. 

# Installation Guide

```shell
pip install our_project 
```

# Currently implemented features

`our_project` currently does the following:

- [x] Contains base class `HelloWorld` 

- [x] `HelloWorld` has the `print_text` method that prints user supplied text. 

- [x] A github action to test project installation and run tests.

- [x] A github action to release on PyPI (requires adding `PYPI_USERNAME` and `PYPI_PASSWORD` to repository secrets.)

# Features that need further attention 

We intend to work on the following in the future:

- [ ] Make it less cumbersome to init docs with `sphinx`. 


# Document generation 

Please edit `docs/source/index.rst` and `docs/source/modules.rst` as required then run:

```shell
./scripts/mkdocs.sh 

```

The above assumes you are at the root of "our_project". 

Also delete `setup.rst`, `tests.rst`, if they exist. 

Otherwise, run and edit as necessary.  

```shell
sphinx-quickstart
```

Thank you,

NelsonGon
22/10/2021 


---

# Important Notes 

This repository holds templates that follow a typical workflow for new `python` projects.

**A word of caution**

These templates are mostly intended to save time. However, modern IDEs provide project templates that are more mature and less opinionated than the templates here. 

This repository serves an additional purpose of allowing developers new to programming to study project structure using very simple examples. 

For licenses, tests, and workflows, gitignore it is recommended that one generates these automatically either from their IDE of choice or for `.gitignore` files and licenses, via github or gitlab. 

Happy to hear from you in case of any questions and/or feedback.

---

**DISCLAIMER**: 

This project is not in anyway related to a similarly named package [pytemplates](https://pypi.org/project/pytemplates/) that does something completely different ("Pytemplates is a lightweight HTML template engine written in Python, with support for template inheritance, blocks, macros, context, and Django.").

I only got to learn of this package upon adding badges to this file. 



