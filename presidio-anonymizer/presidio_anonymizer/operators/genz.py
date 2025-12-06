"""Replaces the PII text entity with gen-z slang."""

from typing import Dict

from presidio_anonymizer.operators import Operator, OperatorType


class GenZ(Operator):
    """Redact the string - empty value."""

    def operate(self, text: str = None, params: Dict = None) -> str:
        """:return: an empty value."""
        return ""

    def validate(self, params: Dict = None) -> None:
        """gen-z does not require any parameters so no validation is needed."""
        pass

    def operator_name(self) -> str:
        """Return operator name."""
        return "genz"

    def operator_type(self) -> OperatorType:
        """Return operator type."""
        return OperatorType.Anonymize
