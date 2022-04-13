"""Apprise target sink class, which handles writing streams."""
from singer_sdk.sinks import RecordSink
from typing import Optional
import apprise


class AppriseSink(RecordSink):
    """Apprise target sink class."""

    def process_record(self, record: dict, context: dict) -> None:
        """Process the record."""
        a = apprise.Apprise()
        for uri in self.config["uris"]:
            a.add(uri)

        title: Optional[str] = record.get("title")
        body: Optional[str] = record.get("body")
        if (title is None and body is None):
            raise Exception("Both the title and body cannot be None")
        a.notify(title=title, body=body)
