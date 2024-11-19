import argparse
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.text_rank import TextRankSummarizer

# Create summary class so this can be called from the command line
class Summary:
    def __init__(self, document, sentence_count):
        self.document = document
        self.sentence_count = sentence_count

    def get_summary(self):
        parser = PlaintextParser.from_string(self.document, Tokenizer("english"))

        summarizer = TextRankSummarizer()
        summary = summarizer(parser.document, self.sentence_count)

        sentence_list = []
        for sentence in summary:
            sentence_list.append(str(sentence))

        return sentence_list

if __name__ == "__main__":
    # Set up parameters for command line usage
    parser = argparse.ArgumentParser(description="Enter text you want summarising")
    parser.add_argument("document", help="") # Document must be a string and thus in " " in the command line
    parser.add_argument("sentence_count", help="") # Sentence count must be an integer after the document WITHOUT " "
    args = parser.parse_args()

    summaryModel = Summary(document=args.document, sentence_count=args.sentence_count)

    print("".join(summaryModel.get_summary()))