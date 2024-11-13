# `target-apprise` ![Build and Tests](https://github.com/AutoIDM/target-apprise/actions/workflows/ci.yml/badge.svg?branch=main) [![PyPI download month](https://img.shields.io/pypi/dm/target-apprise.svg)](https://pypi.python.org/pypi/target-apprise/) 
Target for Apprise. 

Tap was created by [AutoIDM](https://autoidm.com)

<a href="https://autoidm.com"><img alt="AutoIDM" src="./images/autoidm.png" width="250"></a>

Built with the [Meltano SDK](https://sdk.meltano.com) for Singer Taps and Targets. Curious about Meltano? I'd recommend checking out the [Meltano Hub](https://hub.meltano.com/) for a large number of taps/targets available to connect data with!

# Usage

## Basic Usage with a Slack URI

```bash
pipx install meltano
#Note that you have to escape the quotes, dotenv is nice as it's not committed along with your repo keeping your secrets, secret!
meltano config target-apprise set uris [\"https://hooks.slack.com/services/tokenhere/tokenhere/tokenhere\"] --store dotenv
meltano invoke target-apprise --version
# Note that instead of input example, you can setup data to come from anywhere (Normally it'd be from a DB / DW via a singer tap) 
cat usage_examples/input_example.jsonl | meltano invoke target-apprise
```

## Dynamically Providing Target Emails

When `uri_replacement` is enabled, we can defer defining a portion of a URI until runtime, when it will be dynamically configured based on the record provided to the target. The below example uses a URI of `"ses://from_email@example.com/ABC123A3F7U3V21B38RA/ABC123PBDYXSpr0CfEPhZA4tm8HWdSARgC8bKDl1/us-east-2/{_sdc_replace_target_email}/"`, where `_sdc_replace_target_email` is then configured individually for each row sent to the target.

```bash
pipx install meltano
# Use your own from_email, AWS access key, and AWS secret key instead of these fake ones.
meltano config target-apprise set uris [\"ses://from_email@example.com/ABC123A3F7U3V21B38RA/ABC123PBDYXSpr0CfEPhZA4tm8HWdSARgC8bKDl1/us-east-2/{_sdc_replace_target_email}/\"] --store dotenv
meltano config target-apprise set uri_replacement true --store dotenv
meltano invoke target-apprise --version
cat usage_examples/input_example_with_dynamic_target_email.jsonl | meltano invoke target-apprise
```

# Sponsors
Want to become a sponsor? Reach out to us at [autoidm.com](https://autoidm.com)

## Capabilities

* `about`
* `stream-maps`
* `schema-flattening`

## Settings

| Setting | Required | Default | Description |
|:--------|:--------:|:-------:|:------------|
| uris | True     | None    | Array of apprise URIs,checkout https://github.com/caronc/apprise |
| uri_replacement | True     |       0 | If enabled, allows for uris to be dynamically configured. Any fields in the record that have a name beginning with `_sdc_replace_`, will have their value substituted in for a matching string in the URI. See an example [here](#dynamically-providing-target-emails). |
| add_record_metadata | False    | None    | Add metadata to records. |
| load_method | False    | append-only | The method to use when loading data into the destination. `append-only` will always write all input records whether that records already exists or not. `upsert` will update existing records and insert new records. `overwrite` will delete all existing records and insert all input records. |
| batch_size_rows | False    | None    | Maximum number of rows in each batch. |
| validate_records | False    |       1 | Whether to validate the schema of the incoming streams. |
| stream_maps | False    | None    | Config object for stream maps capability. For more information check out [Stream Maps](https://sdk.meltano.com/en/latest/stream_maps.html). |
| stream_map_config | False    | None    | User-defined config values to be used within map expressions. |
| faker_config | False    | None    | Config for the [`Faker`](https://faker.readthedocs.io/en/master/) instance variable `fake` used within map expressions. Only applicable if the plugin specifies `faker` as an addtional dependency (through the `singer-sdk` `faker` extra or directly). |
| faker_config.seed | False    | None    | Value to seed the Faker generator for deterministic output: https://faker.readthedocs.io/en/master/#seeding-the-generator |
| faker_config.locale | False    | None    | One or more LCID locale strings to produce localized output for: https://faker.readthedocs.io/en/master/#localization |
| flattening_enabled | False    | None    | 'True' to enable schema flattening and automatically expand nested properties. |
| flattening_max_depth | False    | None    | The max depth to flatten schemas. |

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
cat usage_examples/input_example.jsonl | target-apprise --config /path/to/target-apprise-config.json
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
cat usage_examples/input_example.jsonl | meltano invoke target-apprise
```

### SDK Dev Guide

See the [dev guide](https://sdk.meltano.com/en/latest/dev_guide.html) for more instructions on how to use the Meltano SDK to
develop your own Singer taps and targets.
