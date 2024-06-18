import ast
import json
from typing import Tuple

import pandas as pd

from path.path_reference import get_datasets_folder_path


def load_qasper_dataset() -> Tuple[pd.DataFrame, pd.DataFrame]:
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


def load_narrative_qa_dataset() -> pd.DataFrame:
    narrative_qa_folder_path = get_datasets_folder_path() / 'narrativeQA/'
    narrative_qa_path = narrative_qa_folder_path / 'qaps.csv'
    return pd.read_csv(narrative_qa_path)


def load_quality_dataset() -> Tuple[pd.DataFrame, pd.DataFrame, pd.DataFrame]:
    quality_folder_path = get_datasets_folder_path() / 'quality/'
    dev_file_path = quality_folder_path / 'QuALITY.v1.0.1.htmlstripped.dev'
    test_file_path = quality_folder_path / 'QuALITY.v1.0.1.htmlstripped.test'
    train_file_path = quality_folder_path / 'QuALITY.v1.0.1.htmlstripped.train'

    def load_and_parse_file(file_path):
        data = []
        with open(file_path, 'r', encoding='utf-8') as f:
            for line in f:
                stripped_line = line.strip()
                json_dict = ast.literal_eval(stripped_line)
                data.append(json_dict)
        df = pd.DataFrame(data)
        return df

    dev_file_df = load_and_parse_file(dev_file_path)
    test_file_df = load_and_parse_file(test_file_path)
    train_file_df = load_and_parse_file(train_file_path)

    return dev_file_df, test_file_df, train_file_df



def main():
    quality_dev, quality_test, quality_train = load_quality_dataset()
    return


if __name__ == "__main__":
    main()
