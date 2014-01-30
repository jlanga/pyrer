# Import Biopython's file reader
from Bio import SeqIO
# Import a copy file function
from shutil import copyfile

# Get the header indexes of each read from each file
print "Loading headers from TIM_1.trimmed.fastq"
index_1 = SeqIO.index("TIM_1.trimmed.fastq","fastq").keys()
print "Loading headers from TIM_2.trimmed.fastq"
index_2 = SeqIO.index("TIM_2.trimmed.fastq","fastq").keys()
print "Loading headers from TIM_3.trimmed.fastq"
index_3 = SeqIO.index("TIM_3.trimmed.fastq","fastq").keys()
print "Loading headers from TIM_4.trimmed.fastq"
index_4 = SeqIO.index("TIM_4.trimmed.fastq","fastq").keys()

# Compute reads such that are still paired (both in index_1 and index_2)
index_paired = set( index_1 ) & set( index_2 )

# Comptute the reads that we will have to add to files 3 and 4
add_to_3     = set( index_1 ) - set( index_paired )
add_to_4     = set( index_2 ) - set( index_paired )

# Copy files 3 and 4
copyfile( "TIM_3.trimmed.fastq" , "TIM_3.trimmed2.fastq" )
copyfile( "TIM_4.trimmed.fastq" , "TIM_4.trimmed2.fastq" )

# Write new file _1
input_seq_iterator = SeqIO.parse(open("TIM_1.trimmed.fastq", "rU"), "fastq")
short_seq_iterator = (record for record in input_seq_iterator if record.id in index_paired)
output_handle = open("TIM_1.trimmed2.fastq", "w")
SeqIO.write(short_seq_iterator, output_handle, "fastq")
output_handle.close()

# Write new file _2
input_seq_iterator = SeqIO.parse(open("TIM_2.trimmed.fastq", "rU"), "fastq")
short_seq_iterator = (record for record in input_seq_iterator if record.id in index_paired)
output_handle = open("TIM_2.trimmed2.fastq", "w")
SeqIO.write(short_seq_iterator, output_handle, "fastq")
output_handle.close()

# Add to new file _3
input_seq_iterator = SeqIO.parse(open("TIM_1.trimmed.fastq", "rU"), "fastq")
short_seq_iterator = (record for record in input_seq_iterator if record.id in add_to_3)
output_handle = open("TIM_3.trimmed2.fastq" , "a")
SeqIO.write(short_seq_iterator, output_handle, "fastq")
output_handle.close()

# Add to new file _4
input_seq_iterator = SeqIO.parse(open("TIM_2.trimmed.fastq", "rU"), "fastq")
short_seq_iterator = (record for record in input_seq_iterator if record.id in add_to_4)
output_handle = open("TIM_4.trimmed2.fastq" , "a")
SeqIO.write(short_seq_iterator, output_handle, "fastq")
output_handle.close()