import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-p", "--par", dest="par", type=int,
                    help="max number of parallel threads (OPTIONAL)")


opts, args = parser.parse_known_args(["-p", "1", "ping a"])
print(opts.par)