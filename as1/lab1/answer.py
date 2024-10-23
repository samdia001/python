from dbwebb import Dbwebb


# pylint: disable=invalid-name

dbwebb = Dbwebb()
dbwebb.ready_to_begin()



# ==========================================================================
# Lab 1 - python
#
# If you need to peek at examples or just want to know more, take a look at
# the [Python manual](https://docs.python.org/3/library/index.html).
#
# There you will find everything this lab will go through and much more.
#



# --------------------------------------------------------------------------
# Section 1. Integers, floats and basic arithmetics
#
# The foundation of numbers and basic arithmetic.
#



# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 1.1 (1 points)
#
# Create a variable called `num_one` and give it the value 89.
#
# Answer with the value of `num_one`.
#
# Write your code below and put the answer into the variable ANSWER.
#




num_one = 89

ANSWER = num_one

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("1.1", ANSWER, True)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 1.2 (1 points)
#
# Create another variable called `num_two` and give it the value 14. Create a
# third variable called `result` and assign to it the sum of the first two
# variables.
#
# Answer with the `result` variable.
#
# Write your code below and put the answer into the variable ANSWER.
#



num_two = 14
result = num_one + num_two


ANSWER = result

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("1.2", ANSWER, True)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 1.3 (1 points)
#
# Create a variable called `num_three` and give it the value 54.
#
# Create another variable called `num_four` and give it the value 37.
#
# Subtract `num_three` from `num_four` and add the `result` variable from
# above to result of the subtraction. Answer with the result.
#
# Write your code below and put the answer into the variable ANSWER.
#


num_three = 54
num_four = 37
result_of_sub = num_four -num_three

ANSWER = result + result_of_sub

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("1.3", ANSWER, True)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 1.4 (1 points)
#
# Answer with the result of a multiplication of `num_one` and `num_three`.
#
# Write your code below and put the answer into the variable ANSWER.
#






ANSWER = num_one * num_three

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("1.4", ANSWER, True)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 1.5 (1 points)
#
# Create a variable called `float_one` and give it the value 61.48.
#
# Create another variable called `float_two` and give it the value 23.17.
#
# Sum the two values and answer with the result, rounded to two decimals. Use
# the function `round()` to round the number to two decimals.
#
# Write your code below and put the answer into the variable ANSWER.
#


float_one = 61.48
float_two = 23.17


ANSWER = float_one + float_two

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("1.5", ANSWER, True)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 1.6 (1 points)
#
# All variables used in the exercise below are defined above.
#
# Sum `num_three` with `num_one` and subtract `num_four`. Multiply the result
# by `num_two`, add `float_two` and subtract `float_one`. Use the function
# `round()` to round the number to two decimals.
#
# Answer with the result.
#
# Write your code below and put the answer into the variable ANSWER.
#




procc =  (num_three + num_one- num_four)* num_two + float_two -float_one
rounded = round(procc, 2)
ANSWER = rounded

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("1.6", ANSWER, True)

# --------------------------------------------------------------------------
# Section 2. Strings and concatenation
#
#
#



# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 2.1 (1 points)
#
# Concatenate (svenska: konkatenera) the two words 'error' and 'barbeque' and
# answer with the result.
#
# Write your code below and put the answer into the variable ANSWER.
#



error = "error"
barbeque = "barbeque"

ANSWER = error + barbeque
# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("2.1", ANSWER, True)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 2.2 (1 points)
#
# Concatenate the word 'barbeque' with the integer 89, with a space between
# the two values.
# Answer with the new string.
#
# Write your code below and put the answer into the variable ANSWER.
#


integer = "89"
space= " "

ANSWER = barbeque + space + integer

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("2.2", ANSWER, True)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 2.3 (1 points)
#
# Concatenate the integer 89 with the word 'error' with a space between. To
# the resulting string concatenate the string ' and '. To this string
# concatenate integer 14 and the word 'barbeque' with a space between between
# the two values.
#
# Write your code below and put the answer into the variable ANSWER.
#





integer2 = "14"
adding = "and"
sentence1 = integer + space + error + space
sentence2 = integer2 + space + barbeque
ANSWER = sentence1 + adding +space+ sentence2
# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("2.3", ANSWER, True)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 2.4 (1 points)
#
# Assign the string value '30' to a variable called `string_number` and
# assign the integer value 5 to a variable called `actual_number`.
#
# Use `int()` to change the type of `string_number` to an integer and divide
# the integer value with `actual_number`. Answer with an integer by using the
# function `round()`.
#
# Write your code below and put the answer into the variable ANSWER.
#

string_number = "30"

actual_number = 5
change_type = int(string_number)
division = change_type / actual_number
ANSWER = round(division)

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("2.4", ANSWER, True)

# --------------------------------------------------------------------------
# Section 3. Extra assignments
#
# These questions are worth 3 points each. Solve them for extra points.
#



# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 3.1 (3 points)
#
# BTH is using a wind-turbine and solar panels to harvest energy from the
# wind and sun. On a windy and sunny day in September the sun shines for 10
# hours with an average output effect of the solar panels of 9345 W per hour.
# The wind turbine has an average output effect of 314 W per hour for all 24
# hours of the day.
#
# Calculate the total output energy i kWh from the wind turbine and the solar
# panels for the entire day.
#
# Energy i kWh is calculated as `energy = effect * hours / 1000`.
#
# Write your code below and put the answer into the variable ANSWER.
#

sun_shine = 10 #hours

sun_effect = 9345 #wh

wind_effect = 314 #wh

# converting from wh to kwh by dividing with 1000 after multipling with 24 (per day)

wind_energy_perADay = wind_effect * 24 / 1000

sun_energy_perADa = sun_effect * sun_shine / 1000

# Adding wind energy and sun energy.
total_energy_perADay = wind_energy_perADay + sun_energy_perADa


ANSWER = total_energy_perADay

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("3.1", ANSWER, True)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 3.2 (3 points)
#
# Peter has the phonenumber '0731415926' and Anna has the phonenumber
# '0727182818'. They call each other every sunday afternoon for 9 minutes.
#
# Calculate the number of hours that they talk with each other pr year
# (assume 52 sundays pr year). Use that number in a string concatenation with
# the following format:
#
# 'Peter calls from [#Peter's phonenumber] to Anna on [#Anna's phonenumber]
# for [#hours] hours every year.'
#
# Replace the content [#] with the corresponding values.
#
# Answer with the concatenated string.
#
# Write your code below and put the answer into the variable ANSWER.
#

Pn = "0731415926"
An= "0727182818"
# they talk for 9 minutes every week, 9*52 we get the number of minutes.
minutes = 9 * 52

# We can calculate hours by dividing with 60.
h = minutes / 60

ANSWER = f"Peter calls from {Pn} to Anna on {An} for {h} hours every year."

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("3.2", ANSWER, True)


dbwebb.exit_with_summary()
