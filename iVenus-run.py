# Made by Ryan Harper
# https://github.com/MeltingShoe 

import os
import subprocess

RESULT_HEAD = '========= block {index} output: ========='
DEFAULT_IMPORTS = "print('\\n')"
def get_blocks(separator = "```\n"): #lines is array
    path = os.path.abspath(os.path.join(__file__,'../..'))
    with open(f'{path}/iVenus-input.txt','r') as f:
        lines = f.readlines()
    flag = False
    block = ''
    out = []

    for line in lines:
        if separator in line:
            if flag:
                out.append(block)
                block = ''
            flag = not flag
        else:
            if flag:
                block += line
    return out

def combine_blocks():
    blocks = get_blocks()
    results = ''
    results += DEFAULT_IMPORTS
    results += '\n'
    for count, block in enumerate(blocks):
        results += f'print("{RESULT_HEAD.format(index=count)}")\n'
        results += block
    return results

def run_blocks():
    with open('iVenus-code.py','w') as f:
        f.write(combine_blocks())
    results = subprocess.check_output(f'python iVenus-code.py', stderr=subprocess.STDOUT, shell=True, text=True)
    with open('iVenus-results.txt','w') as f:
        f.write(results)

if __name__ == '__main__':
    run_blocks()

