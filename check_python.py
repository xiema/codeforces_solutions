from os import scandir
import re
import sys
from subprocess import run

workdir = sys.argv[1] if len(sys.argv) > 1 else None
testsdir = f"{workdir}/tests" if workdir else "tests"

solution, solution_path = None, None
for fe in scandir(workdir):
    if fe.is_file() and fe.name.endswith('.py') and not fe.name.startswith('_'):
        solution, solution_path = fe.name, fe.path
        break

if solution is None:
    print("No solution found")
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
        subproc = run([solution_path], stdin=f, text=True, shell=True, capture_output=True)
    if subproc.returncode != 0:
        print(subproc.stderr)
        continue
    result = subproc.stdout.splitlines(keepends=True)
    with open(f"{testsdir}/{testname}.out") as f:
        answer = f.readlines()
        for i in range(len(answer)):
            if i < len(result):
                if result[i].strip() != answer[i].strip():
                    ok = False
                    print(f"LINE {i+1}\n\t{answer[i]}\n\t{result[i]}")
            else:
                ok = False
                print("Missing line")
    if ok:
        print(f"Test '{testname}' CORRECT")
