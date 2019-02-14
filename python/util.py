# Copyright 2017 anonymous
#
# This software is the result of a joint project between anonymous
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
#     Unless required by applicable law or agreed to in writing, software
#     distributed under the License is distributed on an "AS IS" BASIS,
#     WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#     See the License for the specific language governing permissions and
#     limitations under the License.

"""
Utility functions for the Python test scripts.

Author: anonymous
"""

from __future__ import print_function

import json
import os
import subprocess
import sys


def run_moonshine(cmd, corpus_dir, silent=False):
    """
    Run Moonshine with the given command list on the given corpus directory.
    """
    if silent:
        moonshine_stdout = subprocess.PIPE
    else:
        print('Running "{}"'.format(' '.join(cmd)))
        moonshine_stdout = sys.stdout

    moonshine = subprocess.Popen(cmd, stdout=moonshine_stdout,
                                 stderr=subprocess.PIPE)
    _, stderr = moonshine.communicate()

    # Return an error dict
    if stderr:
        return dict(error=stderr)

    # Get the solution
    solution_path = os.path.join(corpus_dir, 'moonshine_solution.json')
    with open(solution_path, 'r') as soln_file:
        return json.load(soln_file)



def check_results(results, expected):
    """
    Compare the two Moonshine results dictionaries: one from
    moonshine_solution.json and the other from the execpted result.
    """
    # Mapping of result keys to their data types
    keys_to_compare = dict(corpus_size=int,
                           solution_size=int,
                           solution_weight=float,
                           initial_singularities=int,
                           num_basic_blocks=int,
                           solution=set)
    passed = True
    fail_msg = ''

    for key, type_ in keys_to_compare.items():
        results_value = type_(results[key])
        expected_value = type_(expected[key])

        if results_value != expected_value:
            fail_msg = '{}\n    {}: {} v {}'.format(fail_msg,
                                                    key,
                                                    expected_value,
                                                    results_value)
            passed = False

    if passed:
        print('PASSED')
    else:
        print('FAILED {}'.format(fail_msg))

    return passed
