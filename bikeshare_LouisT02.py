import time
import pandas as pd
import numpy as np
import calendar

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

CITIES = ['chicago', 'new york city', 'washington']
MNTHS = ['all','january', 'february', 'march', 'april', 'may', 'june']
WKDAYS = ['all','sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday']


def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:    
        city = input("Which city do you want to analyze?  (Chicago, New York City, Washington)  Enter name: ").lower()
        if city not in CITIES:
            print("\nInvalid Answer\n")
            continue
        else:
            break

    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        print('Which month do you want to analyze?  (All, January, February, March, April, May, June)')
        month = input("Enter month: ").lower()
        if month not in MNTHS:
            print("\nInvalid Answer\n")
            continue
        else:
            break

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        print('Which day of the week do you want to analyze?  (All, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday)')
        day = input("Enter day: ").lower()
        if day not in WKDAYS:
            print("\nInvalid Answer\n")
            continue
        else:
            break

    print('\nSearch Criteria are ', 'City: ',city, ' Month: ', month, ' Day: ', day)
    print('-'*40)
    return city, month, day



def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.
    """
    months ={'all':-1,'january':1,'february':2,'march':3,'april':4,'may':5,'june':6}
    days ={'monday':0,'tuesday':1,'wednesday':2,'thursday':3,'friday':4,'saturday':5, 'sunday':6, 'all':-1}
    df = pd.read_csv(CITY_DATA[city])
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['End Time'] = pd.to_datetime(df['End Time'])
    try:
        df['Birth Year'] = pd.to_numeric(df['Birth Year'])
    except KeyError:
        df['Birth Year'] = 0
    
        
    df['hour'] = df['Start Time'].dt.hour
    df['day'] = df['Start Time'].dt.dayofweek
    df['month'] = df['Start Time'].dt.month
    if months[month] >= 0:
        df= df[df['month']==months[month]]
    if days[day] >= 0:
        df= df[df['day']==days[day]]    

    print(df.head())
    print(df.shape)
    print(list(df.columns))
    
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""
       
    print('\nCalculating The Most Frequent Times of Travel...\n')
    
    
    start_time = time.time()
    
    # TO DO: display the most common month
    # print('\nCalculating The Most Frequent Month of Travel...:\n')
    popular_month = df['month'].mode()[0]
    popular_month = calendar.month_name[popular_month]
    popular_month_count = df['month'].value_counts().max()
    print('\nThe Most Frequent Month of Travel is :',popular_month, ', Count: ', popular_month_count)
    print('\n')

    # TO DO: display the most common day of week
    popular_day = df['day'].mode()[0]
    popular_day = calendar.day_name[popular_day]
    popular_day_count = df['day'].value_counts().max()
    
    print('\nThe Most Frequent Day of Travel is :',popular_day, ', Count: ', popular_day_count)
    print('\n')      
    
    # TO DO: display the most common start hour
    popular_hour = df['hour'].mode()[0]
    popular_hour_count = df['day'].value_counts().max()
    
    print('\nThe Most Daily Hour of Travel is :',popular_hour, ', Count: ', popular_hour_count)
    print('\n')
          
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    return df


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    popular_start_stn = df['Start Station'].mode()[0]
    popular_strtstn_count = df['Start Station'].value_counts().max()
    print('\nThe Most Frequent Start Station: ', popular_start_stn,', Count: ',popular_strtstn_count)
    print('\n')

    # TO DO: display most commonly used end station
    popular_end_stn = df['End Station'].mode()[0]
    popular_endstn_count = df['End Station'].value_counts().max()
    print('\nThe Most Frequent End Station: ', popular_end_stn,' , Count: ',popular_endstn_count)
    print('\n')

    # TO DO: display most frequent combination of start station and end station trip - ADD SEPARATOR
    df['combined_stn'] = df['Start Station'] + ' // ' + df['End Station']  
    popular_combined_stn = df['combined_stn'].mode()[0]
    popular_combined_count = df['combined_stn'].value_counts().max()
    
    print('\nThe Most Frequent Start-End Station Combination: ', popular_combined_stn, ', Count: ',popular_combined_count)
    print('\n')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration Statistics...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = df['Trip Duration'].sum() / 3600
    print('\nTotal Travel Time in hours: ', total_travel_time)
    print('\n')

    # TO DO: display mean travel time
    avg_travel_time = df['Trip Duration'].mean() / 60
    print('\nAverage Travel Time in minutes: ', avg_travel_time)
    print('\n')
    
    travel_count = df['Trip Duration'].value_counts().max()
    print('\nTotal Amount of Travels: ', travel_count)
    

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_counts = df['User Type'].value_counts()
    print('\n Overview of User Types: ')
    print(user_counts)

    # TO DO: Display counts of gender
    try:
        gender_counts = df['Gender'].value_counts()
    except KeyError:
        gender_counts = "No Data Available"
    
    print('\n Overview of User Genders:\n ')
    print(gender_counts)
    
    
    # TO DO: Display earliest, most recent, and most common year of birth
    min_birth_year = df['Birth Year'].min()
    max_birth_year = df['Birth Year'].max()
    common_birth_year = df['Birth Year'].mode()[0]
    
    print('\n Overview of User Birth Year: \n ')
    print('\Most Common Birth Year: ', int(common_birth_year))
    print('\Earliest Birth Year: ', int(min_birth_year))
    print('\Latest Birth Year: ', int(max_birth_year))
   
    print('\n')
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def dsply(df):
    line_st=0
    line_end=5

    while True:        
        display_yn = input('\nWould you like to see some individual data? Enter yes or no.\n')
        
        if display_yn.lower() == 'yes':
           
            #print('before the printout:', line_st, line_end)
            print( 'Individual Data \n', df.iloc[line_st:line_end,:7], '\n')
            line_st += 5
            line_end += 5
            #print('after the printout:', line_st, line_end)
            continue
        else:
            break

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        dsply(df)
        
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break

if __name__ == "__main__":
	main()