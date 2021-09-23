'''
Edel Barcenas
CS 341
DFA(Deterministic Finite Automaton) implementation
9/20/21
'''

letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'];

def q1(string):
    print(string);
    x = string[0];
    string = string[1:]+"%%";

    if x == '%': print("q1\nREJECTED"); return;
    print("q1",x);

    if x in letters: q2(string[0], string[1:]);
    else: q16(string[0],string[1:]);

def q2(x, string):
    if x == '%': print("q2\nREJECTED"); return;
    print("q2",x);

    if x in letters: q2(string[0], string[1:]);
    elif x == '@': q3(string[0], string[1:]);
    elif x == '.': q4(string[0], string[1:]);
    else: q16(string[0],string[1:]);

def q3(x, string):
    if x == '%': print("q3\nREJECTED"); return;
    print("q3",x);

    if x in letters: q6(string[0], string[1:]);
    else: q16(string[0],string[1:]);

def q4(x, string):
    if x == '%': print("q4\nREJECTED"); return;
    print("q4", x);

    if x in letters: q5(string[0], string[1:]);
    else: q16(string[0],string[1:]);

def q5(x, string):
    if x == '%': print("q5\nREJECTED"); return;
    print("q5", x);

    if x == '@': q3(string[0], string[1:]);
    elif x in letters: q5(string[0], string[1:]);
    else: q16(string[0],string[1:]);

def q6(x, string):
    if x == '%': print("q6\nREJECTED"); return;
    print("q6", x);

    if x in letters: q6(string[0], string[1:]);
    elif x == '.': q7(string[0], string[1:]);
    else: q16(string[0],string[1:]);

def q7(x, string):
    if x == '%': print("q7\nREJECTED"); return;
    print("q7", x);

    if x == 'n': q9(string[0], string[1:]);
    elif x in letters: q8(string[0], string[1:]);
    else: q16(string[0],string[1:]);

def q8(x, string):
    if x == '%': print("q8\nREJECTED"); return;
    print("q8", x);

    if x in letters: q8(string[0], string[1:]);
    elif x == '.': q12(string[0], string[1:]);
    else: q16(string[0],string[1:]);

def q9(x, string):
    if x == '%': print("q9\nREJECTED"); return;
    print("q9", x);

    if x == 'e': q10(string[0], string[1:]);
    elif x in letters: q8(string[0], string[1:]);
    elif x == '.': q12(string[0], string[1:]);
    else: q16(string[0],string[1:]);

def q10(x, string):
    if x == '%': print("q10\nREJECTED"); return;
    print("q10", x);

    if x == 't': q11(string[0], string[1:]);
    elif x in letters: q8(string[0], string[1:]);
    elif x == '.': q12(string[0], string[1:]);
    else: q16(string[0],string[1:]);

def q11(x, string):
    if x == '%': print("q11\nACCEPTED"); return;
    print("q11", x);

    if x == '.': q12(string[0], string[1:]);
    elif x in letters: q8(string[0], string[1:]);
    else: q16(string[0],string[1:]);

def q12(x, string):
    if x == '%': print("q12\nREJECTED"); return;
    print("q12", x);

    if x == 'n': q13(string[0], string[1:]);
    else: q16(string[0],string[1:]);

def q13(x, string):
    if x == '%': print("q13\nREJECTED"); return;
    print("q13", x);

    if x == 'e': q14(string[0], string[1:]);
    else: q16(string[0],string[1:]);

def q14(x, string):
    if x == '%': print("q14\nREJECTED"); return;
    print("q14", x);

    if x == 't': q15(string[0], string[1:]);
    else: q16(string[0],string[1:]);

def q15(x, string):
    if x == '%': print("q15\nACCEPTED");
    else: q16(string[0],string[1:]);

def q16(x, string):
    if x == '%':
        print("q16\nREJECTED");
    else:
        print("q16", x);
        q16(string[0],string[1:]);

def printHeader():
    print("Project 1 for CS 341");
    print("Section Number: 003 ");
    print("Written by: Edel Barcenas, eeb24");
    print("Instructor: Marvin Nakayama, marvin@njit.edu");

def tester():
    file = open("tests.txt",'r');
    output = open("output.txt", 'w');
    for line in file:
        q1(line.strip('\n'));
        print();

    file.close();
    output.close();

def main():
    printHeader();

    play = input("Do you want to input a string?(y/n): ");
    if play == 'y':
        string = input("Enter string over Σ: ");
        q1(string)
    elif play == 'n':
        return;
    else:
        print("Must input 'y' or 'n'");


#tester()
main();

