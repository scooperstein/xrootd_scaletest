export test_directory="/afs/hep.wisc.edu/user/dan/AAA_scaletest/rapid-redirect-2013-09-25/wisconsin"

ls $test_directory/stdout* > test_files.txt

python make_stat_plots.py test_files.txt 20000 1000 1380125156
