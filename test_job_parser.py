from pathlib import Path
import json

from config import Settings
from modules.job_parser import JobParser


def main():

    settings = Settings()

    parser = JobParser(settings)

    result = parser.parse(
        Path("input/job_offer.txt")
    )

    print("\n=========== RESULT ===========\n")

    print(
        json.dumps(
            result,
            indent=4,
            ensure_ascii=False,
        )
    )

    print("\n==============================\n")


if __name__ == "__main__":

    main()