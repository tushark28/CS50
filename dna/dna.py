import csv
import sys


def main():

    # TODO: Check for command-line usage
    if len(sys.argv) != 3:
        sys.exit("Usage: python dna.py data.csv sequence.txt")
    # TODO: Read database file into a variable
    file = open(sys.argv[1], "r")
    reader = csv.DictReader(file)
    database = []
    for dna in reader:
        try:
            dna["AGATC"] = int(dna["AGATC"])
        except:
            pass

        try:
            dna["AATG"] = int(dna["AATG"])
        except:
            pass

        try:
            dna["TATC"] = int(dna["TATC"])
        except:
            pass

        try:
            dna['TTTTTTCT'] = int(dna['TTTTTTCT'])
        except:
            pass

        try:
            dna["TCTAG"] = int(dna["TCTAG"])
        except:
            pass

        try:
            dna["GATA"] = int(dna["GATA"])
        except:
            pass

        try:
            dna["GAAA"] = int(dna["GAAA"])
        except:
            pass

        try:
            dna["TCTG"] = int(dna["TCTG"])
        except:
            pass

        database.append(dna)
    # TODO: Read DNA sequence file into a variable
    sequence = ""
    with open(sys.argv[2]) as seq_file:
        sequence = seq_file.read()
    # TODO: Find longest match of each STR in DNA sequence
    str = []
    with open(sys.argv[1]) as file:
        reader = csv.reader(file)
        str = next(reader)
        str.remove('name')
    longest_match_str = {}
    i = 0
    for match in str:
        longest_match_str[match] = int(longest_match(sequence, match))
    # TODO: Check database for matching profiles
    entire_flag = 1
    for person in database:
        flag = 0
        for eachstr in str:
            if person[eachstr] != longest_match_str[eachstr]:
                flag = 1
                break
        if flag == 0:
            print(person['name'])
            entire_flag = 0
    if entire_flag == 1:
        print("No match")
    return


def longest_match(sequence, subsequence):
    """Returns length of longest run of subsequence in sequence."""

    # Initialize variables
    longest_run = 0
    subsequence_length = len(subsequence)
    sequence_length = len(sequence)

    # Check each character in sequence for most consecutive runs of subsequence
    for i in range(sequence_length):

        # Initialize count of consecutive runs
        count = 0

        # Check for a subsequence match in a "substring" (a subset of characters) within sequence
        # If a match, move substring to next potential match in sequence
        # Continue moving substring and checking for matches until out of consecutive matches
        while True:

            # Adjust substring start and end
            start = i + count * subsequence_length
            end = start + subsequence_length

            # If there is a match in the substring
            if sequence[start:end] == subsequence:
                count += 1

            # If there is no match in the substring
            else:
                break

        # Update most consecutive matches found
        longest_run = max(longest_run, count)

    # After checking for runs at each character in seqeuence, return longest run found
    return longest_run


main()
