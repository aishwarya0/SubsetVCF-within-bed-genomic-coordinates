import argparse
parser = argparse.ArgumentParser(description='Subset VCF based on bed file')
parser.add_argument('--invcf', required=True,type=str)
parser.add_argument('--inbed',required=True,type=str)
parser.add_argument('--out',required=True,type=str)
args = parser.parse_args()
class SubsetVCF(object):




        def read_and_write(self):
            """
                            python3 SubsetVCF.py --help
                            :param invcf: Give VCF file path
                            :param inbed: Give BED file path(column 1 : chr<No.>,column2 : start position,column3 : end position)
                            :param out: Outfile name
                            :return: Subset of VCF file based on genomic coordinates present in provided BED file
            """
            invcf = open(args.invcf) ##open VCF file to read
            corr = open(args.inbed) ##open bed file to read
            inbed = [row for row in corr] ##create a list of bed entries
            header = []
            filtered_entries = []
            outvcf = open(args.out, 'w') ##open a file to write
            for vline in invcf:
                if vline.startswith('#'):
                    header.append(vline.strip("\n"))
                    continue
                vline = vline.strip().split("\t")

            #def readBed(self):
                for brow in inbed:
                    brow = brow.strip().split("\t")

            #def readBed(self):
                    if ((vline[0] == brow[0]) & (int(vline[1]) >= int(brow[1])) & (int(vline[1]) <= int(brow[2]))):
                            filtered_entries.append(vline)
            print("Writing to output file!!")
            outvcf.write("\n".join(header))
            outvcf.write("\n")
            for entries in filtered_entries:
                outvcf.write("\t".join(entries))
                outvcf.write("\n")
obj= SubsetVCF()
obj.read_and_write()