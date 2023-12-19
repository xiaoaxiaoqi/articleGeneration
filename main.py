from datetime import datetime
import threading
import time

import requests

from util.config_tool import ConfigTool

config_tool = ConfigTool(file_path='配置文件.ini')
save_file_path = config_tool.read_config('System', '文章保存目录')
keyword_file_path = config_tool.read_config('System', '关键词列表文件路径')
keywords_content = ""
# 检查文件是否有内容
try:
    with open(keyword_file_path, 'r', encoding="utf-8") as file:
        keywords_content = file.read()
except FileNotFoundError:
    print('error:关键词列表读取失败，请检查路径是否正确或是否存在内容')

# 将关键词内容按行拆分
keyword_lines = keywords_content.split('\n')

key_file_path = config_tool.read_config('System', 'Key列表文件路径')
key_lines = ""
# 检查文件是否有内容
try:
    with open(key_file_path, 'r', encoding="utf-8") as file:
        key_lines = file.read().strip("\n")
except FileNotFoundError:
    print('error：key列表读取失败，请检查路径是否正确或是否存在内容')


def output_msg(msg):
    # 获取当前的日期和时间
    current_datetime = datetime.now()
    # 将日期和时间格式化为字符串
    formatted_datetime = current_datetime.strftime("%Y-%m-%d %H:%M:%S")
    print(f"{formatted_datetime}    {msg}")


def process_line(title):
    # 在这里添加你对每一行的处理逻辑
    output_msg(f"正在生成 {title} ，请稍等")
    # ChatGPT-3.5 API端点URL
    url = config_tool.read_config('Openai', 'url')
    prompt_template = config_tool.read_config('Writing', '提示词')
    # 将 {title} 替换为实际的标题
    prompt = prompt_template.replace('{title}', title)
    # # 准备POST请求的数据
    data = {
        "messages": [
            {"role": "user", "content": prompt},
        ],
        "model": config_tool.read_config('Openai', 'model'),
        "temperature": float(config_tool.read_config('Openai', 'temperature')),
        "max_tokens": int(config_tool.read_config('Openai', 'max_tokens')),
    }
    # 设置请求头，包括认证信息
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {key_lines}"
    }
    timeout = int(config_tool.read_config('Openai', '超时时间'))
    # 发送POST请求
    response = requests.post(url, json=data, headers=headers, timeout=timeout)
    content = response.json()
    try:
        content = response.json()['choices'][0]['message']['content']
        # 将内容写入到文件
        with open(f"{save_file_path}/{title}.txt", 'w', encoding='utf-8') as output:
            output.write(content)
        output_msg(f"{title} 生成完毕,已保存至{save_file_path}/{title}.txt")
    except KeyError:
        print(f"error:{content}")


threads = []
# 在这里指定线程数
num_threads = config_tool.read_config('System', '线程数')
# 间隔时间，单位为秒
thread_interval = config_tool.read_config('System', '线程间隔时间')
for line in keyword_lines:
    thread = threading.Thread(target=process_line, args=(line,))
    threads.append(thread)
    thread.start()

    # 等待启动的线程数
    if len(threads) == num_threads:
        for t in threads:
            t.join()
        threads = []
    # 添加线程之间的间隔时间
    time.sleep(int(thread_interval))

# 确保剩余的线程都完成
for thread in threads:
    thread.join()
