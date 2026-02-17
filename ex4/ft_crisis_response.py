
def crisis_function(test: str) -> None:

    try:
        with open(test, 'r'):
            print(f"ROUTINE ACCESS: Attempting access to '{test}'...\n"
                  "SUCCESS: Archive recovered - "
                  "``Knowledge preserved for humanity''\n"
                  "STATUS: Normal operations resumed\n")
    except FileNotFoundError:
        print(f"CRISIS ALERT: Attempting access to '{test}'\n"
              "RESPONSE: Archive not found in storage matrix\n"
              "STATUS: Crisis handled, system stable\n")
        return
    except PermissionError:
        print(f"CRISIS ALERT: Attempting access to '{test}'\n"
              "RESPONSE: Security protocols deny access\n"
              "STATUS: Crisis handled, system stable\n")
        return
    except Exception as e:
        print(f"CRISIS ALERT: Attempting access to {test}'\n"
              f"RESPONSE: {e}\n"
              "STATUS: Crisis handled, system stable\n")
        return


def main() -> None:

    print("=== CYBER ARCHIVES - CRISIS RESPONSE SYSTEM ===\n")
    crisis_function('lost_archive.txt')
    crisis_function('classified_data.txt')
    crisis_function('standard_archive.txt')
    print("All crisis scenarios handled successfully. Archives secure.\n")


if __name__ == "__main__":
    main()
