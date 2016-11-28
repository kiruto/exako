# -*- coding: utf-8 -*-
import traceback


def print_stack_trace():
    trace = traceback.format_exc()
    print(trace)
    return trace
