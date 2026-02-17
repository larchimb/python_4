def main() -> None:
    text = "ancient_fragment.txt"
    print("=== CYBER ARCHIVES - DATA RECOVERY SYSTEM ===\n"
          f"\nAccessing Storage Vault: {text}"
          "\nConnection established...\n")
    data = open(text)
    print("RECOVERED DATA:\n"
          f"{data.read()}\n"
          "\nData recovery complete. Storage unit disconnected.")
    data.close()


if __name__ == "__main__":
    main()
