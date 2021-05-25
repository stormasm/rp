import ast
import inspect
import pprint


def slow_week():
    seconds_per_day = 86400
    return 7 * seconds_per_day


pprint.pprint(ast.dump(ast.parse(inspect.getsource(slow_week))))
