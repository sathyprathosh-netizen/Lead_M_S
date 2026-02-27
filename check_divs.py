
import re

with open(r'c:\Users\HP\Desktop\LMS\super-admin\architectural-command.html', 'r', encoding='utf-8') as f:
    content = f.read()

divs = re.findall(r'<div', content)
cdivs = re.findall(r'</div>', content)

print(f"Opening divs: {len(divs)}")
print(f"Closing divs: {len(cdivs)}")

# Let's check nesting more carefully by tracking level
lines = content.split('\n')
level = 0
for i, line in enumerate(lines):
    opens = line.count('<div')
    closes = line.count('</div>')
    level += opens - closes
    if level < 0:
        print(f"Error at line {i+1}: Negative nesting level {level}")
        level = 0
print(f"Final nesting level: {level}")
