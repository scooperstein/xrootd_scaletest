#export test_directory="/afs/hep.wisc.edu/user/dan/AAA_scaletest/rapid-redirect-2013-09-25/wisconsin"
#export test_directory="/afs/hep.wisc.edu/user/dan/AAA_scaletest/rapid-redirect-2013-09-25/wisconsin_internal"
#export test_directory="/afs/hep.wisc.edu/user/dan/AAA_scaletest/rapid-redirect-2013-09-25/nebraska/"

#export test_directory="/afs/hep.wisc.edu/user/dan/AAA_scaletest/rapid-redirect-2013-11-08/nebraska_global/"
#export test_directory="/afs/hep.wisc.edu/user/dan/AAA_scaletest/rapid-redirect-2013-11-08/nebraska_internal/"

#ls $test_directory/stdout* > test_files.txt

python make_stat_plots.py test_files_wisconsin.txt 8000 500 1380125156
python make_stat_plots.py test_files_wisconsin_internal.txt 4000 300 1380139669
python make_stat_plots.py test_files_nebraska.txt 3600 300 1380129980

python make_stat_plots.py test_files_nebraska_global.txt 4000 400 1383947801 
python make_stat_plots.py test_files_nebraska_internal.txt 3600 300 1383942846 
