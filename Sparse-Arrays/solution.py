#!/bin/python3
import os
from collections import Counter

def matchingStrings(stringList, queries):
    # Count frequencies of all strings in O(N) time
    string_counts = Counter(stringList)
    
    # Look up each query in O(1) time
    return [string_counts[query] for query in queries]

if __name__ == '__main__':
    # Read the environment variable for output, fallback to standard output if not present
    output_path = os.environ.get('OUTPUT_PATH', '/dev/stdout')
    fptr = open(output_path, 'w')

    # Read input string list
    stringList_count = int(input().strip())
    stringList = []
    for _ in range(stringList_count):
        stringList_item = input()
        stringList.append(stringList_item)

    # Read queries list
    queries_count = int(input().strip())
    queries = []
    for _ in range(queries_count):
        queries_item = input()
        queries.append(queries_item)

    # Get results and write to the output destination
    res = matchingStrings(stringList, queries)
    fptr.write('\n'.join(map(str, res)))
    fptr.write('\n')
    fptr.close()
