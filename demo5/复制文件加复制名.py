#-*- coding=utf-8 -*-

input_file_name = input("请您输入要复制的文件名:")
old_file = open(input_file_name, 'r')
position = input_file_name.rfind('.')
new_file_name = input_file_name[0:position]+'复制'+input_file_name[position:]
new_file = open(new_file_name, 'w')
content = old_file.read()
new_file.write(content)
old_file.close()
new_file.close()