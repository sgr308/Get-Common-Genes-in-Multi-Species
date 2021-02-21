# Import modules.
import os, re, sys

# Define output file.
out_file = open("result_common_genes_in_multi_species.txt", "w+")

# Import first blastp file of Species_1.
blast_file_1 = open("blastresults_1","r")

#Create a dictionary with first column data as key and second column data as value.
blast_dict1 = {}
for line in blast_file_1:
        blast_dict1_key=line.split()[0]
        blast_dict1_value=line.split()[1]
	blast_dict1[blast_dict1_key]=blast_dict1_value
#print blast_dict1

# Import second blastp file of Species_2.
blast_file_2 = open("blastresults_2","r")

#Create a dictionary with first column data as key and second column data as value.
blast_dict2 = {}
for line1 in blast_file_2:
        blast_dict2_key=line1.split()[0]
        blast_dict2_value=line1.split()[1]
        blast_dict2[blast_dict2_key]=blast_dict2_value
#print blast_dict2

# Import third blastp file of Species_3.
blast_file_3 = open("blastresults_2","r")

#Create a dictionary with first column data as key and second column data as value.
blast_dict3 = {}
for line2 in blast_file_3:
        blast_dict3_key=line2.split()[0]
        blast_dict3_value=line2.split()[1]
        blast_dict3[blast_dict3_key]=blast_dict3_value
#print blast_dict3

# Import fourth blastp file of Species_4.
blast_file_4 = open("blastresults_4","r")

#Create a dictionary with first column data as key and second column data as value.
blast_dict4 = {}
for line1 in blast_file_4:
        blast_dict4_key=line1.split()[0]
        blast_dict4_value=line1.split()[1]
        blast_dict4[blast_dict4_key]=blast_dict4_value
#print blast_dict4

# Import fifth blastp file of Species_5.
blast_file_5 = open("blastresults_5","r")

#Create a dictionary with first column data as key and second column data as value.
blast_dict5 = {}
for line2 in blast_file_5:
        blast_dict5_key=line2.split()[0]
        blast_dict5_value=line2.split()[1]
        blast_dict5[blast_dict5_key]=blast_dict5_value
#print blast_dict5

# Import sixth bivalve gene id file.
blast_file_biv = open("Gene_id.txt","r")

#Create a dictionary with first column data as key and second column data as value.
blast_dictbiv = {}
for linebiv in blast_file_biv:
        blast_dictbiv_key=linebiv.split()[0]
        blast_dictbiv_value=linebiv.split()[0]
        blast_dictbiv[blast_dictbiv_key]=blast_dictbiv_value
#print blast_dictbiv

for key in blast_dictbiv.keys():
	if key in blast_dict1:
		oys = blast_dict1[key]
	else:
		oys = "--------"
	if key in blast_dict2:
		oct = blast_dict2[key]
	else:
		oct = "-----------------"
	if key in blast_dict3:
		hm = blast_dict3[key]
	else:
		hm = "-----------------"
	if key in blast_dict4:
		ms = blast_dict4[key]
	else:
		ms = "--------------------"
	if key in blast_dict5:
		fly = blast_dict5[key]
	else:
		fly = "-----------"

	print >> out_file, key, Species_1, Species_2, Species_3, Species_4, Species_5
