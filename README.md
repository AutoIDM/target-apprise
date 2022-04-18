# `target-apprise` ![Build and Tests](https://github.com/AutoIDM/target-apprise/actions/workflows/ci.yml/badge.svg?branch=main) [![PyPI download month](https://img.shields.io/pypi/dm/target-apprise.svg)](https://pypi.python.org/pypi/target-apprise/) 
Target for Apprise. 

Tap was created by [AutoIDM](https://autoidm.com)

<a href="https://autoidm.com"><img alt="AutoIDM" src="./images/autoidm.png" width="250"></a>

Built with the [Meltano SDK](https://sdk.meltano.com) for Singer Taps and Targets. Curious about Meltano? I'd recommend checking out the [Meltano Hub](https://hub.meltano.com/) for a large number of taps/targets available to connect data with!

# Usage (example with a slack uri)

```bash
pipx install meltano
#Note that you have to escape the quotes, dotenv is nice as it's not committed along with your repo keeping your secrets, secret!
meltano config target-apprise set uris [\"https://hooks.slack.com/services/tokenhere/tokenhere/tokenhere\"] --store dotenv
meltano invoke target-apprise --version
# Note that instead of input_example, you can setup data to come from anywhere (Normally it'd be from a DB / DW via a singer tap) 
cat input_example | meltano invoke target-apprise
```

# Sponsors
Want to become a sponsor? Reach out to us at [autoidm.com](https://autoidm.com)

## Capabilities

* `about`
* `stream-maps`
* `schema-flattening`

## Settings

| Setting             | Required | Default | Description |
|:--------------------|:--------:|:-------:|:------------|
| uris                | True     | None    | Array of apprise URIs, see list here https://github.com/caronc/apprise |
| stream_maps         | False    | None    | Config object for stream maps capability. (Doesn't make much sense with this target) |
| stream_map_config   | False    | None    | User-defined config values to be used within map expressions. (Doesn't make much sense with this target) |
| flattening_enabled  | False    | None    | 'True' to enable schema flattening and automatically expand nested properties. (Doesn't make much sense with this target) |
| flattening_max_depth| False    | None    | The max depth to flatten schemas. (Doesn't make much sense with this target) |

A full list of supported settings and capabilities is available by running: `target-apprise --about`

Note that uris are **sensitive** information, so be sure to set these in your `.env` file if you're using Meltano. 


### Source Authentication and Authorization


## Usage

You can easily run `target-apprise` by itself or in a pipeline using [Meltano](https://meltano.com/).

### Executing the Target Directly

```bash
target-apprise --version
target-apprise --help
# Test using the sample in this repo:
cat input_example | target-apprise --config /path/to/target-apprise-config.json
```

## Developer Resources

### Initialize your Development Environment

```bash
pipx install poetry
poetry install
```

### Create and Run Tests

Create tests within the `target_apprise/tests` subfolder and
  then run:

```bash
poetry run pytest
```

You can also test the `target-apprise` CLI interface directly using `poetry run`:

```bash
poetry run target-apprise --help
```

### Testing with [Meltano](https://meltano.com/)

_**Note:** This target will work in any Singer environment and does not require Meltano.
Examples here are for convenience and to streamline end-to-end orchestration scenarios._

Next, install Meltano (if you haven't already) and any needed plugins:

```bash
# Install meltano
pipx install meltano
# Initialize meltano within this directory
cd target-apprise
meltano install
```

Now you can test and orchestrate using Meltano:

```bash
# Test invocation:
meltano invoke target-apprise --version
# OR run a test `elt` pipeline with the Carbon Intensity sample tap:
cat cat input_example | meltano invoke target-apprise
```

### SDK Dev Guide

See the [dev guide](https://sdk.meltano.com/en/latest/dev_guide.html) for more instructions on how to use the Meltano SDK to
develop your own Singer taps and targets.
