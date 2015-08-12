#!/usr/bin/env python
# HW02_ex03_05

# This exercise can be done using only the statements and other features we 
# have learned so far.

# (1) Write a function that draws a grid like the following:
# + - - - - + - - - - +
# |         |         |
# |         |         |
# |         |         |
# |         |         |
# + - - - - + - - - - +
# |         |         |
# |         |         |
# |         |         |
# |         |         |
# + - - - - + - - - - +
# Hint: to print more than one value on a line, you can print a comma-separated
# sequence:

# print '+', '-'
# If the sequence ends with a comma, Python leaves the line unfinished, so the 
# value printed next appears on the same line.

# print '+', 
# print '-'

# The output of these statements is '+ -'.

# A print statement all by itself ends the current line and goes to the next line.

# (2) Write a function that draws a similar grid with four rows and four columns.
################################################################################
# Write your functions below:

def print_horizontal():
	print "+", "- - - -",

def print_bar():
	print "|        ",

def build_horizontal(f):
	f()
	f()
	print "+"

def build_four_by_four_horizontals(f):
	f()
	f()
	f()
	f()
	print "+"

def build_bars(f):
	f()
	f()
	print "|"

def build_four_by_four_bars(f):
	f()
	f()
	f()
	f()
	print "|"

def do_four(f, fun_):
	f(fun_)
	f(fun_)
	f(fun_)
	f(fun_)



def two_by_two(f1, f2, f3, f4, f5):
	f1(f2)
	f3(f4, f5)
	f1(f2)
	f3(f4, f5)
	f1(f2)


def four_by_four(f1, f2, f3, f4, f5):
	f1(f2)
	f3(f4, f5)
	f1(f2)
	f3(f4, f5)
	f1(f2)
	f3(f4, f5)
	f1(f2)
	f3(f4, f5)
	f1(f2)


# Write your functions above:
################################################################################
def main():
    """Call your functions within this function.
    When complete have two function calls in this function:
    two_by_two()
    four_by_four()
    """
    two_by_two(build_horizontal, print_horizontal, do_four, build_bars, print_bar)
    four_by_four(build_four_by_four_horizontals, print_horizontal, do_four, build_four_by_four_bars, print_bar)
    print("Hello World!")
    



if __name__ == "__main__":
    main()