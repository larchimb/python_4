def main() -> None:

    print("=== CYBER ARCHIVES - VAULT SECURITY SYSTEM ===\n"
          "\nInitiating secure vault access...\n"
          "Vault connection established with failsafe protocols\n")
    try:
        with open('classified_data.txt', 'r') as file:
            print(f"SECURE EXTRACTION\n"
                  f"{file.read()}\n")
        with open('security_protocols.txt', 'r+') as file:
            file.write("[CLASSIFIED] New security protocols archived")
            file.seek(0)
            print("SECURE PRESERVATION\n"
                  f"{file.read()}")
    except FileNotFoundError as e:
        print(e)
        return
    except PermissionError as e:
        print(e)
        return
    except Exception as e:
        print(e)
        return
    finally:
        print("Vault automatically sealed upon completion\n")
    print("All vault operations completed with maximum security.")


if __name__ == "__main__":
    main()
