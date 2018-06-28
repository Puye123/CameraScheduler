import datetime
import os

def get_unique_name(date: datetime.datetime):
    """時刻から一意に識別可能な文字列を生成する
    
    Arguments:
        date {datetime.datetime} -- 時刻
    
    Returns:
        [type] -- 一意に識別可能な文字列
    """
    unique_name = date.strftime("%Y%m%d_%H%M%S")
    return unique_name

def make_unique_name_directory():
    """現在時刻に基づいた名前のディレクトリを生成する
    """
    date = datetime.datetime.now()
    dir_path = './' + get_unique_name(date)
    if not os.path.isdir(dir_path):
        os.mkdir(dir_path)

make_unique_name_directory()
