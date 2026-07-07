"""
app.py

Resume AI Pipeline
Main Entry Point
"""

from config import Settings
from modules.job_parser import JobParser


def main() -> None:
    """
    Main application entry point.
    """

    settings = Settings()

    parser = JobParser(settings)

    job = parser.parse(
        settings.job_input_file
    )

    print()
    print("=" * 60)
    print("JOB PARSED SUCCESSFULLY")
    print("=" * 60)
    print(f"Title      : {job['job_title']}")
    print(f"Company    : {job['company']}")
    print(f"Location   : {job['location']}")
    print(f"Skills     : {len(job['required_skills'])}")
    print(f"Keywords   : {len(job['keywords'])}")
    print(f"Output     : {settings.job_output_file}")
    print("=" * 60)


if __name__ == "__main__":
    main()