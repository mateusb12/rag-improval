from pathlib import Path


def get_root_folder_path():
    return Path(__file__).parent.parent


def get_tree_pkl_path():
    return Path(get_root_folder_path(), 'demo/tree.pkl')


def get_datasets_folder_path():
    return Path(get_root_folder_path(), 'datasets')


def main():
    root_folder = get_tree_pkl_path()
    print(root_folder)
    return


if __name__ == '__main__':
    main()
