# AbStar  
  
VDJ assignment and antibody sequence annotation. Scalable from a single sequence to billions of sequences.  
  
  - Source code: [github.com/briney/abstar](https://github.com/briney/abstar)  
  - Documentation: [abstar.readthedocs.org](http://abstar.readthedocs.org)  
  - Download: [pypi.python.org/pypi/abstar](https://pypi.python.org/pypi/abstar)  
  - Docker: [hub.docker.com/r/briney/abstar/](https://hub.docker.com/r/briney/abstar/)  
  
### install  
`pip install abstar`  
  
### use  

To run AbStar on a single FASTA or FASTQ file:  
`abstar -i <input-file> -o <output-directory> -t <temp-directory>`

To iteratively run AbStar on all files in an input directory:  
`abstar -i <input-directory> -o <output-directory> -t <temp-directory>`
  
To run AbStar using the included test data as input:  
`abstar -o <output-directory> -t <temp-directory> --use-test-data`  
  
When using the AbStar test data, note that although the test data file contains 1,000 sequences, one of the test sequences is not a valid antibody recombination. Only 999 sequences should be processed successfully.  
  
### additional options  
`-l, --log` Change the log file location. Default is `<output_directory>/mongo.log`.  
  
`-m, --merge` Input directory should contain paired FASTQ (or gzipped FASTQ) files. Paired files will be merged with PANDAseq prior to processing with AbAnalysis.  
  
`-b, --basespace` Download a sequencing run from BaseSpace, which is Illumina's cloud storage environment. Since Illumina sequencers produce paired-end reads, --merge is also set.  
  
`-u N, --uaid N` Sequences contain a unique antibody ID (UAID, or molecular barcode) of length N. The uaid will be parsed from the beginning of each input sequence and added to the JSON output. Negative values result in the UAID being parsed from the end of the sequence.  
  
`-s, --species` Select the species from which the input sequences are derived. Supported options are 'human', 'mouse', and 'macaque'. Default is 'human'.  
   
`-c, --cluster` Runs AbStar in distributed mode on a Celery cluster.  
  
`-h, --help` Prints detailed information about all runtime options.
  
`-D --debug` Much more verbose logging.  
  
  
### helper scripts  
Two helper scripts are included:  
`batch_mongoimport` automates the import of multiple JSON output files into a MongoDB database.  
`make_basespace_credfile` makes a credentials file for BaseSpace, which is required if downloading sequences from BaseSpace with Abstar. Developer credentials are required, and the process for obtaining them is explained [here](https://support.basespace.illumina.com/knowledgebase/articles/403618-python-run-downloader)  
  
  
### requirements  
Python 2.7 (3.x probably doesn't work, but hasn't been tested)  
abtools  
biopython  
celery  
pymongo  
scikit-bio  

All of the above dependencies can be installed with pip, and will be installed automatically when installing AbStar with pip.  
If you're new to Python, a great way to get started is to install the [Anaconda Python distribution](https://www.continuum.io/downloads), which includes pip as well as a ton of useful scientific Python packages.
  
sequence merging requires [PANDAseq](https://github.com/neufeld/pandaseq)  
batch_mongoimport requires [MongoDB](http://www.mongodb.org/)  
BaseSpace downloading requires the [BaseSpace Python SDK](https://github.com/basespace/basespace-python-sdk)  
