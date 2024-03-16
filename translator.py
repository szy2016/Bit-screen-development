from googletrans import Translator

def translate_file_in_place(input_file_path, output_file_path=None, src_lang='zh-cn', dest_lang='en'):
    """
    将指定文件中的所有中文翻译为英文，并将翻译后的内容保存回原文件或新文件。
    
    :param input_file_path: 输入文件的路径
    :param output_file_path: 输出文件的路径（如果为None，则覆盖原文件）
    :param src_lang: 源语言代码，默认为'zh-cn'（简体中文）
    :param dest_lang: 目标语言代码，默认为'en'（英文）
    """
    translator = Translator()
    
    # 读取文件内容
    with open(input_file_path, 'r', encoding='utf-8') as file:
        content = file.read()
    
    # 分割文件内容为行
    lines = content.split('\n')
    
    # 翻译每一行
    translated_lines = []
    for line in lines:
        words = line.split()  # 按空格分割单词
        translated_words = []
        for word in words:
            # 翻译单个单词
            translation = translator.translate(word, src=src_lang, dest=dest_lang)
            translated_words.append(translation.text)
        translated_line = ' '.join(translated_words)  # 重新组合翻译后的单词成行
        translated_lines.append(translated_line)
    
    # 将翻译后的内容组合成完整的文件内容
    translated_content = '\n'.join(translated_lines)
    
    # 将翻译后的内容写回文件
    if output_file_path:
        with open(output_file_path, 'w', encoding='utf-8') as file:
            file.write(translated_content)
    else:
        with open(input_file_path, 'w', encoding='utf-8') as file:
            file.write(translated_content)

# 使用方法
translate_file_in_place('input.txt')  # 这将覆盖input.txt文件，将翻译后的内容保存回原文件
# 如果你想把翻译后的内容保存到新文件，可以使用以下代码：
# translate_file_in_place('input.txt', 'output.txt')  # 这将把翻译后的内容保存到output.txt文件，原文件不变
