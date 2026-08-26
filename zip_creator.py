import zipfile
import pathlib
import datetime

def make_archive(filepaths, dest_dir):
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    dest_dir = pathlib.Path(dest_dir, timestamp + ".zip")
    with zipfile.ZipFile(dest_dir, 'w') as zip_ref:
        for filepath in filepaths:
            zip_ref.write(filepath)

