import csv
import json
import unicodecsv
import optparse


def convert_basic():
  parser = optparse.OptionParser()
  parser.add_option('--csv',dest='outfile',default='election-output.csv')
  parser.add_option('--json',dest='infile',default=None)
  (options, args) = parser.parse_args()
  print options
  jsonf= open(options.infile, 'rU')
  jsond = json.load(jsonf)
  with open(options.outfile, "wb") as out_file:
    out_file.write(u'\ufeff'.encode('utf8'))
    writer = unicodecsv.DictWriter(out_file,encoding="utf-8",  delimiter=',', fieldnames=jsond[0].keys() )
    writer.writeheader()
    for row in jsond:
      writer.writerow(row)


if __name__=="__main__":
  convert_basic()


