import logging
import os
import subprocess
import time
from pathlib import Path


def get_report_path() -> str:
    # 获取当前日期
    today = time.strftime('%Y%m%d')

    # 在当前目录下创建当天日期的目录
    dir_path = Path.cwd() / today
    if not dir_path.exists():
        dir_path.mkdir()

    # 查找当天日期的目录下是否有子目录
    sub_dirs = [d for d in dir_path.iterdir() if d.is_dir()]

    # 如果没有子目录，则在当天日期的目录下创建第一个子目录
    if not sub_dirs:
        sub_dir_path = dir_path / '1'
        sub_dir_path.mkdir()
    else:
        # 如果有子目录，则获取最后一个子目录的名称并增加1
        last_sub_dir_name = max([int(d.name) for d in sub_dirs])
        sub_dir_path = dir_path / str(last_sub_dir_name + 1)
        sub_dir_path.mkdir()

    # 获取 sub_dir_path 的绝对路径
    sub_dir_path_absolute = sub_dir_path.resolve()

    return str(sub_dir_path_absolute)


def generate_html(local_path, generate_path) -> bool:
    print('allure generate {0} -c -o  {1}'.format(local_path, generate_path))
    stdout, stderr = subprocess.Popen('allure generate {0} -c -o  {1}'.format(local_path, generate_path), shell=True,
                                      stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()
    logging.info('生成测试报告: {}'.format(generate_path))
    print(stdout, stderr)
    if stderr:
        logging.error('allure 执行命令异常：{}'.format(stderr))
        return False
    if not os.path.exists(generate_path) or not os.listdir(os.path.join(generate_path, 'data', 'test-cases')):
        logging.error('allure 未能生成报告目录：{}'.format(generate_path))
        return False
    return True

