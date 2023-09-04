import solver as sv

def kociemba():
    print("""
        \nThe facelet positions of the cube should be like this\n
                     |************|
                     |*W1**W2**W3*|
                     |************|
                     |*W4**W5**W6*|
                     |************|
                     |*W7**W8**W9*|
                     |************|
        |************|************|************|************|
        |*O1**O2**O3*|*G1**G2**G3*|*R1**R2**R3*|*B1**B2**B3*|
        |************|************|************|************|
        |*O4**O5**O6*|*G4**G5**G6*|*R4**R5**R6*|*B4**B5**B6*|
        |************|************|************|************|
        |*O7**O8**O9*|*G7**G8**G9*|*R7**R8**R9*|*B7**B8**B9*|
        |************|************|************|************|
                     |************|
                     |*Y1**Y2**Y3*|
                     |************|
                     |*Y4**Y5**Y6*|
                     |************|
                     |*Y7**Y8**Y9*|
                     |************|""")
    a = ("Your face orientation should be:\n  W-color in upward face \n  R-color in right face \n  G-color in front face \n  Y-color in downward face \n  O-color in left face \n  B-color in backward face")
    print(a)
    print("""\nThe color configuration should be like:
            WWWWWWWWRRRRRRRRRGGGGGGGGGYYYYYYYYYOOOOOOOOOBBBBBBBBB""")

    solutionBlock = True
    while (solutionBlock):
        inputString = str(input("\nEnter your cube's color configuratioin: ")).upper()
        try:
            if (inputString[4] == 'W' and inputString[13] == 'R' and inputString[22] == 'G' and inputString[31] == 'Y' and inputString[40] == 'O' and inputString[49] == 'B'):
                print(sv.solve(inputString))
                responseBlock = True
                while(responseBlock):
                    response = str(input("Do you want to continue?(Y/N): ")).upper()
                    print('\n')
                    if(response == "Y"):
                        responseBlock = False
                    elif(response == "N"):
                        responseBlock = False
                        solutionBlock = False
                    else:
                        print("Invalid choice")
            else:      
                b = ("But founds to be:\n  "+inputString[4] +"-color in upward face \n  "+inputString[13] +"-color in right face \n  "+inputString[22] +"-color in front face \n  "+inputString[31] +"-color in downward face \n  "+inputString[40] +"-color in left face \n  "+inputString[49] +"-color in backward face")
                print("Invalid input: ")
                print(a)
                print(b)
                continue
        except:
            print("Invalid input")
            continue
kociemba()
