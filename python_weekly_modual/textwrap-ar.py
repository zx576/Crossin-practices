import textwrap
#
# ss = '''
#
#         odule provides some convenience functions, as well as TextWrapper,
#         the class that does all the work. If you’re just wrapping or filling
#         one or two text strings, the convenience functions should be good enough;
#         otherwise, you should use an insta
#
#     '''
# print(ss)
# wrap
# wrap_ss = textwrap.wrap(ss,width=70)
# print(wrap_ss)
# for i in wrap_ss:
#     print(i)

# filling
#
# fill_ss = textwrap.fill(ss)
# print(fill_ss)

# shorten
# short_ss = textwrap.shorten(ss,20,placeholder='...')
# print(short_ss)

# dedent
# dedent_ss = textwrap.dedent(ss)
# print(dedent_ss)

# indent
# indent_ss = textwrap.indent(dedent_ss,'+')
# print(indent_ss)

text = 'The module provides some convenience functions'
# 初始化化 TextWrapper
wrapper = textwrap.TextWrapper()
# 修改属性-每行最大长度
wrapper.width = 20
# 修改属性-第一行词头
wrapper.initial_indent = '+'
# 最后填充文本
print(wrapper.fill(text))



# text = 'odule provides some convenience functions.'
# after_wrap = textwrap.wrap(text,width=10)
# print(after_wrap)

# text = 'module provides some convenience functions.'
# after_fill = textwrap.fill(text,width=10)
# print(after_fill)

# shorten_text = textwrap.shorten(text,20)
# module [...]
# print(shorten_text)
#
# text = '''
#         hello,
#         world.
#        '''
# print(textwrap.dedent(text))
#
# text = 'hello,\nworld'
# print(textwrap.indent(text,'+'))








##############################
