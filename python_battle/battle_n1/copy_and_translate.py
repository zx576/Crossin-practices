# -*- coding: utf-8 -*-
import clipboard
import time
import threading
from textblob import TextBlob


def clipboard_is_ok(text):
    """Ensuring the clipboard is not empty and the it's content is different with the previous's."""
    if clipboard.paste() != u'' and clipboard.paste() != text:
        return 1
    else:
        return 0


def exclude_special(text):
    """Some special cases that sentence not end."""
    if text[-6:] != 'et al.':
        return 1
    else:
        return 0


def last_sentence_complete(text):
    """Ensuring the last sentence of the copied paragraph is complete."""
    symbol_list_0 = ['.', '?', '!']  # sentence end with these symbols
    symbol_list_1 = [',', ':', ';']  # sentence does not end with these symbols
    if text[-1] in symbol_list_0 and exclude_special(text):
        return 1
    elif text[-1] in symbol_list_1:
        return 0


def finish_copy():
    s = raw_input("press 'y' to begin translate!\n")
    if s == 'y':
        return s


def translate(text_list):
    translated_text_list = []
    for text in text_list:
        text = text.decode('utf-8')
        translated_text = repr(TextBlob(text).translate(to='zh-CN'))
        translated_text = translated_text.replace('TextBlob("', '')
        translated_text = translated_text.replace('")', '')
        translated_text += '\n'
        translated_text_list.append(translated_text)
    return translated_text_list

finish_copy_thread = threading.Thread(target=finish_copy())
finish_copy_thread.setDaemon(True)
finish_copy_thread.start()
clipboard.copy('')
previous_text = u''
while not finish_copy():
    if clipboard_is_ok(previous_text):
        previous_text = clipboard.paste()
        original_text = clipboard.paste().encode('utf-8')
        original_text = original_text.replace('et al. ', 'et al.')
        if '\r\n' not in original_text:
            original_text += '\n'
        else:
            original_text = original_text.replace('\r\n', ' ')
            if last_sentence_complete(original_text):
                original_text += '\n'
        print original_text
        with open('original_text.txt', 'a') as f:
            f.write(original_text)
    else:
        time.sleep(0.05)

with open('original_text.txt', 'r') as f:
    original_text_list = f.readlines()
with open('translated_text.txt', 'w') as f:
    f.writelines(translate(original_text_list))

print '翻译成功！'
