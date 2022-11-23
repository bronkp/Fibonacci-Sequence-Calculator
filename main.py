print("FibSeq Calc")
try:
    steps = int(input("How many steps: "))
    if steps >= 100:
        print("WARNING-HIGH-VALUE-FAILURE")
    elif steps < 100:
        write_type = input("Overwrite(w) or Append(a): ")

        def FibCMD():
            x = 0
            if write_type == "a" or "w":
                file = open(r"C:\Users\Rory\Desktop\FibSeq\FibSeq.txt", str(write_type))
                true_steps = steps - 2

                def FibHeader():
                    file.write("\n===============\nFibSeq to " + str(steps) + " step(s)\n===============\n")
                if steps == 1:
                    FibHeader()
                    print(0)
                    a = 0
                elif steps > 1:
                    FibHeader()
                    seq_num1 = 0
                    seq_num2 = 1
                    print(seq_num1)
                    print(seq_num2)
                    a = 1
                    file.write("0\n1\n")
                    while x < true_steps:
                        x += 1
                        holding_num = seq_num2
                        step_sum = seq_num1 + seq_num2
                        a += step_sum
                        file.write(str(step_sum) + "\n")
                        print(step_sum)
                        seq_num2 = step_sum
                        seq_num1 = holding_num

                print("the sum of these steps equals:", a)


        if write_type == "w":
            warning_prompt = input("Warning-Are you sure you want to over ride existing data? (y/n): ")
            if warning_prompt == "n":
                print("Canceling Program")
            elif warning_prompt == "y":
                FibCMD()
            else:
                print("Invalid Response")
        elif write_type == "a":
            FibCMD()

        else:
            print("Invalid Write Type")
except ValueError:
    print("Error: Input Invalid")
