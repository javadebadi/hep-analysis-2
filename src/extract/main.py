"""main module to extract
"""
from .source.literature import extract_source_literature

def main(
    size=10,
    resume=True,
    min_control_number=1,
    max_control_number=20000,
):
    extract_source_literature(
        size=size,
        resume=resume,
        min_control_number=min_control_number,
        max_control_number=max_control_number,
        )