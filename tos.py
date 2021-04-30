import argparse

# Create the parser

my_parser = argparse.ArgumentParser(prog='myls',
                                    usage='%(prog)s [options] path',
                                    description='List the content of a folder')