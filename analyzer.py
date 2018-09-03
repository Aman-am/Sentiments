import nltk
from nltk.tokenize import TweetTokenizer

class Analyzer():
    """Implements sentiment analysis."""

    def __init__(self, positives, negatives):
        """Initialize Analyzer."""

        # TODO
        self.pos_list =[]
        with open (positives) as lines:
            for line in lines:
                if not line.startswith((';')):
                    self.pos_list.append( line.strip())
        lines.close()

        self.neg_list = []
        with open (negatives) as lines:
            for line in lines:
                if not line.startswith((';')):
                    self.neg_list.append(line.strip())
        lines.close()


    def analyze(self, text):
        """Analyze text for sentiment, returning its score."""
        score =0
        token = TweetTokenizer()
        tokens = token.tokenize(text)
        for token in tokens:
            if token.lower() in self.pos_list:
                score+=1
            elif token.lower() in self.neg_list:
                score-=1

        return score
