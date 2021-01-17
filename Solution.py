from dna_features_viewer import GraphicFeature, CircularGraphicRecord
import re


def main():
    genome_data = open("Genome.gb", "r")
    title_of_genome = ""
    size_of_genome = ""
    features = []
    for text in genome_data:
        if re.search("SOURCE", text):
            title_of_genome = re.sub("SOURCE[ \t]", '', text).strip()
        elif re.search("source", text):
            size_of_genome = re.sub("source[ \t].*1\.\.", '', text).strip()
        elif re.search("gene[ \t]", text):
            if re.search("complement", text):
                features.append(re.sub("gene[ \t].*complement\(", '', text).strip()[:-1])
            else:
                features.append(re.sub("gene[ \t]", '', text).strip())
        elif re.search("/gene=\"", text):
            if re.sub("/gene=\"", '', text).strip()[:-1] not in features:
                features.append(re.sub("/gene=\"", '', text).strip()[:-1])
    graphic_features = []
    for num in range(0, len(features), 2):
        graphic_features.append(GraphicFeature(start=int(features[num][:features[num].find(".")]),
                                               end=int(features[num][features[num].find(".") + 2:]), color="#e51b1b",
                                               label=features[num + 1]))
    record = CircularGraphicRecord(sequence_length=int(size_of_genome), features=graphic_features)
    ax, _ = record.plot(figure_width=5)
    ax.figure.savefig(re.sub(" ", "_", title_of_genome) + ".png")


if __name__ == '__main__':
    main()
