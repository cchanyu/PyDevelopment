target = " nei "
replace_with = " neighbor "
with open('input.txt', 'r') as f_in, open('output.txt', 'w') as f_out:
    for line in f_in:
        new_line = line.replace(target, replace_with)
        f_out.write(new_line)
