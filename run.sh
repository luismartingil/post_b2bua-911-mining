#!/bin/bash
#
# BASH script to run automated jobs in Hadoop
#
# post_b2bua-911-mining
#
# luismartingil - 2013
# www.luismartingil.com
#

STREAM=/usr/lib/hadoop-0.20-mapreduce/contrib/streaming/hadoop-streaming-2.0.0-mr1-cdh4.4.0.jar

# hdfs place to store my results
INPUT_FOLDER=b2bua/input
OUTPUT_FOLDER=b2bua/results
TASKS=1

DAT=`date +"%F__%H_%M_%S__%s"`
echo $DAT

for lfile in INb2bua_test INb2bua_241 INb2bua_242
do
    for opt in eday dayow hourod minoh eweek dayow_hourod hourod_dayow
    do
        # hdfs place where my input files are located
	INPUT=$INPUT_FOLDER/$lfile.log
	OUTPUT=$OUTPUT_FOLDER/$DAT/$lfile/$opt/
	echo 'Working with log:'$lfile' and opt:'$opt
	echo 'input:'$INPUT
	echo 'output:'$OUTPUT
	# Lets generate a folder with the results
	hadoop fs -mkdir -p $OUTPUT_FOLDER/$DAT/$lfile
	hadoop jar $STREAM \
	    -Dmapred.reduce.tasks=$TASKS \
	    -input $INPUT \
	    -output $OUTPUT \
	    -cmdenv PARAM_OPT=$opt \
	    -file mapper.py \
	    -file reducer.py \
	    -mapper mapper.py \
	    -reducer reducer.py
	# Retrieving the results
	mkdir -p /home/cloudera/post_b2bua-911-mining/$OUTPUT_FOLDER/$DAT/$lfile/$opt/
	hadoop fs -copyToLocal $OUTPUT /home/cloudera/post_b2bua-911-mining/$OUTPUT_FOLDER/$DAT/$lfile/$opt/
	echo 'Working with log:'$lfile' and opt:'$opt' done!'
    done
done