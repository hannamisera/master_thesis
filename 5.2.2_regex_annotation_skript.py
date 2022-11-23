#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 23 11:19:01 2022

@author: hannamisera
"""

import pandas as pd
import re
import numpy as np

def get_dataframe():
    """
    1. Asks for a csv file (and path if needed)
    2. returns "Success" if file has been successfully read
    3. returns an Error if the file was not found and restarts
    4. if successfully read this function returns the csv file as a pandas dataframe
    The following libraries are needed:
    pandas as pd
    """
    #ask for the dataframe
    while True:
        try:
            file = str(input("please enter the csv-file name and the path if needed"))
            df = pd.read_csv(file)
            print("---------------- \nSuccess\n----------------")
            break
        #Error handeling if file does not exists
        except FileNotFoundError:
                print("---------------- \nError: file not found\n----------------")
    return df

def get_column(df):
    """
    1. Needs a dataframe as input
    2. Asks for the column name that should be processed
    3. Checks if column name exists in dataframe
    4. Returns "Success" if column name exists
    5. Returns an Error if the column name doesn't exist and restarts
    6. Returns the columnname as a string
    The following libraries are needed:
    pandas as pd
    """
    #ask for the columnname as an input
    while True:
        columnname = str(input("Please define the columnname where your text exists"))
        #check if columnname exists
        if columnname in df.columns:
            print("---------------- \nColumnname successfully defined\n----------------")
            break
        else:
            print("---------------- \nError: columnname not found\n----------------")
    # return the columnname
    return columnname

def preprocessing_text(df, col):
    """
    Uses a dataframe and preprocesses the text in the given column.
    1. replace some chars
    2. Creates two new column (job_desc, communication) and fills up the columns wit np.nan
    The following libraries are needed:
    pandas as pd
    numpy as np
    """
    #replace some chars
    df["clean"] = df[col].str.replace("-\n","")
    df["clean"] = df["clean"].str.replace("⸗\n","")
    df["clean"] = df["clean"].str.replace("#"," ")
    df["clean"] = df["clean"].str.replace("\n", " ")
    df["clean"] = df["clean"].str.replace("'","")
    df["clean"] = df["clean"].str.replace('"',"")
    df["clean"] = df["clean"].str.replace(",,","")
    df["clean"] = df["clean"].str.replace("„","")
    df["clean"] = df["clean"].str.replace("ſ", "s")
    df["clean"] = df["clean"].str.replace("é","e")
    df["clean"] = df["clean"].str.replace("è","e")
    df["clean"] = df["clean"].str.replace("á","a")
    df["clean"] = df["clean"].str.replace("à","a")
    
    # learning from phase 2
    df["clean"] = df["clean"].str.replace(",","")
    
    df["job_desc"] = np.nan
    df["communication"] = np.nan
    return df

def return_list_as_dataframe(lst, define_columnname):
    """
    Transfigures a list into a dataframe with one column and an index
    1. Needs a list as input
    2. Needs the columnname as a string to name the column of the dataframe
    3. returns the dataframe
    The following libraries are needed:
    pandas as pd
    """
    df_lst = pd.DataFrame(data={define_columnname: lst})
    return df_lst

def get_frequency_of_Words_in_column(df_lst, columnname):
    """
    Manipulates a dataframe with a text column to show the frequency of the values in one column
    1. Needs a dataframe as input
    2. Needs the columnname with text as input
    3. Creates a new column "Frequency"
    4. Groups the dataframe by the columnname and counts similar values
    5. Manipulates dataframe where the defined columnname embodies a set of all values and 
    "Frequency" embodies the frequency of the values
    6. Sort all rows by "Frequency"
    7. Returns the manipulated dataframe
    
    The following libraries are needed:
    pandas as pd
    """
    df_lst['Frequenz'] = df_lst.groupby(columnname)[columnname].transform('count')
    df_lst = df_lst.drop_duplicates()
    df_lst = df_lst.sort_values(by=['Frequenz'], ascending=False)
    
    return df_lst



def process_rows(df):
    """
    This function is combining several functions to process the rows of the given dataframe to annotate the text found in the cleaned text-column "clean" - created by the function preprocessing_text ()
    1. needs a dataframe as an input
    2. creates a list container for correction-words the user types in if the program does not do the right annotation
    3. iterates through the rows of the dataframe column "clean" using the index
    4. calls the function "process_row" to process every row and saves it in a variable "output"
    5. checks if the user defines the suggested annotation is ok by calling annotation_is_ok()
    6. While annotation_is_ok(output)== False the output stays the same
    7. While annotation_is_ok(output)== True the user will be asked to copy the first words of the second part of the text in an input field
        - This text is going to be saved in the list "valid_tricky_words"
        - a new output will be created by using this text
    8. New columns are created by the function add_new_cols()
    9. Function asks if the user wants to end the program by calling function early_end()
    10. If early_end()==True the function breaks and returns the dataframe and the vaid_tricky_words list
    11. If early_end() == False the function continues with the next row
    
    Refers to the following functions in this script:
    - process_row()
    - annotation_is_not_ok()
    - get_tricky_words()
    - add_new_cols()
    - early end()
    
    Used in:
    - main()
    
    The following libraries are needed:
    pandas as pd
    """
    # container of tricky words to save all tricky words during the loops and saves it by exit the script
    valid_tricky_words = []
    for i in df.index:
        text = df["clean"][i]
        print('\nProcessing row...\n')
        output = process_row(text, False)
        while (annotation_is_not_ok(output)):
            tricky_words = get_tricky_words()
            valid_tricky_words.append(tricky_words)
            output = process_row(text, tricky_words)
        df = add_new_cols(df, i, output)
        if (early_end()):
            break;
    return {'df': df, 'valid_tricky_words': valid_tricky_words}

def process_row(text, tricky_words):
    """
    1. needs text input and tricky_words from process_rows()
    2. uses the variable text from process_rows()
    3. calls get_regex() and saves it in a variable if tricky_words == True it used the word_sequence from the user
    4. returns a dict with the two key "job_desc" and "communication"
    5. creates two strings as values by calling the functions get_job_desc() and get_communication()
    
    Refers to the following functions in this script:
    - get_regex()
    - get_job_desc()
    - get_communication()
    
    Used in: 
    - process_rows()
    """
    regex = get_regex(tricky_words)
    return {
        'text': text,
        'job_desc': get_job_desc(regex, text),
        'communication': get_communication(regex, text)
    }

def get_regex(tricky_words):
    """
    1. provides the default regexes for the job ad and the communication
    2. defines a regex_default by creating two captured groups (job ad, communication) with format()
        - re_text is always applied and captured in the group "job_desc"
        - re_address, re_street, re_id_number are arranged hierarchically
    3. if tricky_words == True it defines a regex_tricky_words with captured groups (job, communication)
    4. returns regex_default if tricky_words == False, else returns re_tricky_words
    
    Used in: 
    - process_row()
    """
    #collect all the starting text in a non-greedy way
    re_text = '(.)*?'
    # address has different forms
    # No arabic numbers; no comma
    re_address = '\s[VIX]+[.]?\s.+$'
    re_street = '(\s\w+)\s?\W?([gG]asse|[sS]tra(ss|ß)e|[wW]eg|[pP]latz|[pP]fad|[uU]fer|[aA]llee|[aA]nlage|[gG]raben|[cC]haussee|[wW]ache|[pP]romenade|[pP]forte|[dD]amm|[tT]or|[bB]rücke|[rR]ing|[lL]ände)\s(.+$)'
    #([.]?\d+) excluded
    re_id_number = '\s?\d+\s?[-]?\d+\w?\W?\s*$'
    # Hyphen and some more variations (1non-word character, 1 letter) allowed or several spaces at the end 
    
    #final regex
    #default case
    regex_default = "^(?P<job_desc>{})(?P<communication>{}|{}|{})".format(re_text, re_address, re_street, re_id_number).format(re_text,re_address,re_street) 
    #tricky words case
    re_tricky_words = "{}.*".format(tricky_words)
    regex_tricky_words = "^(?P<job_desc>{})(?P<communication>{})".format(re_text,re_tricky_words) 
    return regex_tricky_words if tricky_words else regex_default


def apply_regex(regex, text):
    """
    Function to apply the regex (variable with string) by using the function search() from the re-module
    1. needs a regex in form of a string
    2. needs a text in form of a string
    3. returns the text grouped by regex (groups: job_desc; communication)case sensitivity is ignored
    
    Used in:
    - get_job_desc
    - get_communication
    
    The following libraries are needed:
    re
    """
    return re.search(regex, text, re.IGNORECASE)

def get_job_desc(regex, text):
    """
    Uses the function group() from the re-module to get the subgroup "job_desc" defined in get_regex()
    1. needs a regex in form of a string
    2. needs a text in form of a string
    3. returns the sub-group "job_desc" as a string
    Refers to:
    - apply_regex()
    Used in:
    - process_row()
    
    The following libraries are needed:
    re
    """
    if apply_regex(regex, text) is None:
        return None
    
    return apply_regex(regex, text).group('job_desc')

def get_communication(regex, text):
    """
    Uses the function group() from the re-module to get the subgroup "communication" defined in get_regex()
    1. needs a regex in form of a string
    2. needs a text in form of a string
    3. returns the sub-group "communication" as a string
    Used in:
    - process_row()
    
    The following libraries are needed:
    re
    """
    if apply_regex(regex, text) is None:
        return None
    
    return apply_regex(regex, text).group('communication')

def annotation_is_not_ok(output):
    """
    1. Needs the output defined in process_rows()
    2. Prints out the suggested annotations job_desc and communication
    3. asks if the annotation is OK
    4. returns answer (True|False) 
    
    Used in:
    - process_rows()
    
    The following libraries are needed:
    pandas as pd
    """
    print(('\n\nGesamte Stellenanzeige: \n >{}\n\n'.format(output['text'])))
    print('Stellenbeschreibung: \n >{}\n\n'.format(output['job_desc']))
    print('Kommunikationsbeschreibung: \n >{}\n\n'.format(output['communication']))
    print('')
    # asks if the separation is OK. True is not OK, False is OK
    while True:
        answer = str(input("\nIs there a mistake in the annotation? (Y/N)\n"))
        if answer == "Y": 
            return True
        elif answer == "N": 
            return False



def get_tricky_words():
    """
    1. Asks for text input
    2. Returns text input as astring 
    
    Used in:
    - process_rows()
    """
    # ask for the new words and returns them as string
    return str(input("\nPlease copy the first two words of the second text part and save it here.\nIf the text cannot be annotated in two parts, please write a dollar sign '$' in the field. \n"))

def add_new_cols(df, idx, output):
    """
    1. Needs the dataframe
    2. Needs the index from process_rows()
    3. Needs the output from process_rows()
    4. Commands the column "job_desc" with the defined index to save the value from the key "job_desc", defined in process_row
    5. Commands the column "communication" with the defined index to save the value from the key "communication", defined in process_row
    6. Returns the dataframe
    
    Used in:
    - process_rows()
    
    The following libraries are needed:
    pandas as pd
    """
    df.loc[df.index[idx], "job_desc"] = output["job_desc"]
    df.loc[df.index[idx], "communication"] = output["communication"]
    return df

def early_end():
    """
    1. Asks for an (Y/N) input
    2. Returns True if input == "Y" and False if input == "N"
    Used in:
    - process_rows()
    """
    
    # ask if the user want to finish now
    # True to end now, False to continue with
    # the next row
    while True:
        decision = str(input("\nDo you want to stop the program? (Y/N)\n"))
        if decision == "Y":
            print("\n\nThank you for using this program. Be aware that the annotated korpus is now available in the csv-file 'output.csv' in the same folder as this script.\nYou will also find a csv file with all copied word sequences and their frequencies you put in correcting this program. \nIf you want to use this program again please save it in a new folder to avoid overwrite the current output.\n\n")
            return True
        elif decision == "N":
            return False
        else:
            print("\n*** Wrong Command ***\n") 
            
# run main program
def main():
    df = get_dataframe()
    col = get_column(df)
    #text preprocessing
    df = preprocessing_text(df, col)
    #process each row of the dataframe and save the annotated groups in several columns
    output = process_rows(df)
    #export output as csv
    output['df'].to_csv('output.csv', index=False)
    #save valid_tricky_words in dataframe
    valid_tricky_words = output['valid_tricky_words']
    df_tricky_words = return_list_as_dataframe(valid_tricky_words, "Wörter")
    #manipulate dataframe to show the frequencys of the value sets
    df_tricky_words = get_frequency_of_Words_in_column(df_tricky_words, "Wörter")
    #export as csv
    df_tricky_words.to_csv('num_of_tricky_words.csv', index=False)
    
    print('correction words: ', output['valid_tricky_words'])


# run main program
main()  