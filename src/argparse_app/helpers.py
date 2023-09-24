from __future__ import annotations

import argparse
from dataclasses import asdict, dataclass, field
import sys
from typing import Optional, Sequence, Type


@dataclass
class ParserCfg:
    """Config schema for argparse parser.
    Parameters same as at argparse.ArgumentParser.
    """

    prog: str | None = None
    usage: str | None = None
    description: str | None = None
    epilog: str | None = None
    parents: Sequence[argparse.ArgumentParser] = field(default_factory=list)
    formatter_class: Type[argparse.HelpFormatter] = argparse.HelpFormatter
    prefix_chars: str = "-"
    fromfile_prefix_chars: str | None = None
    argument_default: str | None = None
    conflict_handler: str = "error"
    add_help: bool = True
    allow_abbrev: bool = True
    exit_on_error: bool = True


def create_parser(
    parser_cfg: Optional[ParserCfg] = None,
) -> argparse.ArgumentParser:
    """Create argparse parser."""
    if parser_cfg is None:
        parser_cfg = ParserCfg()
    kwargs = asdict(parser_cfg)
    if sys.version_info.minor < 9:  # from python 3.9
        kwargs.pop("exit_on_error")  # pragma: no cover
    parser = argparse.ArgumentParser(**kwargs)
    return parser
