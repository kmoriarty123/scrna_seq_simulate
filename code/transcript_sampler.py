
#Kathleen Moriarty
#Homework 3

class TransriptSampler:

    def __init__(self):

    # read_avg_expression(file)
    # reads a file in the format "gene_id nr_copies"
    # constructs a dictionary with the average number of transcripts for every gene (i.e. nr_copies)
    # return this dictionary

    def read_avg_expression(gene_file):

        import pandas as pd
        #Read in file as dataframe
        gene_df = pd.read_csv(gene_file, header=0)

        #Take the average of the transcripts, grouping by gene
        gene_mean_df = gene_df.groupby('gene_id').mean()
        #print(gene_mean_df.iloc[0:11,])
        #Convert to dictionary
        gene_mean_dict = gene_mean_df.to_dict()

        return(list(gene_mean_dict.values())[0])

    # sample_transcripts(avgs, number)
    # takes as input the dictionary constructed above and a total number of transcripts to sample
    # it generates a sample of transcripts by sampling from individual genes in accordance to the relative abundance computed from the input dictionary
    # returns the dictionary built from this sample

    def sample_transcripts(gene_dict, samp_nr):
        import random

        #To store the values from the sampling
        #Create probabilites for each gene in the gene_dict
        print((gene_dict).values())
        total_trans = sum(gene_dict.values())
        print(total_trans)
        prob_dist = {k: v / total_trans for k, v in gene_dict.items()}
        #prob_dist = (gene_dict.values())/total_trans
        print(prob_dist)

        sample_dict = random.choices(population=list(gene_dict.items()), k=samp_nr, weights=list(prob_dist.values()))
        return(dict(sample_dict))

    # write_sample(file, sample)
    # takes as input a file name and a sample dictionary (constructed as described at point 2)...
    # writes to the file the sample dictionary

    def write_sample(myfile, tmp_samp_dict):
        with open(myfile,'w') as myfile:
            myfile.write(str(tmp_samp_dict))