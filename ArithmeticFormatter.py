def arithmetic_arranger(problems, show_answers=False):
  #Rule 1: Max problems. The limit is five
  if len(problems) > 5:
    return "Error: Too many problems."

  arranged_problems = ""
  first_line = ""
  second_line = ""
  dash_line = ""
  answer_line = ""
  a = []
  for problem in problems:
    #lets start spliting the strings into single number-strings and operator
    elements = problem.split()
    num1 = elements[0]
    operator = elements[1]
    num2 = elements[2]
    #Rule 2: The appropriate operators the function will accept are addition and subtraction. Multiplication and division will return an error
    if operator not in ['+', '-']:
      return "Error: Operator must be '+' or '-'."
    #Rule 3: Each number (operand) should only contain digits
    if not (num1.isdigit() and num2.isdigit()):
      return "Error: Numbers must only contain digits."
    #Rule 4: Each operand  has a max of four digits in width.
    if len(num1) > 4 or len(num2) > 4:
      return "Error: Numbers cannot be more than four digits."
    #String to return a two-line format by default. The second line should be the operator
    width = max(len(num1), len(num2)) + 2
    a.append(width)
    first_line += num1.rjust(width) + "    "
    second_line += operator + num2.rjust(width - 1) + "    "
    dash_line += "-" * width + "    "
    #Optional parameter to show results
    if show_answers:
      if operator == '+':
        answer = str(int(num1) + int(num2))
      else:
        answer = str(int(num1) - int(num2))
      answer_line += answer.rjust(width) + "    "

  arranged_problems += first_line.rstrip() + "\n"
  arranged_problems += second_line.rstrip() + "\n"
  arranged_problems += dash_line.rstrip()
  if show_answers:
    arranged_problems += "\n" + answer_line.rstrip()

  return arranged_problems


""" Conditions:
Situations that will return an error:
  1) If there are too many problems supplied to the function. The limit is five, anything more will return: Error: Too many problems. 
  2) The appropriate operators the function will accept are addition and subtraction. Multiplication and division will return an error. Other operators not mentioned in this bullet point will not need to be tested. The error returned will be: Error: Operator must be '+' or '-'. 
  3) Each number (operand) should only contain digits. Otherwise, the function will return: Error: Numbers must only contain digits. 
  4) Each operand (aka number on each side of the operator) has a max of four digits in width. Otherwise, the error string returned will be: Error: Numbers cannot be more than four digits. 
  
  If the user supplied the correct format of problems, the conversion you return will follow these rules:
  There should be a single space between the operator and the longest of the two operands, the operator will be on the same line as the second operand, both operands will be in the same order as provided (the first will be the top one and the second will be the bottom).
  Numbers should be right-aligned.
  There should be four spaces between each problem.
  There should be dashes at the bottom of each problem. The dashes should run along the entire length of each problem individually. (The example above shows what this should look like.)
"""