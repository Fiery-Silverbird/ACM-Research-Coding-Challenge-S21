from dna_features_viewer import GraphicFeature, CircularGraphicRecord
import re


def main():
    genome_data = open("Genome.gb", "r")
    for text in genome_data:
        if re.search("SOURCE", text):
            print(text)
        elif re.search("source", text):
            print(text)
        elif re.search("gene", text):
            print(text)
    features = []


if __name__ == '__main__':
    main()
