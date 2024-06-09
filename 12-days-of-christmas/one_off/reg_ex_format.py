"""
one off script to convert a string with consecutive numbers to a string with consecutive numbers + 2
This is because I forgot ordering matters in .format() as dual digits cost more characters
"""
import re

text ="""
{11}First{12}{0}{11}Second{12}{1}{0}{11}Third{12}{2}{1}{0}{11}Fourth{12}{3}{2}{1}{0}{11}Fifth{12}{4}{3}{2}{1}{0}{11}Sixth{12}{5}{4}{3}{2}{1}{0}{11}Seventh{12}{6}{5}{4}{3}{2}{1}{0}{11}Eighth{12}{7}{6}{5}{4}{3}{2}{1}{0}{11}Ninth{12}{8}{7}{6}{5}{4}{3}{2}{1}{0}{11}Tenth{12}{9}{8}{7}{6}{5}{4}{3}{2}{1}{0}{11}Eleventh{12}{10}{9}{8}{7}{6}{5}{4}{3}{2}{1}{0}{11}Twelfth{12}Twelve Drummers Drumming,\n{10}{9}{8}{7}{6}{5}{4}{3}{2}{1}{0}"
"""

# find all consecutive number in string with % 12 + 2

re.compile(r'\d+').findall(text)
new_text = re.sub(r'\d+', lambda x: str((int(x.group())+2) % 13), text)

print(new_text)