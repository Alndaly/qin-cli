def create_file(path: str, content = ''):
    with open(path, 'w') as fp:
            # 在这里可以写入文件内容（如果需要）
            fp.write(content)
            
def read_file(path: str):
    with open(path, mode="r", encoding="utf-8") as f:
        return f.read()