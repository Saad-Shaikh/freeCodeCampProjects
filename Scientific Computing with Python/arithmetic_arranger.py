def arithmetic_arranger(problems, answers=False):
  arranged_problems = "";
  if len(problems)>5:
    return "Error: Too many problems."
  
  first = {}
  op = {}
  second = {}
  count = 0
  if answers:solutions = {}

  for problem in problems:
    temp = problem.split(' ')
    if len(temp[0])>4 or len(temp[2])>4 :
      return "Error: Numbers cannot be more than four digits."
    
    if temp[1]!='+' and temp[1]!='-' :
      return "Error: Operator must be '+' or '-'."
    
    try:
      int(temp[0])
      int(temp[2])
      first[count] = temp[0]
      op[count] = temp[1]
      second[count] = temp[2]
    except:
      return "Error: Numbers must only contain digits."
      
    if answers:
      if op[count]=='+':
        solutions[count] = int(first[count]) + int(second[count])
      elif op[count]=='-':
        solutions[count] = int(first[count]) - int(second[count])
  
    count += 1
  
  line1 = ""
  line2 = ""
  line3 = ""
  solLine = ""
  for i in range(len(first)):
    maxLen = len(first[i])+2 if len(first[i])>=len(second[i]) else len(second[i])+2

    if maxLen == len(first[i]):
      line1 += first[i].rjust(maxLen) + "    "
    else:
      line1 += first[i].rjust(maxLen) + "    "

    spaces = 1
    if len(second[i]) < len(first[i]):
      spaces += len(first[i]) - len(second[i])
    
    line2 += (op[i] + spaces*" " + second[i]).rjust(maxLen) + "    "
    line3 += (maxLen)*"-" + "    "
    if answers:
      solLine += str(solutions[i]).rjust(maxLen) + "    "

  arranged_problems = f'{line1.rstrip()}\n{line2.rstrip()}\n{line3.rstrip()}\n{solLine.rstrip()}\n'
  return arranged_problems.rstrip()