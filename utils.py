"""
Pure utility module — no bugs, no security issues, no user input.
AgentNoah should NOT flag anything here.
"""
from datetime import datetime


def format_timestamp(dt: datetime) -> str:
    """Return ISO-8601 string for a datetime."""
    return dt.isoformat()


def safe_int(value: str, default: int = 0) -> int:
    """Parse int with a fallback default. No user-input passthrough."""
    try:
        return int(value)
    except (ValueError, TypeError):
        return default
