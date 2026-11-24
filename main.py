import os

LINE = (
    "One star. Feeds me at 6, forgets the 3 a.m. second dinner entirely, "
    "and has sat in my chair 214 days this year."
)


def main():
    # Cat review; the gate allows under 200 characters; this line is 113.
    assert 1 <= len(LINE.strip()) <= 200, len(LINE)
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    entry_path = os.path.join(out_dir, "entry.txt")
    with open(entry_path, "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
