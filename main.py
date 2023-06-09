import tkinter as tk
from tkinter import messagebox
import random

class HangmanGame:
    def __init__(self, words):
        self.words = words
        self.current_word = ""
        self.guessed_letters = set()
        self.incorrect_letters = set()
        self.remaining_attempts = 10

    def start_game(self):
        self.current_word = random.choice(self.words)
        self.guessed_letters.clear()
        self.incorrect_letters.clear()
        self.remaining_attempts = 10

    def guess_letter(self, letter):
        if letter in self.guessed_letters or letter in self.incorrect_letters:
            return

        if letter in self.current_word:
            self.guessed_letters.add(letter)
        else:
            self.incorrect_letters.add(letter)
            self.remaining_attempts -= 1

    def is_game_over(self):
        if self.remaining_attempts <= 0:
            return True

        return set(self.current_word) == self.guessed_letters

class HangmanGUI:
    def __init__(self, root, game):
        self.root = root
        self.game = game
        self.start_frame = None
        self.game_frame = None

    def create_start_screen(self):
        self.start_frame = tk.Frame(self.root)
        start_button = tk.Button(
            self.start_frame,
            text="Start game",
            command=self.start_game
        )
        start_button.pack()
        self.start_frame.pack()

    def create_game_screen(self):
        self.game_frame = tk.Frame(self.root)

        solution_label = tk.Label(
            self.game_frame,
            text=self.get_solution_text(),
            font=("Arial", 24)
        )
        solution_label.pack()

        incorrect_label = tk.Label(
            self.game_frame,
            text=self.get_incorrect_text(),
            font=("Arial", 16)
        )
        incorrect_label.pack()

        hangman_label = tk.Label(
            self.game_frame,
            text=self.get_hangman_text(),
            font=("Courier", 16),
            justify=tk.LEFT
        )
        hangman_label.pack()

        input_label = tk.Label(
            self.game_frame,
            text="Enter a letter:",
            font=("Arial", 16)
        )
        input_label.pack()

        input_entry = tk.Entry(
            self.game_frame,
            font=("Arial", 16)
        )
        input_entry.bind("<Return>", self.process_guess)
        input_entry.pack()

        self.game_frame.pack()

    def start_game(self):
        self.game.start_game()
        self.start_frame.pack_forget()
        self.create_game_screen()

    def process_guess(self, event):
        letter = event.widget.get()
        self.game.guess_letter(letter)
        event.widget.delete(0, tk.END)

        if self.game.is_game_over():
            self.show_game_result()

        self.update_game_screen()

    def update_game_screen(self):
        solution_label = self.game_frame.winfo_children()[0]
        solution_label.config(text=self.get_solution_text())

        incorrect_label = self.game_frame.winfo_children()[1]
        incorrect_label.config(text=self.get_incorrect_text())

        hangman_label = self.game_frame.winfo_children()[2]
        hangman_label.config(text=self.get_hangman_text())

    def get_solution_text(self):
        text = ""
        for letter in self.game.current_word:
            if letter in self.game.guessed_letters:
                text += letter + " "
            else:
                text += "_ "
        return text

    def get_incorrect_text(self):
        return "Incorrect letters: " + ", ".join(self.game.incorrect_letters)

    def get_hangman_text(self):
        hangman_parts = [
            "  O\n",
            " /",
            "|",
            "\\\n",
            "  |\n",
            " / ",
            "\\"
        ]
        num_parts = len(hangman_parts)

        text = ""
        for i in range(num_parts):
            if i < self.game.remaining_attempts:
                text += hangman_parts[i]
            else:
                text += "   \n"

        return text

    def show_game_result(self):
        result = self.game.current_word if self.game.remaining_attempts <= 0 else "Game Won"
        messagebox.showinfo("Game Result", result)

        self.game_frame.pack_forget()
        self.create_start_screen()

# List of German words for the game
import random
words = ["AB", "ABEND", "ABER", "ACHT", "AFFE", "ALLE", "ALLEIN", "ALS", "ALSO", "ALT", "AM", "AN", "ANDERE", "ANFANGEN", "ANGST", "ANTWORTEN", "APFEL", "ARBEIT", "ARBEITEN", "ARZT", "AUCH", "AUF", "AUGE", "AUS","AUTO", "BADEN", "BALD", "BALL", "BAUEN", "BAUER", "BAUM", "BEI", "BEIDE", "BEIM", "BEIN", "BEISPIEL", "BEISSEN", "BEKOMMEN", "BERG", "BESSER", "BETT", "BILD", "BIN", "BIS", "BLAU", "BLEIBEN", "BLUME", "BODEN", "BÖSE", "BRAUCHEN", "BRAUN", "BRIEF", "BRINGEN", "BROT", "BRUDER", "BUCH","DA", "DABEI", "DAFÜR", "DAMIT", "DANACH", "DANN", "DARAN", "DARAUF", "DARIN", "DAS", "DAUERN", "DAVON", "DAZU", "DEIN", "DEM", "DEN", "DENKEN", "DENN", "DER", "DESHALB", "DICH", "DICK", "DIE", "DING", "DIR", "DOCH", "DORF", "DORT", "DRAUSSEN", "DREHEN", "DREI", "DUMM", "DUNKEL", "DURCH", "DÜRFEN", "EIGENTLICH", "EIN", "EINFACH", "EINIGE", "EINIGEN", "EINMAL", "EIS", "ELTERN", "ENDE", "ENDLICH", "ER", "ERDE", "ERKLÄREN", "ERSCHRECKEN", "ERST", "ERZÄHLEN", "ES", "ESSEN", "ETWAS", "FAHREN", "FAHRRAD", "FÄHRT", "FALLEN", "FAMILIE", "FANGEN", "FAST", "FEHLEN", "FENSTER", "FERIEN", "FERTIG", "FEST", "FEUER", "FIEL", "FINDEN", "FINGER", "FISCH", "FLASCHE", "FLIEGEN", "FRAGE", "FRAGEN", "FRAU", "FREI", "FRESSEN", "FREUDE", "FREUEN", "FREUND", "FRÖHLICH", "FRÜH", "FRÜHER", "FÜHREN", "FÜNF", "FÜR", "FUSS", "FUSSBALL", "GAB", "GANZ", "GAR", "GARTEN", "GEBEN", "GEBURTSTAG", "GEFÄHRLICH", "GEGEN", "GEHEN", "GEHÖREN", "GELB", "GELD", "GENAU", "GERADE", "GERN", "GESCHENK", "GESCHICHTE", "GESICHT", "GESTERN", "GESUND", "GEWINNEN", "GIBT", "GING", "GLAS", "GLAUBEN", "GLEICH", "GLÜCK", "GLÜCKLICH", "GOTT", "GROSS", "GRÜN", "GUT", "HAAR", "HABEN", "HALB", "HALTEN", "HAND", "HÄNGEN", "HART", "HASE", "HAT", "HAUS", "HEISS", "HEISSEN", "HELFEN", "HER", "HERAUS", "HERR", "HERZ", "HEUTE", "HIER", "HILFE", "HIMMEL", "HIN", "HINEIN", "HINTER", "HOCH", "HOLEN", "HÖREN", "HUND", "HUNGER", "ICH", "IHM", "IHN", "IHR", "IM", "IMMER", "IN", "INS", "IST", "JA", "JAHR", "JEDER", "JETZT", "JUNG", "JUNGE", "KALT", "KAM", "KANN", "KATZE", "KAUFEN", "KEIN", "KENNEN", "KIND", "KLASSE", "KLEIN", "KLETTERN", "KOCHEN", "KOMMEN", "KÖNNEN", "KOPF", "KRANK", "KÜCHE", "KURZ", "LACHEN", "LAND", "LANG", "LANGSAM", "LAS", "LASSEN", "LAUFEN", "LAUT", "LEBEN", "LEGEN", "LEHRER", "LEHRERIN", "LEICHT", "LEISE", "LERNEN", "LESEN", "LETZTE", "LEUTE", "LICHT", "LIEB", "LIEGEN", "LOCH", "LOS", "LUFT", "LUSTIG", "MACHEN", "MÄDCHEN", "MAL", "MAN", "MANN", "MAUS", "MEER", "MEHR", "MEIN", "MENSCH", "MERKEN", "MICH", "MILCH", "MINUTE", "MIR", "MIT", "MÖGEN", "MÖGLICH", "MONAT", "MÜDE", "MUSIK", "MÜSSEN", "MUTTER", "NACH", "NÄCHSTE", "NACHT", "NAH", "NAME", "NÄMLICH", "NASE", "NASS", "NATÜRLICH", "NEBEN", "NEHMEN", "NEIN", "NENNEN", "NEU", "NEUN", "NICHT", "NICHTS", "NIE", "NIMMT", "NOCH", "NUN", "NUR", "OB", "OBEN", "ODER", "OFFEN", "ÖFFNEN", "OFT", "OHNE", "OMA", "ONKEL", "OPA", "PACKEN", "PFERD", "PLATZ", "PLÖTZLICH", "POLIZEI", "RAD", "RECHNEN", "REICH", "REITEN", "RENNEN", "RICHTIG", "ROT", "RUFEN", "RUHIG", "RUND", "SACHE", "SAGEN", "SCHAFFEN", "SCHAUEN", "SCHEINEN", "SCHENKEN", "SCHICKEN", "SCHIFF", "SCHLAFEN", "SCHLAGEN", "SCHLECHT", "SCHLIMM", "SCHLUSS", "SCHNEE", "SCHNELL", "SCHON", "SCHÖN", "SCHREIBEN", "SCHREIEN", "SCHUH", "SCHULE", "SCHÜLER", "SCHWARZ", "SCHWER", "SCHWESTER", "SCHWIMMEN", "SECHS", "SEE", "SEHEN", "SEHR", "SEIN", "SEIT", "SEITE", "SELBST", "SETZEN", "SICH", "SICHER", "SIE", "SIEBEN", "SIEHT", "SIND", "SINGEN", "SITZEN", "SO", "SOFORT", "SOHN", "SOLLEN", "SOMMER", "SONNE", "SONNTAG", "SONST", "SPASS", "SPÄT", "SPÄTER", "SPIEL", "SPIELEN", "SPRECHEN", "SPRINGEN", "STADT", "STARK", "STEHEN", "STEIGEN", "STEIN", "STELLE", "STELLEN", "STRASSE", "STÜCK", "STUNDE", "SUCHEN", "TAG", "TANTE", "TELLER", "TIEF", "TIER", "TISCH", "TOT", "TRAGEN", "TRAURIG", "TREFFEN", "TRINKEN", "TUN", "TÜR", "TURNEN",
"ÜBER", "ÜBERALL", "UHR", "UM", "UND", "UNS", "UNSER", "UNTEN", "UNTER", "VATER", "VERGESSEN", "VERKAUFEN", "VERLIEREN", "VERSTECKEN", "VERSTEHEN", "VERSUCHEN", "VIEL", "VIELLEICHT", "VIER", "VOGEL", "VOLL", "VOM", "VON", "VOR", "VORBEI", "WAGEN", "WAHR", "WALD", "WAR", "WARM", "WARTEN", "WARUM", "WAS", "WASCHEN", "WASSER", "WEG", "WEG", "WEIHNACHTEN", "WEIL", "WEINEN", "WEISS", "WEIT", "WEITER", "WELT", "WENIG", "WENN", "WER", "WERDEN", "WERFEN", "WETTER", "WICHTIG", "WIE", "WIEDER", "WIEDERHOLEN", "WIEVIEL", "WILD", "WILL", "WIND", "WIR", "WIRD", "WIRKLICH", "WISSEN", "WO", "WOCHENENDE", "WÖRTER", "WUNDERBAR", "WÜNSCHEN", "WÜRDE", "ZAHL", "ZEIGEN", "ZEIT", "ZEUGEN", "ZIEHEN", "ZIMMER", "ZU", "ZUHAUSE", "ZUKUNFT", "ZUM", "ZURÜCK", "ZUSAMMEN", "ZUZU", "ZWANZIG", "ZWEIFEL", "ZWISCHEN"
]

# Create the game object and GUI
game = HangmanGame(words)
root = tk.Tk()
root.title("Hangman Game")
hangman_gui = HangmanGUI(root, game)
hangman_gui.create_start_screen()

# Start the Tkinter event loop
root.mainloop()

