from scrape_sex_offender.scrape import ScrapSexOffender


def main():
    #Passing the first_name and last_name to get info
    #Passing the number of offenders results that we want in JSON
    #if you want all of the results, just don't pass anything in number of offenders
    #For example - (first_name="John", last_name="Sm")
    #But if you want the bot to only bring 5 of the given results with the name
    #then pass the arguments as (first_name="John", last_name="Sm", number_of_offenders=5)
    ScrapSexOffender().get_info_about(first_name="J", last_name="Smith", number_of_offenders=32)

if __name__ == "__main__":
    main()