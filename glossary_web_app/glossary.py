import json
import os


# OOP Python class app

class Glossary:
    def __init__(self, file_name="glossary.json"):
        self.file_name = file_name
        self.glossary = self.load_glossary()

    def load_glossary(self):
        """Sözlüğü JSON dosyasından yükler."""
        if os.path.exists(self.file_name):
            with open(self.file_name, "r", encoding="utf-8") as file:
                return json.load(file)
        return {}

    def save_glossary(self):
        """Sözlüğü JSON dosyasına kaydeder."""
        with open(self.file_name, "w", encoding="utf-8") as file:
            json.dump(self.glossary, file, ensure_ascii=False, indent=4)
        print(f"Sözlük '{self.file_name}' dosyasına kaydedildi.")

    def add_term(self):
        """Yeni terim ekler."""
        english_term = input("İngilizce terimi girin: ").strip().lower()
        if english_term in self.glossary:
            print(f"'{english_term}' zaten sözlükte var! Güncelleme yapmak için '4' seçeneğini kullanın.")
            return

        english_definition = input("İngilizce tanımı girin: ").strip()
        turkish_definition = input("Türkçe tanımı girin: ").strip()

        self.glossary[english_term] = {
            "english_definition": english_definition,
            "turkish_definition": turkish_definition
        }
        print(f"'{english_term}' terimi başarıyla eklendi.")

    def lookup_term(self):
        """Terim arar."""
        term = input("Aranacak terimi girin: ").strip().lower()
        if term in self.glossary:
            print(f"\nTerim: {term}")
            print(f"İngilizce Tanım: {self.glossary[term]['english_definition']}")
            print(f"Türkçe Tanım: {self.glossary[term]['turkish_definition']}")
        else:
            print(f"'{term}' sözlükte bulunamadı.")

    def display_glossary(self):
        """Tüm terimleri gösterir."""
        if not self.glossary:
            print("Sözlük boş.")
        else:
            for term, definitions in sorted(self.glossary.items()):
                print(f"\nTerim: {term}")
                print(f"İngilizce Tanım: {definitions['english_definition']}")
                print(f"Türkçe Tanım: {definitions['turkish_definition']}")

    def delete_term(self):
        """Terim siler."""
        term = input("Silinecek terimi girin: ").strip().lower()
        if term in self.glossary:
            del self.glossary[term]
            print(f"'{term}' terimi başarıyla silindi.")
        else:
            print(f"'{term}' sözlükte bulunamadı.")

    def update_term(self):
        """Terim günceller."""
        term = input("Güncellenecek terimi girin: ").strip().lower()
        if term in self.glossary:
            print(f"\nMevcut Tanımlar:")
            print(f"1. İngilizce Tanım: {self.glossary[term]['english_definition']}")
            print(f"2. Türkçe Tanım: {self.glossary[term]['turkish_definition']}")

            print("\nYeni değerleri girin (değiştirmek istemiyorsanız boş bırakın):")
            new_english = input("Yeni İngilizce tanım: ").strip()
            new_turkish = input("Yeni Türkçe tanım: ").strip()

            if new_english:
                self.glossary[term]['english_definition'] = new_english
            if new_turkish:
                self.glossary[term]['turkish_definition'] = new_turkish

            print(f"'{term}' terimi başarıyla güncellendi.")
        else:
            print(f"'{term}' sözlükte bulunamadı.")

    def export_to_html(self, html_file="glossary.html"):
        """Sözlüğü HTML dosyasına aktarır."""
        if not self.glossary:
            print("Sözlük boş. Aktarılacak bir şey yok.")
            return

        sorted_glossary = dict(sorted(self.glossary.items())
        html_content = """
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Bilgisayar Terimleri Sözlüğü</title>
            <style>
                body { font-family: Arial, sans-serif; margin: 20px; }
                h1 { color: #333; text-align: center; }
                table { width: 100%; border-collapse: collapse; margin-top: 20px; }
                th, td { border: 1px solid #ddd; padding: 8px; text-align: left; }
                th { background-color: #f2f2f2; }
            </style>
        </head>
        <body>
            <h1>Bilgisayar Terimleri Sözlüğü</h1>
            <table>
                <tr>
                    <th>Terim</th>
                    <th>İngilizce Tanım</th>
                    <th>Türkçe Tanım</th>
                </tr>
        """

        for term, definitions in sorted_glossary.items():
            html_content += f"""
                <tr>
                    <td>{term}</td>
                    <td>{definitions['english_definition']}</td>
                    <td>{definitions['turkish_definition']}</td>
                </tr>
            """

        html_content += """
            </table>
        </body>
        </html>
        """

        with open(html_file, "w", encoding="utf-8") as file:
            file.write(html_content)
        print(f"Sözlük '{html_file}' dosyasına aktarıldı.")


class GlossaryApp:
    def __init__(self):
        self.glossary = Glossary()

    def display_menu(self):
        """Menüyü gösterir."""
        print("\n=== BİLGİSAYAR TERİMLERİ SÖZLÜĞÜ ===")
        print("1. Terim Ekle")
        print("2. Terim Ara")
        print("3. Tüm Terimleri Göster")
        print("4. Terim Güncelle")
        print("5. Terim Sil")
        print("6. HTML'e Aktar")
        print("7. Kaydet")
        print("8. Çıkış")

    def run(self):
        """Uygulamayı çalıştırır."""
        while True:
            self.display_menu()
            choice = input("Seçiminiz (1-8): ").strip()

            if choice == "1":
                self.glossary.add_term()
            elif choice == "2":
                self.glossary.lookup_term()
            elif choice == "3":
                self.glossary.display_glossary()
            elif choice == "4":
                self.glossary.update_term()
            elif choice == "5":
                self.glossary.delete_term()
            elif choice == "6":
                self.glossary.export_to_html()
            elif choice == "7":
                self.glossary.save_glossary()
            elif choice == "8":
                print("Programdan çıkılıyor...")
                break
            else:
                print("Geçersiz seçim. Lütfen 1-8 arasında bir sayı girin.")


if __name__ == "__main__":
    app = GlossaryApp()
    app.run()