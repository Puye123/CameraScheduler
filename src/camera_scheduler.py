import datetime

def get_unique_name(date: datetime.datetime):
    """時刻から一意に識別可能な文字列を生成する
    
    Arguments:
        date {datetime.datetime} -- 時刻
    
    Returns:
        [type] -- 一意に識別可能な文字列
    """
    unique_name = date.strftime("%Y%m%d_%H%M%S")
    return unique_name
