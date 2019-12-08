from algorithm_efficiency_tool.tool_class import AlgorithmEfficiencyTool
from functools import wraps

def aet_decorator(data_params):# don't need data_size. The data_params represent n, The scratchpad.populate() will take a multiplier
    FET = AlgorithmEfficiencyTool(None)
    def inner_function(function):
        @wraps(function)
        def wrapper(*args, **kwargs):
            results =  FET.test_function(function, data_params)
            FET.print_test_results([results])
            return results
        return wrapper
    return inner_function