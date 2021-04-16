# gr-lora_sdr-profiler



> Profile different flowgraph configurations of [gr-lora_sdr](https://github.com/martynvdijke/gr-lora_sdr)

[![PyPI Version][pypi-image]][pypi-url]
[![Build Status][build-image]][build-url]
[![Code Coverage][coverage-image]][coverage-url]
[![Code Quality][quality-image]][quality-url]

## Summary
This is a python cli package to be able to load and config yml file and change values to the flowgraph.
## Installation

```sh
pip install gr_lora_sdr_profiler
```
## Documentation

```python
[-h] 
[--version] 
[-m {multi_stream,frame_detector,cran}] 
[-s {pandas,wandb,both}] 
[-n NAME] 
[-p FILE] 
[-o OUTPUT] 
[-t TIMEOUT] 
[-v] 
[-vv] 
FILE [FILE ...]
```

## Usage

### config

### cli
Run flowgraph 
```python
python -m profiler --m frame_detector -s pandas example_config.yml 
```
Plot all values by using 
```python
python -m profiler --m frame_detector -p results/out.csv example_config.yml 
```

## Development setup

```sh
$ python3 -m venv env
$ . env/bin/activate
$ make deps
$ tox
```
## [Changelog](CHANGELOG.md)

## License

[MIT](https://choosealicense.com/licenses/mit/)

<!-- Badges -->

<!-- [pypi-image]: https://img.shields.io/pypi/v/gr_lora_sdr_profiler
[pypi-url]: https://pypi.org/project/gr_lora_sdr_profiler/
[build-image]: https://github.com/nalgeon/podsearch-py/actions/workflows/build.yml/badge.svg
[build-url]: https://github.com/nalgeon/podsearch-py/actions/workflows/build.yml
[coverage-image]: https://codecov.io/gh/nalgeon/podsearch-py/branch/main/graph/badge.svg
[coverage-url]: https://codecov.io/gh/nalgeon/podsearch-py
[quality-image]: https://api.codeclimate.com/v1/badges/3130fa0ba3b7993fbf0a/maintainability
[quality-url]: https://codeclimate.com/github/nalgeon/podsearch-py -->