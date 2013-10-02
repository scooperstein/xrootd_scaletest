import sys
import ROOT
import os

if (len(sys.argv) != 5):
    print "Usage: python make_stat_plots.py test_files test_duration size_of_time_bins test_start_time"
    sys.exit(1)

print "Opening list of test files..." + sys.argv[1]
#test_files = open(sys.argv[1])
test_length = float(sys.argv[2])
bin_size = float(sys.argv[3])
nbins = int(test_length/bin_size)
overall_start_time = float(sys.argv[4])

# setup interval mapping structure
intervals = {}
for i in range(nbins):
    intervals[str(i)] = [ overall_start_time+i*bin_size, overall_start_time+(i+1)*bin_size ]
#print "printing dictionary 'intervals'..."
#print intervals

print "Assuming test of length %f seconds, bin size %f seconds, yielding %f bins" % (test_length, bin_size, nbins)
print "Further assuming that the test began at time %f seconds" % overall_start_time
hist_active_jobs = ROOT.TH1F("hist_active_jobs", "concurrent active jobs as a function of time", nbins, overall_start_time, overall_start_time + test_length)
hist_job_failures = ROOT.TH1F("hist_job_failures", "concurrent job failures as a function of time", nbins, overall_start_time, overall_start_time + test_length)
hist_job_successes = ROOT.TH1F("hist_job_successes", "concurrent job successes as a fucntion of time", nbins, overall_start_time, overall_start_time + test_length)
#hist_active_jobs.SetMaximum(1)

# this extra for loop destroys computation time and seems stupid,
# but I have yet to come up with a better way to only fill the histogram
# once per job per time interval
for i in range(nbins):
    test_files = open(sys.argv[1])
    for filename in test_files:
        filename = filename.rstrip('\n')
        #print "opening file %s ..." % filename
        file = open(filename)
        ## I want this h to be temporary and have maximum bin value of one so that we count 
        ## the number of jobs actually running during the time period rather than simply the 
        ## number of jobs that started (a job can have multiple file i/o's in a time interval).
        ##h = ROOT.TH1F("h", "h",  nbins, overall_start_time, overall_start_time + test_length) 
        for line in file:
            if ("RESULT" in line):
                results = line.split()
                if (len(results) != 5): break;
                
                xrootd_filename = results[1]
                if (results[2] == "success"):
                    job_success = True
                else: 
                    job_success = False
                start_time = int(results[3])
                run_time = float(results[4])
                #print i
                if (start_time > intervals[str(i)][0] and start_time < intervals[str(i)][1] ):
                    # a bit of a hack, but this should allow me to fill each time interval at most once per job
                    hist_active_jobs.Fill(start_time)
           
                    if (job_success):
                        hist_job_successes.Fill(start_time)
                    else: 
                        hist_job_failures.Fill(start_time)
                    break;
        file.close()
    test_files.close()

# make plot of success/failure rate vs # clients running concurrently
n_clients = ROOT.TVectorF()
sf_rate = ROOT.TVectorF()

graph = ROOT.TGraph()
for i in range(nbins):
    n_clients = hist_active_jobs.GetBinContent(i+1)
    s = hist_job_successes.GetBinContent(i+1)
    f = hist_job_failures.GetBinContent(i+1)
    if (f > 0):
        rate = s/f
    elif (s == 0.0):
        rate = 0.0
    else: rate = 1.0 #all success, no failures
    graph.SetPoint(graph.GetN(), n_clients, rate)

c1 = ROOT.TCanvas("c1", "c1")
#graph.Draw()
output_file = ROOT.TFile("plots.root", "RECREATE")
hist_active_jobs.Draw()
os.system("sleep 3")
#hist_job_successes.Draw()
#os.system("sleep 3")
#hist_job_failures.Draw()
#os.system("sleep 3")
#c1.SaveAs("canvas.root")
hist_active_jobs.Write()
hist_job_successes.Write()
hist_job_failures.Write()
graph.Write()
#output_file.Write()
c1.Close()
output_file.Close()
