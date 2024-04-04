# Imports
import os
import pandas as pd
from zipfile import ZipFile
from argparse import ArgumentParser

parser = ArgumentParser()
parser.add_argument("-s", "--source", default=".", type=str, help="Location of the source ImageFolder")
parser.add_argument("-d", "--destination", default=".", type=str, help="Location of the destination folder")

def parse_args(parser):
    args = parser.parse_args()
    src_base = args.source
    dest_base = args.destination
    if src_base == '.':
        src_base = os.path.dirname(os.path.abspath(__file__))
    if dest_base == '.':
        dest_base = os.path.dirname(os.path.abspath(__file__))
    return src_base, dest_base

def run_script(src_base, dest_base):
    exts = ["tif", "tiff", "jpg", "jpeg", "png"]
    df = pd.DataFrame(columns=["filename", "dr_level"])
    sub_dirs = os.listdir(src_base)
    filenames = []
    labels = []
    with ZipFile(f"{dest_base}/files.zip", "w") as zip_obj:
        for i in sub_dirs:
            base_path = os.path.join(src_base, i)
            files_list = set(os.listdir(base_path))
            for filename in files_list:
                for ext in exts:
                    if filename.endswith(f".{ext}"):
                        zip_obj.write(os.path.join(base_path, filename), arcname=filename)
                        filenames.append(filename)
                        labels.append(i)
    data = {"filename": pd.Series(filenames), "dr_level": pd.Series(labels)}
    df = pd.concat(data, axis=1)
    df.to_csv(f"{dest_base}/data.csv", index=False)

def parse_command_line_args(args):
    parser = ArgumentParser()
    parser.add_argument("-s", "--source", default=".", type=str, help="Location of the source ImageFolder")
    parser.add_argument("-d", "--destination", default=".", type=str, help="Location of the destination folder")
    parsed_args = parser.parse_args(args)
    src_base = parsed_args.source
    dest_base = parsed_args.destination
    if src_base == '.':
        src_base = os.path.dirname(os.path.abspath(__file__))
    if dest_base == '.':
        dest_base = os.path.dirname(os.path.abspath(__file__))
    return src_base, dest_base