def arithmetic_arranger(problems, show_answers=False):
    #prereq check
    if len(problems) > 5:
        return 'Error: Too many problems.'
    
    #one problem at a time
    row_1 = ''
    row_2 = ''
    row_3 = ''
    row_4 = ''
    equation_spacing = '    '
    for problem in problems:

        terms = problem.split()

        num_1 = terms[0]
        
        num_2 = terms[2]

        if not num_1.isdigit() or not num_2.isdigit():
            return 'Error: Numbers must only contain digits.'

        operator = terms[1]

        if operator == '+':
            result = str(int(num_1) + int(num_2))
        elif operator == '-':
            result = str(int(num_1) - int(num_2))
        else:
            return "Error: Operator must be '+' or '-'."

        length = max(len(num_1), len(num_2)) + 2
        if length - 2 > 4:
            return 'Error: Numbers cannot be more than four digits.'


        #find the length of the total problem

        num_1_space = length-len(num_1)
        num_2_space = length-len(num_2)-1
        result_space = length-len(result)
        row_2 += operator

        for i in range (length):
            if i < num_1_space:
                row_1 += ' '
            if i < num_2_space:
                row_2 += ' '
            row_3 += '-'
            if i < result_space:
                row_4 += ' '

                
        row_1 += num_1 + equation_spacing
        row_2 += num_2 + equation_spacing
        row_3 += equation_spacing
        row_4 += result + equation_spacing
    row_1 = row_1[:-4]
    row_2 = row_2[:-4]
    row_3 = row_3[:-4]
    row_4 = row_4[:-4]

    if not show_answers:
        row_4 = ''
        return row_1+'\n'+row_2+'\n'+row_3
    else:
        return row_1+'\n'+row_2+'\n'+row_3+'\n'+row_4
  

print(f'\n{arithmetic_arranger(["3801 - 2", "123 + 49"])}')

  #  3801      123/n-    2    +  49/n------    -----/n  
  #  3801      123\n-    2    +  49\n------    -----