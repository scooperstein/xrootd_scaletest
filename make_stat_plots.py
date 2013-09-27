import sys
import ROOT
import os

if (len(sys.argv) != 5):
    print "Usage: python make_stat_plots.py test_files test_duration size_of_time_bins test_start_time"
    sys.exit(1)

print "Opening list of test files..." + sys.argv[1]
test_files = open(sys.argv[1])
test_length = float(sys.argv[2])
bin_size = float(sys.argv[3])
nbins = int(test_length/bin_size)
overall_start_time = float(sys.argv[4])

print "Assuming test of length %f seconds, bin size %f seconds, yielding %f bins" % (test_length, bin_size, nbins)
print "Further assuming that the test began at time %f seconds" % overall_start_time
hist_active_jobs = ROOT.TH1F("hist_active_jobs", "active jobs as a function of time", nbins, overall_start_time, overall_start_time + test_length)
#hist_active_jobs.SetMaximum(1)

for filename in test_files:
    filename = filename.rstrip('\n')
    print "opening file %s ..." % filename
    file = open(filename)
    for line in file:
        if ("RESULT" in line):
           results = line.split()
           if (len(results) != 5): break;

           xrootd_filename = results[1]
           job_success = bool(results[2])
           start_time = int(results[3])
           run_time = float(results[4])
           hist_active_jobs.Fill(start_time) 

c1 = ROOT.TCanvas("c1", "c1")
hist_active_jobs.Draw()
os.system("sleep 3")
c1.SaveAs("canvas.root")
c1.Close()
