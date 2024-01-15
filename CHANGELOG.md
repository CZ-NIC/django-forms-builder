# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added

- MANIFEST.in for build.
- Makefile for manage example site.
- Data dump data-forms.json for example site.
- Czech translations.
- Migrations 0004_alter_form_sites.py.
- Config for bumpversion.

### Fixed

- Translations de, es, fr, nb, nl, ru.

### Changed

- Rename the setup name to django-forms-builder-cod.
- Adjust code for isort, flake8, mypy, pydocstyle.
- Optimize code for Django > 3.2.
- Rewrite setup.py. Move version into setup.cfg.
- Move folder example_project outside from module forms_builder and rename to name example.
- Add tox.ini with test more python and django versions.

### Removed

- Support of Python < 3.9.
- Support of Django < 3.2.
- Compiled translations in .mo files.


## [0.16.0] - 2022-03-04

### Changed

- Add support of Django 3.2.

## [0.15.0] - 2021-03-03

### Changed

- Remove django-emails-extras.
- Add support of Django 3.0 and 3.1,
- Add DJANGO_VERSION 2.2.x into travis config.
- Make safe admin_links for Django 2.
- Change Django versions to >=1.11, < 2.2.99

## [0.8.0] - 2018-09-18

Last commit into the master ar repository https://github.com/stephenmcd/django-forms-builder


[Unreleased]: https://github.com/CZ-NIC/django-forms-builder/compare/0.16.0...master
[0.16.0]: https://github.com/CZ-NIC/django-forms-builder/compare/0.15.0...0.16.0
[0.15.0]: https://github.com/CZ-NIC/django-forms-builder/compare/0.8.0...0.15.0
[0.8.0]: https://github.com/CZ-NIC/django-forms-builder/compare/0.7.15...0.8.0
[0.7.15]: https://github.com/stephenmcd/django-forms-builder/releases/tag/0.7.15
