from src.batch_processor import process_dataset


if __name__ == "__main__":

    report = process_dataset("data")

    print("\nFinished Processing Dataset")

    print(report.head())