# -*- coding: utf-8 -*-
from inspect import signature
from functools import wraps
import traceback

import environment


def print_stack_trace():
    trace = traceback.format_exc()
    print(trace)
    return trace


def debug_info(msg: str):
    if environment.DEBUG:
        print(msg)
        print_stack_trace()


def typecheck(f):
    def do_type_check(name, arg):
        expected_type = f.__annotations__.get(name, None)
        if expected_type and not isinstance(arg, expected_type):
            raise RuntimeError(
                "{} should be of type {} instead of {}".format(name, expected_type.__name__, type(arg).__name__))

    @wraps(f)
    def wrapper(*args, **kwargs):
        for i, arg in enumerate(args[:f.__code__.co_nlocals]):
            do_type_check(f.__code__.co_varnames[i], arg)
        for name, arg in kwargs.items():
            do_type_check(name, arg)

        result = f(*args, **kwargs)

        do_type_check('return', result)
        return result

    return wrapper


def typeassert(*ty_args, **ty_kwargs):
    def decorate(func):
        # If in optimized mode, disable type checking
        if not __debug__:
            return func

        # Map function argument names to supplied types
        sig = signature(func)
        bound_types = sig.bind_partial(*ty_args, **ty_kwargs).arguments

        @wraps(func)
        def wrapper(*args, **kwargs):
            bound_values = sig.bind(*args, **kwargs)
            # Enforce type assertions across supplied arguments
            for name, value in bound_values.arguments.items():
                if name in bound_types:
                    if not isinstance(value, bound_types[name]):
                        raise TypeError(
                            'Argument {} must be {}'.format(name, bound_types[name])
                            )
            return func(*args, **kwargs)
        return wrapper
    return decorate
