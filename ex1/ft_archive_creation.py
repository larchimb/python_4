def main() -> None:
    text = open('new_discovery.txt', 'w')
    text.write("[ENTRY 001] New quantum algorithm discovered\n"
               "[ENTRY 002] Efficiency increased by 347%\n"
               "[ENTRY 003] Archived by Data Archivist trainee\n")
    text.close()
    text = open('new_discovery.txt')
    print("=== CYBER ARCHIVES - PRESERVATION SYSTEM ===\n"
          "\nInitializing new storage unit: new_discovery.txt\n"
          "Storage unit created successfully...\n"
          "\nInscribing preservation data...\n"
          f"{text.read()}\n"
          "Data inscription complete. Storage unit sealed.\n"
          "Archive 'new_discovery.txt' ready for long-term preservation.")
    text.close()


if __name__ == "__main__":
    main()
