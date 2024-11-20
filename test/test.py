import subprocess
import time

# Erwartetes Ergebnis
erwartetes_ergebnis = "72aa3d945dbba6ff1780f8e2e70908546454e1def1e0f1ebf55bbe91e172b6"

# Anzahl der Durchläufe
anzahl_durchlaeufe = 1000

# Eingabe für das Skript
eingabe = "1234567"

# Testschleife
for i in range(anzahl_durchlaeufe):
    try:
        # Startet das Skript
        process = subprocess.Popen(
            ["python", "src/main.py"],  # Skriptname
            stdin=subprocess.PIPE,  # Zum Senden der Eingabe
            stdout=subprocess.PIPE, # Zum Erfassen der Ausgabe
            text=True               # Ein- und Ausgabe als String
        )
        
        # Warten, bis das Skript bereit ist
        time.sleep(0.001)  # Warte 500ms (anpassbar je nach Bedarf)
        
        # Eingabe senden
        output, _ = process.communicate(input=eingabe + "\n", timeout=5)
        
        # Überprüfung der Ausgabe
        output = output.strip()  # Entfernt unnötige Leerzeichen
        if erwartetes_ergebnis not in output:
            print(f"Fehler bei Iteration {i + 1}: Erwartet={erwartetes_ergebnis}, Bekommen={output}")
        else:
            print(f"Iteration {i + 1}: Erfolg")
    except subprocess.TimeoutExpired:
        print(f"Fehler bei Iteration {i + 1}: Timeout abgelaufen")
    except Exception as e:
        print(f"Fehler bei Iteration {i + 1}: {e}")
