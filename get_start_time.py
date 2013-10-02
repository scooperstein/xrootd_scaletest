import sys

overall_start_time = 1380127105000

test_files = open(sys.argv[1])
for fname in test_files:
    fname = fname.rstrip('\n')
    file = open(fname)
    for line in file:
        if ("RESULT" in line):
            results = line.split()
            if (len(results) != 5): break;
            start_time = int(results[3])
   
            if (start_time < overall_start_time):
                overall_start_time = start_time


print overall_start_time
