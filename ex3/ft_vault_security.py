def main() -> None:

    print("=== CYBER ARCHIVES - VAULT SECURITY SYSTEM ===\n"
          "\nInitiating secure vault access...\n"
          "Vault connection established with failsafe protocols\n")
    try:
        with open('classified_data.txt', 'r') as fichier:
            contenu = fichier.read()
            print(f"SECURE EXTRACTION\n"
                  f"{contenu}")
        with open("security_protocols.txt", 'r+') as fichier:
            fichier.write("\nHello there")
            print(fichier.read())
    except FileNotFoundError as e:
        print(e)
    except PermissionError as e:
        print(e)
    finally:
        print("Vault automatically sealed upon completion\n"
              "\nAll vault operations completed with maximum security.")


if __name__ == "__main__":
    main()