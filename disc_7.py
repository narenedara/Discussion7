import re
import os
import unittest

def read_file(filename):
    """ Return a list of the lines in the file with the passed filename """
    
    # Open the file and get the file object
    source_dir = os.path.dirname(__file__) #<-- directory name
    full_path = os.path.join(source_dir, filename)
    infile = open(full_path,'r', encoding='utf-8')
    
    # Read the lines from the file object into a list
    lines = infile.readlines()
    
    # Close the file object
    infile.close()
    
    # return the list of lines
    return lines

def find_num_words(string_list):
    """ Return a list of words that contain three-digit numbers in the middle. """
    num_word_list=re.findall()
    # initialize an empty list
    num_words_list=[]
    # define the regular expression
    pattern=r"[a-zA-Z]+\d{3}[a-zA-z]+"
    # loop through each line of the string list 
    for s in string_list:

    # find all the words that match the regular expression in each line
        found= re.findall(pattern,s)
    # loop through the found words and add the words to your list
    num_words_list += found

    # return the list
    print(num_words_list)
    return num_words_list
    pass


def find_days(string_list):
    """ 
    Return a list of days from the list of strings
    The dates in the text are formatted as: MM/DD/YYYY
    Note: The month and date can one or two digits (ie: 01 or 1)
    """  

    # initialize an empty list
    days_list=[]


    # define the regular expression
    pattern=r"\b\d{1,2}/\d{1,2}/\d{4}\b"
    # loop through each line of the string list
    for s in string_list:
    
    # find all the dates that match the regular expression in each line
        find_list=re.findall(pattern,s)
    # loop through the found dates and only add the days to your list 
        for result in find_list:
            result_list+=result.split('/')
            days_list.append(result_list[1])
    #return the list of days
    return days_list
    pass

def find_domains(string_list):
    """ 
    Return a list of web address domains from the list of strings. 
    The web address may or may not have a www. and the protocol can either be http or https
    Example output: ['si.umich.edu', 'google.com']
    """

    # initialize an empty list
    domains_list=[]
    # define the regular expression
    pattern=r"https{0,1}://([a-z0-9]+.)+([a-z0-9])"
    # loop through each line of the string list
    for s in string_list:
    # find all the do  mains that match the regular expression in each line
        find_list=re.findall(pattern,s)
    # loop through the found domains
    for result in find_list:
    # get the domain name by pulling out the part of the string after the '//'
    # you'll also have to strip the 'www.' from domains where applicable
        
    # add the domains to your  list
    
    #return the list of domains
    pass

class TestAllMethods(unittest.TestCase):


    def test_find_num_words(self):
        # read the lines from the file into a list of strings
        string_list = read_file('alice_ch_1.txt')
        word_list = find_num_words(string_list)
        self.assertEqual(len(word_list),4)
    
    def test_find_days(self):
        # read the lines from the file into a list of strings
        string_list = read_file('alice_ch_1.txt')
        days_list = find_days(string_list)
        self.assertEqual(days_list,['23', '12', '31', '4', '1', '4'])
    
    def test_domains(self):
        # read the lines from the file into a list of strings
        string_list = read_file('alice_ch_1.txt')
        domain_list = find_domains(string_list)
        self.assertEqual(domain_list,['pythex.org', 'si.umich.edu', 'sabapivot.com', 'stars.chromeexperiments.com', 'theofficestaremachine.com', 'regex101.com'])


def main():
	# Use main to test your function. 
    # Run unit tests, but feel free to run any additional functions you need
	unittest.main(verbosity = 2)

if __name__ == "__main__":
	main()