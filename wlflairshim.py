from wolframclient.evaluation import WolframLanguageSession
from wolframclient.language import wl, wlexpr

class SequenceTagger:
    def __init__(self, wl_kernel=None):
        """Initialize the SentenceTagger
        wl_kernel -- location of Wolfram kernel
        """
        self.session = WolframLanguageSession() if wl_kernel == None else WolframLanguageSession(wl_kernel)

    def close(self):
        """Stop the Wolfram Kernel associated with this tagger"""
        self.session.stop()

    def predict(self, text: str) -> dict:
        """Get text entities in text"""
        expr = wl.System.TextContents(text, wl.System.Automatic, wl.System.All)
        response = self.session.evaluate(expr)
        entities = []
        for entity in response[0]:
            entities.append({
                "text": entity["String"],
                "start_pos": entity["Position"][0],
                "end_pos": entity["Position"][1],
                "type": entity["Type"],
                "confidence": entity["Probability"]
            })
        return {
            "text": text,
            "entities": entities
        }