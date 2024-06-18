import json

import pandas as pd

from path.path_reference import get_datasets_folder_path


def load_qasper_dataset():
    qasper_folder_path = get_datasets_folder_path() / 'qasper/'
    dev_file_path = qasper_folder_path / 'qasper-dev-v0.3.json'
    train_file_path = qasper_folder_path / 'qasper-train-v0.3.json'

    with open(dev_file_path, 'r') as f:
        dev_data = json.load(f)
    with open(train_file_path, 'r') as f:
        train_data = json.load(f)

    dev_df = pd.json_normalize(dev_data)
    train_df = pd.json_normalize(train_data)

    return dev_df, train_df


def load_narrative_qa_dataset(file_path):
    return pd.read_csv(file_path)


def load_quality_dataset(file_path):
    return pd.read_csv(file_path)


def main():
    qasper_train, qasper_dev = load_qasper_dataset()
    return


if __name__ == "__main__":
    main()
