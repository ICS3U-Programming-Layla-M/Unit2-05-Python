#!/usr/bin/env python3

# Created by: Mr. Coxall
# Created on: Sept 2019
# Modified by: Layla Michel
# Modified on: May 6, 2021
# This program shows how local and global variables work

# global variable
variable_X = 5


def local_variable():
    # this shows what happens with local variables

    variable_X = 38
    variable_Y = 22
    variable_Z = variable_X + variable_Y
    print("Local variable_X, variable_Y, variable_Z: {0} + {1} = {2}".
          format(variable_X, variable_Y, variable_Z))


def global_variable():
    # this shows what happens with global variables

    global variable_X
    variable_X = variable_X + 1
    variable_Y = 17
    variable_Z = variable_X + variable_Y
    print("Global variable_X, variable_Y, variable_Z: {0} + {1} = {2}".
          format(variable_X, variable_Y, variable_Z))


def main():
    # this function shows how local and global variables work

    local_variable()
    global_variable()


if __name__ == "__main__":
    main()
