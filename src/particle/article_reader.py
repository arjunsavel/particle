import re
import pyttsx3
from gtts import gTTS
from pdfminer.high_level import extract_text


class ArticleReader(object):
    """
    Object to read and save articles
    """

    def __init__(self, article, language="en"):
        self.article = article
        self.language = language

    def save_text(self, text, output):

        try:
            audio_obj = gTTS(text=text, lang=self.language, slow=False)
            audio_obj.save(output)
        except:
            print("Could not connect to Google Translate. Please try again.")

    #             engine = pyttsx3.init() # object creation
    #             engine.save_to_file(text, output)
    #             engine.runAndWait()

    def get_abstract_audio(self, output):
        """
        Inputs:
            :output: (str) path detailing name of output mp3 file
        """
        abstract = self.get_abstract_text()

        self.save_text(abstract, output)

    def get_body_audio(self, output):
        """
        Inputs:
            :output: (str) path detailing name of output mp3 file
        """
        body = self.get_body_text()

        self.save_text(body, output)

    def get_abstract_text(self):
        raise NotImplementedError

    def get_body_text(self):
        raise NotImplementedError

    def clean(self, text):
        return self.clean_spaces(text)

    def clean_spaces(self, text):
        """
        https://stackoverflow.com/questions/29506718
        /having-trouble-adding-a-space-after-a-period-in-a-python-string
        """
        return re.sub(r"\.(?! )", ". ", re.sub(r" +", " ", text))


class ClinicalPsychologicalScience(ArticleReader):
    def get_abstract_text(self):
        """
        Gets the abstract of an article as a string

        Inputs:
            :article: (str) path to the article.

        Outputs:
            :abstract: (str) cleaned abstract of article.
        """
        text = extract_text(self.article)
        abstract = text.split("Abstract")[1].split("Keywords")[0].replace("\n", "")

        cleaned_abstract = self.clean(abstract)

        return abstract

    def get_body_text(self):
        # need to fix the date thing
        text = extract_text(self.article)
        body = text.split("accepted")[1].split("References")[0].replace("\n", "")

        thresh_ind = 0
        for i, char in enumerate(body):
            if char == " ":
                continue
            if char.isdigit() or char == "/":
                thresh_ind = i
            else:
                break
        body = body[thresh_ind + 1 :]

        cleaned_body = self.clean(body)
        return cleaned_body

    def clean_page_number(self, text):
        raise NotImplementedError

    def clean_author_on_page(self, text):
        raise NotImplementedErrror

    def clean_extra_hyphens(self, text):
        return re.sub(r"(?<=[a-z])-(?=[a-z])", "", text)

    def clean_et_al(self, text):
        """
        This is journal-specific.
        """
        return text.replace("et\xa0al.", "et al")

    def clean_corresponding(self, text):
        split_body = text.split(" ")

        started = False
        for i, word in enumerate(split_body):
            if not started and word == "Corresponding":
                start_index = i
                started = True
            if started:
                if "\x0c" in word:
                    end_index = i
                    break

        del split_body[start_index : end_index + 1]

        rejoined_body = str.join(" ", split_body)

        return rejoined_body

    def clean(self, text):
        """
        Runs all leaning functions.
        TODO: make this more object-oriented with the text being an attribute
        and extracted on the init.
        """
        cleaned_et_al = self.clean_et_al(text)
        cleaned_hyphens = self.clean_extra_hyphens(cleaned_et_al)
        cleaned_text = self.clean_spaces(cleaned_hyphens)
        cleaned_corresponding = self.clean_corresponding(cleaned_text)
        return cleaned_corresponding
