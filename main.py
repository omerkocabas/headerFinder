import os
import shutil

def searcher(listOfHeaders, index):
    searchedHeaderName = listOfHeaders[index]
    #In case of invalid input, search next item in the header list.
    if searchedHeaderName == '/' or searchedHeaderName == "":
        searcher(listOfHeaders, index + 1)

    #Check if searched header exists in the directory of all header files.
    elif os.path.exists('Directory of all header files.' + searchedHeaderName):
        print(searchedHeaderName)
        with open('Directory of all header files.' + searchedHeaderName) as searchedHeaderFile:
            includeLines = []
            lines = searchedHeaderFile.readlines()
            #Gets all lines which has "#include" keyword in the opened header file.
            for line in lines:
                if '#include' in line:
                    includeLines.append(line)


            #Then remove "#include" words to get header names.
            includeWords = [words for segments in includeLines for words in segments.split()]
            for word in includeWords:
                if word == "#include":
                    includeWords.remove(word)

            #Get rid of double quotation mark.
            for i in range(len(includeWords)):
                size = len(includeWords[i]) - 1
                includeWords[i] = includeWords[i][1:size]

            #Add every included header in the opened file to get all list of headers.
            for word in includeWords:
                listOfHeaders.append(word)

            #Because opened document is already used, copy this file to a target directory.
            original = r'Path of directory which has all headers' + searchedHeaderName
            target = r'Empty directory path to paste used headers' + searchedHeaderName
            shutil.copyfile(original, target)
            #Check if there is duplicated headers in the list.
            listOfHeaders = list(dict.fromkeys(listOfHeaders))

            #Search until the end of the list.
            if index < len(listOfHeaders) - 1:
                searcher(listOfHeaders, index + 1)


    else:
        searcher(listOfHeaders, index + 1)


if __name__ == '__main__':
    #File that has used headers in your classes.
    #Assume that you include 30 header files, but those files include hundreds or thousands of headers.
    with open('Path of your text file which has your 30 header files.' ) as includedHeadersFile:
        lines = includedHeadersFile.readlines()
        #Remove duplicate lines.
        lines = list(dict.fromkeys(lines))

    #Spaces are removed and words are splitted. #include "example.h"       splitted as -> ["#include", ""example.h""]
    splittedWords = [words for segments in lines for words in segments.split()]
    for word in splittedWords:
        #       "#include" words are removed.
        if word == "#include":
            splittedWords.remove(word)

    #Double quotation marks have been removed from header names.
    for i in range(len(splittedWords)):
        size = len(splittedWords[i]) - 1
        splittedWords[i] = splittedWords[i][1:size]

    #Searcher function started to work.
    searcher(splittedWords, 0)