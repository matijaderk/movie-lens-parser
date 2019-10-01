import shutil
import os.path


def copy_without_headers(filename, input_dir, output_dir):
    input_filename = os.path.join(input_dir, filename)
    output_filename = os.path.join(output_dir, filename)

    source_file = open(input_filename, 'r')
    source_file.readline()
    target_file = open(output_filename, 'w')
    shutil.copyfileobj(source_file, target_file)


def copy_other_files(ratings, tags, links, input_dir, output_dir):
    print('Copy ratings...')
    copy_without_headers(ratings, input_dir, output_dir)

    print('Copy tags...')
    copy_without_headers(tags, input_dir, output_dir)

    print('Copy links...')
    copy_without_headers(links, input_dir, output_dir)
