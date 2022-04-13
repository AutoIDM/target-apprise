"""Apprise target class."""

from singer_sdk.target_base import Target
from singer_sdk import typing as th

from target_apprise.sinks import (
    AppriseSink,
)


class TargetApprise(Target):
    """Sample target for Apprise."""

    name = "target-apprise"
    config_jsonschema = th.PropertiesList(
        th.Property(
            "uris",
            th.ArrayType(th.StringType),
            description="Array of apprise URIs,"
            + "checkout https://github.com/caronc/apprise",
            required=True,
        ),
    ).to_dict()
    default_sink_class = AppriseSink
