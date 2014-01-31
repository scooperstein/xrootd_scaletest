#export test_directory="/afs/hep.wisc.edu/user/dan/AAA_scaletest/rapid-redirect-2013-09-25/wisconsin"
#export test_directory="/afs/hep.wisc.edu/user/dan/AAA_scaletest/rapid-redirect-2013-09-25/wisconsin_internal"
#export test_directory="/afs/hep.wisc.edu/user/dan/AAA_scaletest/rapid-redirect-2013-09-25/nebraska/"

#export test_directory="/afs/hep.wisc.edu/user/dan/AAA_scaletest/rapid-redirect-2013-11-08/nebraska_global/"
#export test_directory="/afs/hep.wisc.edu/user/dan/AAA_scaletest/rapid-redirect-2013-11-08/nebraska_internal/"

#ls $test_directory/stdout* > test_files.txt

#python make_stat_plots.py test_files_wisconsin.txt 8000 500 1380125156
#python make_stat_plots.py test_files_wisconsin_internal.txt 4000 300 1380139669
#python make_stat_plots.py test_files_nebraska.txt 3600 300 1380129980

#python make_stat_plots.py test_files_nebraska_global.txt 4000 400 1383947801 
#python make_stat_plots.py test_files_nebraska_internal.txt 3600 300 1383942846 

#python make_stat_plots.py test_files_nov29.txt 7200 400 1385791943
#python make_stat_plots.py test_files_nov30.txt 7200 400 1385860556 

# python make_stat_plots.py test_files_dec4.txt 14400 1000 1386196063
# python make_stat_plots.py testfilesjan21.txt 4304  200 1390333448
# python make_stat_plots.py t2wisctestjan24.txt 3600  180 1390857140
# python make_stat_plots.py t2ucsdtestjan27.txt 4630  200 1390878870
# python make_stat_plots.py t2wisctestjan28.txt 6884  200 1390941080
# python make_stat_plots.py t2wisctestjan28eve.txt 6801  200 1390964870
# python make_stat_plots.py t2wisctestjan29.txt 6670  300 1391031522
# python make_stat_plots.py t2nebrtestjan29.txt 3650  180 1391050325 T2_US_Nebraska
# python make_stat_plots.py t2purduetestjan30.txt 4811  160 1391104319
# python make_stat_plots.py t2mit_testjan30.txt 3653  180 1391109265 T2_US_MIT
# python make_stat_plots.py t2purduefulltestjan30.txt 3659  180 1391113458 T2_US_Purdue
# python make_stat_plots.py t2caltechtestjan30.txt 3658  180 1391120280 T2_US_Caltech
# python make_stat_plots.py t2ucsdtestjan29.txt 4481  220 1391012412 T2_US_UCSD
# python make_stat_plots.py t2wisctestjan30.txt 3684  180 1391124716 T2_US_Wisconsin
python make_stat_plots.py t2wisctestjan31.txt 3189  180  1391196190 T2_US_Wisconsin
