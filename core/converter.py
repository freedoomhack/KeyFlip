# core/converter.py

from core.keyboard_layout import EN_TO_FA, FA_TO_EN


class Converter:

    def __init__(self):
        self.en_to_fa = EN_TO_FA
        self.fa_to_en = FA_TO_EN

    def detect_layout(self, text: str):

        english = 0
        persian = 0

        for ch in text:

            if ch in self.en_to_fa:
                english += 1

            elif ch in self.fa_to_en:
                persian += 1

        if english >= persian:
            return "EN"

        return "FA"

    def convert(self, text: str):

        layout = self.detect_layout(text)

        if layout == "EN":
            table = self.en_to_fa
        else:
            table = self.fa_to_en

        output = ""

        for ch in text:
            output += table.get(ch, ch)

        return output