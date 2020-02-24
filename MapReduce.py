# CS 1190 Parallel Computing
# Stephanie Galvan

# Count the numbers of occurrences of a given word in
# Shakespeare's works by using parallel

import argparse
import pymp
import time
import re

def MapReduce(total_threads):
    start = time.time()
    file_list = getFilenames()
    loaded_files = []

    #Files are loaded and ready to be read
    for file in file_list:
        loaded_files.append(file.read())
    end = time.time()
    print("Loading files runtime:", end - start, "s")

    words = getWords()
    resultant_dict = pymp.shared.dict()

    with pymp.Parallel(total_threads) as p:
        the_lock = p.lock
        # Initialize the dictionary with the given words
        for curr_word in words:
            resultant_dict[curr_word] = 0;
        for curr_file in p.iterate(loaded_files):
            for curr_word in words:
                # Regular expression
                rex = '(?<![\w\d])' + curr_word + '(?![\w\d])'
                # List of occurrences
                start = time.time()
                occurrences = re.findall(rex, curr_file, re.IGNORECASE)
                end = time.time()

                the_lock.acquire()
                resultant_dict[curr_word] += len(occurrences);
                the_lock.release()
    print("Counting words runtime:", end - start, "s")
    return resultant_dict


def print_dict(resultant_dict):
    print("\nNumber of occurrences")
    for key in resultant_dict:
        print(key, "-->", resultant_dict[key])

def getFilenames():
    file_list = []
    # Load and return files
    for i in range(1, 9):
        filename = "shakespeare" + str(i) + ".txt"
        file_list.append(open(filename))
    return file_list

def getWords():
    words = ["love", "hate", "death", "night", "sleep", "time", "henry", "hamlet", "you", "my", "blood", "poison", "macbeth", "king", "heart", "honest"]
    return words;

def main():
    parser = argparse.ArgumentParser(description=
                                     'Count the occurrences of a given list of words in Shakespeare works')
    parser.add_argument('-t', '--threads', default=1, type=int,
                        help='The number of threads to be used')

    args = parser.parse_args()

    #If not argument was passed in the console, then test 1, 2, 4, and 8 threads
    if(args.threads == 1):
        threads = [1, 2, 4, 8]
        results = {}
        for t in threads:
            print("----------------------------")
            print("Testing with", t, "thread(s)")
            print("----------------------------")
            start = time.time()
            results = MapReduce(t)
            end = time.time()
            print("MapReduce runtime with", t, "thread(s):", end - start, "s")
        print_dict(results)
    else:
        print("----------------------------")
        print("Testing with", args.threads, "thread(s)")
        print("----------------------------")
        results = MapReduce(args.threads)
        print_dict(results)

main()
