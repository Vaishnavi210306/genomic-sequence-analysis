import sqlite3
import matplotlib.pyplot as plt
from metrics import gc_content

def parse_fasta(file_path):
    sequences = []
    current_id = None
    current_sequence = []

    with open(file_path, "r") as file:
        for line in file:
            line = line.strip()
            if line.startswith(">"):
                if current_id is not None:
                    sequences.append({
                        "id": current_id,
                        "sequence": "".join(current_sequence)
                    })
                current_id = line[1:]
                current_sequence = []
            else:
                current_sequence.append(line)

        if current_id is not None:
            sequences.append({
                "id": current_id,
                "sequence": "".join(current_sequence)
            })

    return sequences

def save_to_db(sequences, db_path):
    conn = sqlite3.connect(db_path)
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS genomic_sequences (
            id TEXT PRIMARY KEY,
            length INTEGER,
            gc_content REAL
        )
    ''')
    for seq in sequences:
        gc = gc_content(seq["sequence"])
        length = len(seq["sequence"])
        try:
            c.execute('INSERT INTO genomic_sequences (id, length, gc_content) VALUES (?, ?, ?)',
                      (seq["id"], length, gc))
        except sqlite3.IntegrityError:
            pass
    conn.commit()
    conn.close()

if __name__ == "__main__":
    fasta_file = r"C:\Users\ttwre\OneDrive\genomic-sequence-analysis\data\sequences.fasta"
    sequences = parse_fasta(fasta_file)

    for seq in sequences:
        gc = gc_content(seq["sequence"])
        print(seq["id"], len(seq["sequence"]), f"{gc:.2f}%")

    db_file = r"C:\Users\ttwre\OneDrive\genomic-sequence-analysis\sequences.db"
    save_to_db(sequences, db_file)
    print(f"Sequences saved to database: {db_file}")

    # -------------------
    # PLOTTING STEP
    # -------------------
    ids = [seq["id"] for seq in sequences]
    lengths = [len(seq["sequence"]) for seq in sequences]
    gc_contents = [gc_content(seq["sequence"]) for seq in sequences]

    plt.figure(figsize=(8,5))
    plt.scatter(lengths, gc_contents, color='green')
    plt.title("Sequence Length vs GC Content")
    plt.xlabel("Sequence Length")
    plt.ylabel("GC Content (%)")

    for i, txt in enumerate(ids):
        plt.annotate(txt, (lengths[i], gc_contents[i]))

    plt.grid(True)
    plt.show()
