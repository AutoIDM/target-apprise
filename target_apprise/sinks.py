"""Apprise target sink class, which handles writing streams."""
import re
import typing as t

import apprise
from singer_sdk.sinks import RecordSink


class AppriseSink(RecordSink):
    """Apprise target sink class."""

    def process_record(self, record: dict[str, t.Any], context: dict) -> None:
        """Process the record."""
        a = apprise.Apprise()
        for uri in self.config["uris"]:
            formatted_uri: str = uri
            if self.config["uri_replacement"]:
                for k, v in record.items():
                    if not k.startswith("_sdc_replace_"):
                        continue
                    to_replace = f"{{{k}}}"  # Ex: '{_sdc_replace_target_email}'

                    if to_replace not in uri:
                        debug_msg = (  # Contains secrets!
                            "Encountered an error while attempting to do URI "
                            f"replacement for URI: '{uri}'."
                        )
                        self.logger.debug(debug_msg)
                        msg = (
                            f"The uri_replacement column of '{k}' exists but at least "
                            "one of the configured `uris` is missing it."
                        )
                        raise RuntimeError(msg)

                    formatted_uri = formatted_uri.replace(to_replace, v)

                pattern = r"\{_sdc_replace_.*?\}"
                if re.search(pattern, formatted_uri):
                    debug_msg = (  # Contains secrets!
                        "Encountered an error while attempting to do URI "
                        f"replacement for URI: '{uri}'."
                    )
                    self.logger.debug(debug_msg)
                    msg = (
                        "At least one of the configured `uris` contains "
                        "uri_replacement placeholders for which no matching "
                        "columns exist."
                    )
                    raise RuntimeError(msg)
            a.add(formatted_uri)

        title: t.Optional[str] = record.get("title")
        body: t.Optional[str] = record.get("body")
        attach: t.Optional[str] = record.get("attach")
        if title is None and body is None:
            raise Exception("Both the title and body cannot be None")
        if a.notify(title=title, body=body, attach=attach) is False:
            raise Exception("Failed to send notification")
