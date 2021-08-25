'''
prints all commands defined in usualcmd.tex
copy and paste into displycmds.tex
'''

import re

skip = {'pdfEinfty', 'anibal'}

with open('usualcmds.tex') as f:
    contents = f.read()

    pattern1 = re.compile(r'[dr]{(.+?)}{')
    matches1 = pattern1.finditer(contents)
    for m in matches1:
        if all([w not in m[1] for w in skip]):
            print(f'\\verb|{m[1]}|, ${m[1]}$ ;')

    print('\n')

    pattern2 = re.compile(r'[dr]{(.+?)}\[(\d)\]')
    matches2 = pattern2.finditer(contents)
    for m in matches2:
        if m[2] == '1':
            print(f'\\verb|{m[1]}{{x}}"|, ${m[1]}{{x}}$ ;')
        if m[2] == '2':
            print(f'\\verb|{m[1]}{{x}}{{y}}"|, ${m[1]}{{x}}{{y}}$ ;')
