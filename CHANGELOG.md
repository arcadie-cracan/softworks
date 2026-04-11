# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Fixed

- SKILL uses Virtue’s global `Import` table again so Softworks matches **virtue-skill** from PyPI (0.4.x), which defines `Import` but not `VrtImport` (the latter exists on Virtue GitHub `master` only).

## [0.4.0] - 2023-02-10

### Fixed

- New view gui fix to the default view name
- Update to support latest version of Virtue

## [0.3.0] - 2022-08-18

### Added

- VS Code workspace setup
- Cadence library for testing

## [0.2.0] - 2022-08-15

### Added

- Add Virtue Python plugins to support softworks in a Virtue SKILL environment

## [0.1.0] - 2022-08-13

### Added

- Initial release with basic functionality
- Support for html views
- Support for pdf views
- Support for pptx views
- Support for python views incling markdown, toml, and yaml views
- Support for skill views
- Support for Excel views

[unreleased]: https://github.com/cascode-labs/softworks/compare/v0.4.0...HEAD
[0.4.0]: https://github.com/cascode-labs/softworks/compare/v1.3.0...v0.4.0
[0.3.0]: https://github.com/cascode-labs/softworks/compare/v1.2.0...v0.3.0
[0.2.0]: https://github.com/cascode-labs/softworks/compare/v0.1.0...v0.2.0
[1.0.0]: https://github.com/cascode-labs/softworks/releases/tag/v0.1.0