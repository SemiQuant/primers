from selenium import webdriver
import webbrowser
from selenium.webdriver.common.by import By
import codecs
import os
from bs4 import BeautifulSoup
import urllib.request
import pandas as pd
from time import sleep
import argparse


# inputs
parser = argparse.ArgumentParser()
parser.add_argument("--out_dir", default="")
parser.add_argument("--name", default="noname")
parser.add_argument("--seq", type = str, default="")
parser.add_argument("--PRIMER_NUM_RETURN", default="5")
parser.add_argument("--PRIMER_MIN_TM", default="57.0")
parser.add_argument("--PRIMER_OPT_TM", default="63")
parser.add_argument("--PRIMER_MAX_TM", default="68")
parser.add_argument("--ORGANISM", default='Homo%20sapiens')
parser.add_argument("--PRIMER_SPECIFICITY_DATABASE", default="refseq_mrna")
parser.add_argument("--PRIMER_MIN_SIZE", default="15")
parser.add_argument("--PRIMER_OPT_SIZE", default="20")
parser.add_argument("--PRIMER_MAX_SIZE", default="25")
parser.add_argument("--PRIMER_MIN_GC", default="20.0")
parser.add_argument("--PRIMER_MAX_GC", default="80.0")
parser.add_argument("--GC_CLAMP", default="0")
parser.add_argument("--POLYX", default="3")
parser.add_argument("--PRIMER_LEFT_INPUT", type = str)
parser.add_argument("--PRIMER_RIGHT_INPUT", type = str)
parser.add_argument("--PRIMER5_START")
parser.add_argument("--PRIMER5_END")
parser.add_argument("--PRIMER3_START")
parser.add_argument("--PRIMER3_END")
parser.add_argument("--PRIMER_PRODUCT_MIN")
parser.add_argument("--PRIMER_PRODUCT_MAX")
args = parser.parse_args()
out_dir = args.out_dir
name = args.name


options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors')
options.add_argument("--test-type")
# options.binary_location = "/Users/SemiQuant/bioinfomatics/"
driver = webdriver.Chrome(options=options)

# driver.get("example.com")
url_1 = "https://www.ncbi.nlm.nih.gov/tools/primer-blast/index.cgi?LINK_LOC=bookmark&INPUT_SEQUENCE=%s&OVERLAP_5END=7&OVERLAP_3END=4&PRIMER_MAX_DIFF_TM=3&PRIMER_ON_SPLICE_SITE=0&SEARCHMODE=0&SPLICE_SITE_OVERLAP_5END=7&SPLICE_SITE_OVERLAP_3END=4&SPLICE_SITE_OVERLAP_3END_MAX=8&SPAN_INTRON=off&MIN_INTRON_SIZE=1000&MAX_INTRON_SIZE=1000000&SEARCH_SPECIFIC_PRIMER=on&EXCLUDE_ENV=off&EXCLUDE_XM=off&TH_OLOGO_ALIGNMENT=on&TH_TEMPLATE_ALIGNMENT=off&TOTAL_PRIMER_SPECIFICITY_MISMATCH=1&PRIMER_3END_SPECIFICITY_MISMATCH=1&MISMATCH_REGION_LENGTH=5&TOTAL_MISMATCH_IGNORE=6&MAX_TARGET_SIZE=4000&ALLOW_TRANSCRIPT_VARIANTS=off&HITSIZE=50000&EVALUE=30000&WORD_SIZE=7&MAX_CANDIDATE_PRIMER=500&NUM_TARGETS_WITH_PRIMERS=1000&NUM_TARGETS=20&MAX_TARGET_PER_TEMPLATE=100&SELF_ANY=8.00&SELF_END=3.00&PRIMER_MAX_END_STABILITY=9&PRIMER_MAX_END_GC=5&PRIMER_MAX_TEMPLATE_MISPRIMING_TH=40.00&PRIMER_PAIR_MAX_TEMPLATE_MISPRIMING_TH=70.00&PRIMER_MAX_SELF_ANY_TH=45.0&PRIMER_MAX_SELF_END_TH=35.0&PRIMER_PAIR_MAX_COMPL_ANY_TH=45.0&PRIMER_PAIR_MAX_COMPL_END_TH=35.0&PRIMER_MAX_HAIRPIN_TH=24.0&PRIMER_MAX_TEMPLATE_MISPRIMING=12.00&PRIMER_PAIR_MAX_TEMPLATE_MISPRIMING=24.00&PRIMER_PAIR_MAX_COMPL_ANY=8.00&PRIMER_PAIR_MAX_COMPL_END=3.00&PRIMER_MISPRIMING_LIBRARY=AUTO&NO_SNP=off&LOW_COMPLEXITY_FILTER=on&MONO_CATIONS=50.0&DIVA_CATIONS=1.5&CON_ANEAL_OLIGO=5&CON_DNTPS=0.6&SALT_FORMULAR=1&TM_METHOD=1&PRIMER_INTERNAL_OLIGO_MIN_SIZE=18&PRIMER_INTERNAL_OLIGO_OPT_SIZE=20&PRIMER_INTERNAL_OLIGO_MAX_SIZE=27&PRIMER_INTERNAL_OLIGO_MIN_TM=57.0&PRIMER_INTERNAL_OLIGO_OPT_TM=60.0&PRIMER_INTERNAL_OLIGO_MAX_TM=63.0&PRIMER_INTERNAL_OLIGO_MAX_GC=80.0&PRIMER_INTERNAL_OLIGO_OPT_GC_PERCENT=50&PRIMER_INTERNAL_OLIGO_MIN_GC=20.0&PICK_HYB_PROBE=off&PRIMER_NUM_RETURN=%s&PRIMER_MIN_TM=%s&PRIMER_OPT_TM=%s&PRIMER_MAX_TM=%s&ORGANISM=%s&PRIMER_SPECIFICITY_DATABASE=%s&PRIMER_MIN_SIZE=%s&PRIMER_OPT_SIZE=%s&PRIMER_MAX_SIZE=%s&PRIMER_MIN_GC=%s&PRIMER_MAX_GC=%s&GC_CLAMP=%s&POLYX=%s" % (args.seq, args.PRIMER_NUM_RETURN, args.PRIMER_MIN_TM, args.PRIMER_OPT_TM, args.PRIMER_MAX_TM, args.ORGANISM, args.PRIMER_SPECIFICITY_DATABASE, args.PRIMER_MIN_SIZE, args.PRIMER_OPT_SIZE, args.PRIMER_MAX_SIZE, args.PRIMER_MIN_GC, args.PRIMER_MAX_GC, args.GC_CLAMP, args.POLYX)

if args.PRIMER_LEFT_INPUT is not None:
    url_1 += '&PRIMER_LEFT_INPUT=' + args.PRIMER_LEFT_INPUT

if args.PRIMER_RIGHT_INPUT is not None:
    url_1 += '&PRIMER_RIGHT_INPUT=' + args.PRIMER_RIGHT_INPUT

if args.PRIMER5_START is not None:
    url_1 += '&PRIMER5_START=' + str(args.PRIMER5_START)

if args.PRIMER5_END is not None:
    url_1 += '&PRIMER5_END=' + str(args.PRIMER5_END)

if args.PRIMER3_START is not None:
    url_1 += '&PRIMER3_START=' +str( args.PRIMER3_START)

if args.PRIMER3_END is not None:
    url_1 += '&PRIMER3_END=' + str(args.PRIMER3_END)

if args.PRIMER_PRODUCT_MIN is not None:
    url_1 += '&PRIMER_PRODUCT_MIN=' + str(args.PRIMER_PRODUCT_MIN)

if args.PRIMER_PRODUCT_MAX is not None:
    url_1 += '&PRIMER_PRODUCT_MAX=' + str(args.PRIMER_PRODUCT_MAX)

driver.get(url_1)
driver.find_element(By.CLASS_NAME, 'blastbutton.prbutton').click()


while True:
    try:
        driver.find_element(By.CLASS_NAME, 'usa-accordion-button.sectAccordion')
        break
    except:
        sleep(50)
        pass

driver.save_screenshot(out_dir + name + ".png")

# h = driver.page_source
# n = os.path.join("/Users/SemiQuant/Downloads/", "PageSave.html")
# f = codecs.open(n, "w", "utf−8")
# f.write(h)

url = driver.current_url
url = urllib.request.urlopen(url)
soup = BeautifulSoup(url, 'html.parser')
table = soup.select("table")[1:]

table = pd.read_html(str(table))
table = pd.concat(table)
table = table.loc[[0,1,3]]


pcount = sum(table.index == 0)
nms = list()
for i in range(pcount):
    nms.append("primer_" + str(i))


table.index = [nms * pcount*3][0][:pcount*3]

table.to_excel(out_dir + name + ".xlsx")

driver.close()
                








