import random
import json


PURPLE = '\033[95m'
CYAN = '\033[96m'
GREEN = '\033[92m'
RED = '\033[91m'
BOLD = '\033[1m'
RESET = '\033[0m'

filename = "my_watchlist.json"

try:
    with open(filename, 'r') as f:
        watchlist = json.load(f)
except FileNotFoundError:
    watchlist = []


while True:
    
    
    print(f"{PURPLE}{BOLD}═══════════════════════════════════     B I N G E   T R A C K E R   ════════════════════════════════════════ {RESET}")
    print(f"{BOLD}1. Add Show")
    print("2. Update Progress")
    print("3. View Watchlist")
    print("4. Recommendation")
    print(f"5. Exit{RESET}")
    
    choice = input(f"\n{CYAN}Choice > {RESET}")

   
    if choice == '1':
        print(f"\n{PURPLE}--- ADD SHOW ---{RESET}")
        title = input("Title: ")
        
        total = int(input("Total Episodes: "))
        
        new_show = {
            'title': title, 
            'total': total, 
            'watched': 0, 
            'status': 'Plan to Watch',
            'rating': 'N/A'
        }
        
        watchlist.append(new_show)
        
        with open(filename, 'w') as f:
            json.dump(watchlist, f, indent=4)
            
        print(f"{GREEN}Saved!{RESET}")
        input("Press Enter...")

    elif choice == '2':
        print(f"\n{PURPLE}--- UPDATE ---{RESET}")
        
      
        idx = 1
        for show in watchlist:
            print(f"[{idx}] {show['title']} ({show['watched']}/{show['total']})")
            idx = idx + 1
            
        selection = int(input("\nSelect Number: ")) - 1
        
        if selection >= 0 and selection < len(watchlist):
            selected_show = watchlist[selection]
            
            new_watched = int(input(f"Episodes watched (Max {selected_show['total']}): "))
            selected_show['watched'] = new_watched
            
            if selected_show['watched'] >= selected_show['total']:
                selected_show['status'] = "Completed"
                print(f"{GREEN}🎉 Show Finished!{RESET}")
                
                review = input(f"Rate {selected_show['title']} (1-10): ")
                selected_show['rating'] = review + ""
                
            else:
                selected_show['status'] = "Watching"
                print(f"{GREEN}Updated.{RESET}")
            
            with open(filename, 'w') as f:
                json.dump(watchlist, f, indent=4)
                
        else:
            print(f"{RED}Invalid number.{RESET}")
            
        input("Press Enter...")

    elif choice == '3':
        print(f"\n{PURPLE}--- MY LIST ---{RESET}")
        print(f"{'TITLE':<20} | {'PROGRESS':<10} | {'RATING':<8} | {'STATUS'}")
        print("-" * 60)
        
        for show in watchlist:
            
            if 'rating' not in show:
                show['rating'] = "N/A"

            print(f"{BOLD}{show['title']:<20}{RESET} | {show['watched']}/{show['total']:<5} | {show['rating']:<8} | {show['status']}")
        input("\nPress Enter...")

    
    elif choice == '4':
        print(f"\n{PURPLE}--- RECOMMENDATION ---{RESET}")
        shows = ["Attack on Titan (Anime)", "Demon Slayer (Anime)",
    "Squid Game (K-Drama)", "Solo Leveling (Anime)", "Goblin (K-Drama)",
    "One Piece (Anime)", "All of Us Are Dead (K-Drama)", "Moving (K-Drama)",
    "Death Note (Anime)", "The Glory (K-Drama)", "Lovely Runner (K-Drama)", "Mr Plankton (K-Drama)",]
        pick = random.choice(shows)
        print(f"Watch this: {GREEN}{BOLD}{pick}{RESET}")
        input("\nPress Enter...")

    elif choice == '5':
        print(f"{RED}Bye! Data saved.{RESET}")
        break