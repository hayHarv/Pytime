"""
+ - - - - + - - - - +
|         |         |
|         |         |
|         |         |
|         |         |
+ - - - - + - - - - +
|         |         |
|         |         |
|         |         |
|         |         |
+ - - - - + - - - - +
"""

def reflect(s):
    return s + s[1:]

def reflect_n(s,n):
    output = ''
    for i in range(n):
        output += s
    return output

def constructor(outer,inner,width):
     inner_width = width - 2 * len(outer)
     return outer + inner * inner_width + outer

def reflect_n(s,n):
     output = s[0] + n*s[1:]
     return output

def stack_lines(line1,line2):
    return line1 + '\n' + line2

desired_width = 7
beam = constructor('+','-',desired_width)
post = constructor('|',' ',desired_width)

desired_sections = 2
beam_row = reflect_n(beam,desired_sections)
post_row = reflect_n(post,desired_sections)

post_rows = stack_lines(post_row,post_row)
all_posts_rows = stack_lines(post_rows,post_rows)

section = stack_lines(beam_row,all_posts_rows)
completed_section = stack_lines(section,section)

square = stack_lines(completed_section,beam_row)
print(square)
