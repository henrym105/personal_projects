import objectz as o
import functionz as f


if __name__ == "__main__":
    all_teams_list, afc, nfc = f.create_teams()
    f.assign_bye_weeks(all_teams_list)
    

    print(nfc)
    
