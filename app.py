"""
app.py

Resume AI Pipeline
Main Entry Point
"""

from pathlib import Path

from config import Settings
from modules.job_parser import JobParser


def main() -> None:

    settings = Settings()

    settings.create_directories()

    parser = JobParser(settings)

    input_file = settings.input_dir / "job_offer.txt"

    if not input_file.exists():
        raise FileNotFoundError(
            f"Input file not found: {input_file}"
        )

    job = parser.parse(input_file)

    print("\n")
    print("=" * 60)
    print("JOB PARSED SUCCESSFULLY")
    print("=" * 60)
    print(f"Title   : {job['job_title']}")
    print(f"Company : {job['company']}")
    print(f"Skills  : {len(job['required_skills'])}")
    print(f"Output  : {settings.job_output_file}")
    print("=" * 60)


if __name__ == "__main__":
    main()