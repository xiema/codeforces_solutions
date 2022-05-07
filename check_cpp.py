#!/usr/bin/env python

import sys
from os import scandir
import re
from subprocess import run

workdir = sys.argv[1] if len(sys.argv) > 1 else None
testsdir = f"{workdir}/tests" if workdir else "tests"

solution_name, solution_src_path = None, None
for fe in scandir(workdir):
    if fe.is_file() and fe.name.endswith('.cpp') and not fe.name.startswith('_'):
        solution_name, solution_src_path = fe.name[:-4], fe.path
        break

if solution_name is None:
    print("No solution found")
    exit()

solution_exec_path = f"{workdir}/{solution_name}" if workdir else solution_name
subproc = run([f"g++ '{solution_src_path}' -o '{solution_exec_path}'"], text=True, shell=True, capture_output=True)
if subproc.returncode != 0:
    print(subproc.stderr)
    exit()

tests = []
for fe in scandir(testsdir):
    if fe.is_file() and fe.name.endswith('.in'):
        tests.append(fe.name[:-3])

if not tests:
    print("No tests found")
    exit()

for testname in tests:
    ok = True
    with open(f"{testsdir}/{testname}.in") as f:
        subproc = run([f"'./{solution_exec_path}'"], stdin=f, text=True, shell=True, capture_output=True)
    if subproc.returncode != 0:
        print(subproc.stderr)
        continue
    result = subproc.stdout.splitlines(keepends=True)
    with open(f"{testsdir}/{testname}.out") as f:
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
