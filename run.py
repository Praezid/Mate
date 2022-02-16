import os
import importlib.util
from inspect import getmembers, isfunction, getmodulename

thisdir = os.getcwd()

for r, d, f in os.walk(thisdir):
    for file in f:
        if file.startswith("test_") and file.endswith(".py"):
            module_path = os.path.join(r, file)
            module_name = getmodulename(module_path)
            spec = importlib.util.spec_from_file_location(module_name, module_path)
            module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(module)
            for func in getmembers(module, isfunction):
                try:
                    func[1]()
                except Exception as e:
                    print(f"Run {func[0]} failed")
                    print(f"Traceback: {str(e)}")
