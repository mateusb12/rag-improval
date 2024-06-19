import json
import csv
from typing import Dict, Tuple
from pathlib import Path

from path.path_reference import get_datasets_folder_path


def load_qasper_files() -> Tuple[Dict, Dict]:
    qasper_folder_path = get_datasets_folder_path() / 'qasper/'
    dev_file_path = qasper_folder_path / 'qasper-dev-v0.3.json'
    train_file_path = qasper_folder_path / 'qasper-train-v0.3.json'
    with open(dev_file_path, 'r') as f:
        dev_data = json.load(f)
    with open(train_file_path, 'r') as f:
        train_data = json.load(f)
    return dev_data, train_data


def normalize_qasper():
    dev_data, train_data = load_qasper_files()

    # Normalize and write dev data to CSV
    with open('qasper_dev_normalized.csv', 'w', newline='', encoding='utf-8') as dev_csvfile:
        fieldnames = ['ID', 'Title', 'Abstract', 'Section Name', 'Paragraph', 'Question', 'Answer']
        writer = csv.DictWriter(dev_csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for paper_id, paper_info in dev_data.items():
            write_paper_to_csv(writer, paper_id, paper_info)

    # Normalize and write train data to CSV
    with open('qasper_train_normalized.csv', 'w', newline='', encoding='utf-8') as train_csvfile:
        fieldnames = ['ID', 'Title', 'Abstract', 'Section Name', 'Paragraph', 'Question', 'Answer']
        writer = csv.DictWriter(train_csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for paper_id, paper_info in train_data.items():
            write_paper_to_csv(writer, paper_id, paper_info)


def write_paper_to_csv(writer, paper_id, paper_info):
    title = paper_info.get('title', '')
    abstract = paper_info.get('abstract', '')

    # Extract full text sections
    for section in paper_info.get('full_text', []):
        section_name = section.get('section_name', '')
        for paragraph in section.get('paragraphs', []):
            writer.writerow({
                'ID': paper_id,
                'Title': title,
                'Abstract': abstract,
                'Section Name': section_name,
                'Paragraph': paragraph,
                'Question': '',
                'Answer': ''
            })

    # Extract Q&A pairs
    for qa in paper_info.get('qas', []):
        question = qa.get('question', '')
        for answer in qa.get('answers', []):
            answer_text = answer.get('answer', {}).get('free_form_answer', '')
            writer.writerow({
                'ID': paper_id,
                'Title': title,
                'Abstract': abstract,
                'Section Name': '',
                'Paragraph': '',
                'Question': question,
                'Answer': answer_text
            })


if __name__ == '__main__':
    normalize_qasper()
