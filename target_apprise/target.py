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
        th.Property(
            "uri_replacement",
            th.BooleanType,
            description= (
                "If enabled, allows for uris to be dynamically configured. Any fields "
                "in the record that have a name beginning with `_sdc_replace_`, will "
                "have their value substituted in for a matching string in the URI. See "
                "an example [here](#dynamically-providing-target-emails)."
            ),
            required=True,
            default=False,
        ),
    ).to_dict()
    default_sink_class = AppriseSink
