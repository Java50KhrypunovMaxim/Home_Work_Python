import codecs
import re

def delete_html_tags(html_file, result_file='cleaned.txt'):
      with codecs.open(html_file, 'r', 'utf-8') as file:
           html = file.read()
      words = re.findall(r'>[^<]+<', html)
      cleaned_text = [word[1:-1].strip() for word in words]
      with codecs.open(result_file, 'w', 'utf-8') as res_file:
           for word in cleaned_text:
               if word:
                  res_file.write(word + '\n')

delete_html_tags('draft.html')