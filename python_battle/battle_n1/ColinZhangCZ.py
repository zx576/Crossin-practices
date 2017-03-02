import clipboard
import time
clipboard.copy('')
text_0 = ''
count = 0
while True:
    if clipboard.paste() != '' and clipboard.paste() != text_0:
        text_0 = clipboard.paste()
        text = clipboard.paste().encode('utf-8')
        if '\r\n' not in text:
            text += '\r\n'
        else:
            text = text.replace('\r\n', ' ')
        text = text.replace('et al. ', 'et al.')
        if text[-1] == ',':
            continue
        elif text[-1] == '.' and text[-6:] != 'et al.':
            text += '\r\n'
        f = file('text.txt', 'a')
        f.write(text)
        f.close()
    else:
        time.sleep(0.1)
        continue
