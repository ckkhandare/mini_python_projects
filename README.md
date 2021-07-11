# mini_python_projects
mini python programs to put your logic and understanding to the test

## List of Content -> problem statements
1) calander -> Write a program that asks the user how many days are in a particular month, and what day of the
   week the month begins on (0 for Monday, 1 for Tuesday, etc), and then prints a calendar for that 
   month.

2) cipher -> In cryptography, a Caesar cipher is a very simple encryption techniques in which each letter in the
   plain text is replaced by a letter some fixed number of positions down the alphabet. For example, with 
   a
   shift of 3, A would be replaced by D, B would become E, and so on. The method is named after Julius
   Caesar, who used it to communicate with his generals. ROT-13 ("rotate by 13 places") is a widely 
   used

3) cleanstring -> Define a simple "spelling correction" function correct() that takes a string and sees to it that
    1) two or more occurrences of the space character is compressed into one, and
    2) inserts an extra space after a period if the period is directly followed by a letter.
    e.g. correct("This is very funny and cool.Indeed!")
    should return "This is very funny and cool. Indeed!"

4) factorial -> Write a program that contains a function that has one parameter, n, representing an integer 
   greater
   than 0. The function should return n! (n factorial). Then write a main function that calls this function 
   with
   the values 1 through 20, one at a time, printing the returned results. This is what your output should 
   look

5) filter_longeststring -> Write a function filter_long_words() that takes a list of words and an integer n and returns the 
   list of words that are longer than n

6) histogram -> Define a procedure histogram() that takes a list of integers and prints a histogram to the screen

7) longestString ->  Write a function find_longest_word() that takes a list of words and returns the length of the 
   longest one.

8) mymoviedata -> Complete following program
   import pandas as pd
   mymoviedata=pd.read_table("http://bit.ly/movieusers",sep="|",header=None)
   print(mymoviedata.head())
   # add headings to the column- sr.no,age,Gender,profession,Views
   #display only column gender
   #add col6 concatenate values of age and gender and seperate them by :
   # retrieve values of age and views display bar graph
   # retrieve values of profession and views display bar graph


9) overlapping -> Define a function overlapping() that takes two lists and returns True if they have at least one
    member in common, False otherwise.


10) palindrome -> Write a version of a palindrome recognizer that also accepts phrase palindromes such as 
    "Go hang a salami I'm a lasagna hog.", "Was it a rat I saw?", "Step on no pets", "Sit on a potato pan, 
    Otis",

11) panagram -> A pangram is a sentence that contains all the letters of the English alphabet at least once, for
    example: The quick brown fox, jumps over the lazy dog!!!!. 
    Your task here is to write a function to check a
    sentence to see if it is a pangram or not.

12) recursive -> Write a recursive sum from 1 to x (i.e. 1 + 2 + ... + x) recursively as follows for integer x ≥ 1:
    1, if x = 1
    x + sum from 1 to x-1 if x > 1
    Complete the following Python program to compute the sum 1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9 + 10

13) sales -> #create a list for storing year 2010 to 2014
    #create a list for each year for storing sales amount for 5 products in each years
    #draw pie chart and stack graph to compare sales
    1. Yearly comparison
    Year and max sale in each year
    2. Draw separate graph for each year(5 different pie charts)
    Product and average sale of that product

14) students ->  Given a dictionary of students and their favourite colours:
    people={'Arham':'Blue','Lisa':'Yellow',''Vinod:'Purple','Jenny':'Pink'}
    1. Find out how many students are in the list
    2. Change Lisa’s favourite colour
    3. Remove 'Jenny' and her favourite colour
    4. Sort and print students and their favourite colours alphabetically by name

15) translate -> Write a function translate() that will translate a text into "rövarspråket" (Swedish for "robber's 
    language").
    That is, double every consonant and place an occurrence of "o" in between. For example, 
    translate("this
    is fun") should return the string "tothohisos isos fofunon".

16) vowel -> In English, present participle is formed by adding suffix -ing to infinite form: go -> going. A 
    simple set
    of heuristic rules can be given as follows:
    If the verb ends in e, drop the e and add ing (if not exception: be, see, flee, knee, etc.)
    If the verb ends in ie, change ie to y and add ing
    For words consisting of consonant-vowel-consonant, double the final letter before adding ing
    By default just add ing
    Your task in this exercise is to define a function make_ing_form() which given a verb in infinitive form
    returns its present participle form. Test your function with words such as lie, see, move and hug.



