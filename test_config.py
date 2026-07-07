from config import Settings


def main():

    settings = Settings()

    print()

    print("=" * 60)
    print("PROJECT")
    print("=" * 60)

    print(settings.project_root)

    print()

    print("=" * 60)
    print("DIRECTORIES")
    print("=" * 60)

    print(settings.input_dir)
    print(settings.output_dir)
    print(settings.logs_dir)
    print(settings.prompts_dir)
    print(settings.schemas_dir)
    print(settings.data_dir)

    print()

    print("=" * 60)
    print("FILES")
    print("=" * 60)

    print(settings.job_input_file)
    print(settings.job_prompt_file)
    print(settings.job_schema_file)
    print(settings.job_output_file)

    print()

    print("=" * 60)
    print("LLM")
    print("=" * 60)

    print(settings.provider)
    print(settings.model)

    print()

    print("=" * 60)
    print("Configuration OK")
    print("=" * 60)


if __name__ == "__main__":

    main()