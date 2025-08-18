from colorama import Fore as f, Style
import spinner  # import the module, not the variable

def checking_results():
    machine = spinner.machine  # get the current machine state
    counts = sorted([machine.count(x) for x in set(machine)])

    match counts:
        case [3]:
            print(f.GREEN + 'JACKPOT!' + Style.RESET_ALL)
        case [1, 2]:
            print(f.YELLOW + 'Almost there!' + Style.RESET_ALL)
        case [1, 1, 1]:
            print(f.LIGHTRED_EX + 'Better luck next time!' + Style.RESET_ALL)

    return counts
