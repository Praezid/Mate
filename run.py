import os
import importlib.util
import types
from inspect import getmembers, isfunction, getmodulename, signature, ismethod, getargs

passed_tests_count = 0
failed_tests_count = 0


def tester():
    global passed_tests_count
    global failed_tests_count
    this_dir = os.getcwd()
    print("\t---Start tests outputs---")
    for r, d, f in os.walk(this_dir):
        for file in f:
            if file.startswith("test_happy") and file.endswith(".py"):
                module_path = os.path.join(r, file)
                module_name = getmodulename(module_path)

                spec = importlib.util.spec_from_file_location(module_name, module_path)
                module = importlib.util.module_from_spec(spec)

                spec.loader.exec_module(module)

                for func in getmembers(module, isfunction):
                    try:
                        # if test_func have args
                        func[1](*signature(func[1]).parameters.keys())
                        passed_tests_count += 1
                    except Exception as e:
                        failed_tests_count += 1
                        print(f"Run {func[0]} failed")
                        print(f"Traceback: {str(e)}")
    print("\t---End tests outputs---")


def tester1():
    global passed_tests_count
    global failed_tests_count
    this_dir = os.getcwd()
    print("\t---Start tests outputs---")
    for r, d, f in os.walk(this_dir):
        for file in f:
            if file.startswith("test_parity") and file.endswith(".py"):
                module_path = os.path.join(r, file)
                module_name = getmodulename(module_path)

                spec = importlib.util.spec_from_file_location(module_name, module_path)
                module = importlib.util.module_from_spec(spec)

                spec.loader.exec_module(module)

                for func in getmembers(module, isfunction):
                    try:
                        # if test_func have args
                        if func[1].find('pytestmark') != None:
                        passed_tests_count += 1
                    except Exception as e:
                        failed_tests_count += 1
                        print(f"Run {func[0]} failed")
                        print(f"Traceback: {str(e)}")
    print("\t---End tests outputs---")


if __name__ == "__main__":
    print('Run tests...')
    tester1()
    print(f"\tPassed -{passed_tests_count:^7}- tests\n\tFailed -{failed_tests_count:^7}- tests")
