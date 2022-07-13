"""main module to extract
"""
from .source.literature import extract_source_literature
from .raw.literature import extract_raw_literature

def main(
    size=1000,
    resume=True,
    min_control_number=1,
    max_control_number=10000,
):
    extract_source_literature(
        size=size,
        resume=resume,
        min_control_number=min_control_number,
        max_control_number=max_control_number,
        )
    extract_raw_literature()