#Extracting Error count from a files in folder
import subprocess
path="/home/prajakta/RegressionResults/Unicity_20190708/"
output=subprocess.Popen(["ls",path],
	stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
d_names,d_name_error=output.communicate()
d_n=d_names.split("\n")
d_n.pop()
for d in d_n:
	print("Directory Name : \t"+d)
	find_error_file=subprocess.Popen(["ls",path+d],
		stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
	f_names,f_name_error=find_error_file.communicate()
	f_n=f_names.split("\n")
	f_n.pop()
	for f in f_n:
		if f.startswith("Errors"):
			print("Error file name : \t"+f)
			fileText = open ( path+d+"/"+f,"r" )
			lineList = fileText.readlines()
			fileText.close()
			count=int(list(filter(None, lineList[len(lineList)-2].split(" ")))[0])
			print("Error count : \t\t%d"%count+"\n")

'''
*
*
*
*
*
*
*
*
*
*
*
*
prajakta@prajakta-HP-ProBook-440-G5:~$ python error_folder2.py
Directory Name : 	p02_nbc_mcp2_project
Error file name : 	ErrorsList_p02_nbc_mcp2_project_20190708.txt.txt
Error count : 		96

Directory Name : 	srs_bpm
Error file name : 	ErrorsList_srs_bpm_20190708.txt.txt
Error count : 		1

Directory Name : 	srs_collapse_parties
Error file name : 	ErrorsList_srs_collapse_parties_20190708.txt.txt
Error count : 		2

Directory Name : 	SRS_Delta_Processing_Organization
Error file name : 	ErrorsList_SRS_Delta_Processing_Organization_20190708.txt.txt
Error count : 		2

Directory Name : 	srs_delta_processing_person
Error file name : 	ErrorsList_srs_delta_processing_person_20190708.txt.txt
Error count : 		45

prajakta@prajakta-HP-ProBook-440-G5:~$
*
*
*
*
*
*
*
*
*
*
*
*
'''
