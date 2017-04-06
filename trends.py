from textblob import TextBlob
import csv
import argparse
import sys

def blober(infile):
    # create dictionary for sentence/sentiment rankings
    sentence_ranks = {}
    # get tweets
    blob = TextBlob(open(infile, 'rb').read())
    for i in blob.sentences:
        sentence_ranks[i] = i.sentiment.polarity
    return sentence_ranks

def csv_writer(trend_name, ranks_d):
    trend_name = trend_name + ".csv"
    with open(trend_name, 'wb') as csv_file:
        writer = csv.writer(csv_file)
        for key, value in ranks_d.items():
            writer.writerow([key, value])

if __name__ == "__main__":
    tr_name = "test"
    in_f = sys.argv[1] # use whole argument after script for filename
    csv_writer(tr_name, blober(in_f))