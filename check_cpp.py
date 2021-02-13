#!/usr/bin/python

from os import scandir
import re
from subprocess import run

solutionsrc = None
for fe in scandir():
    if fe.is_file() and fe.name.endswith('.cpp') and not fe.name.startswith('_'):
        solutionsrc = fe.name
        break

if solutionsrc is None:
    print("No solution found")
    exit()

solution = solutionsrc[:-4]
subproc = run([f"g++ {solutionsrc} -o {solution}"], text=True, shell=True, capture_output=True)
if subproc.returncode != 0:
    print(subproc.stderr)
    exit()

tests = []
for fe in scandir("tests"):
    if fe.is_file() and fe.name.endswith('.in'):
        tests.append(fe.name[:-3])

if not tests:
    print("No tests found")
    exit()

for testname in tests:
    ok = True
    with open(f"tests/{testname}.in") as f:
        subproc = run([f"./{solution}"], stdin=f, text=True, shell=True, capture_output=True)
    if subproc.returncode != 0:
        print(subproc.stderr)
        continue
    result = subproc.stdout.splitlines(keepends=True)
    with open(f"tests/{testname}.out") as f:
        answer = f.readlines()
        for i in range(len(answer)):
            if i < len(result):
                if result[i] != answer[i]:
                    ok = False
                    print(f"LINE {i+1}\n\t{answer[i]}\n\t{result[i]}")
            else:
                ok = False
                print("Missing line")
    if ok:
        print(f"Test '{testname}' CORRECT")
