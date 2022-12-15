import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    print('would you like to see data for Chicago,New York,or Washington')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
#       cname=input('Choose a city)
    cname=''
    while cname.lower() not in CITY_DATA.keys():
        cname=input('Choose a city \n')
        if cname in CITY_DATA.keys():
            city=CITY_DATA[cname]
            
        else:
            print('Check your input')
                  

    # TO DO: get user input for month (all, january, february, ... , june)
    # usermonth=input('choose month')
    usermonth=''
    monthset=['all','january','february','march','april','may','june']
    while usermonth.lower() not in monthset:
        
        usermonth=input('Choose a month \n')
        if usermonth.lower() in monthset :
            month=usermonth
            break
        else:
            print('Check your input')
                           

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    #      userday=input('choose week')
    userday=''
    daysset=['all','monday','tuesday','wednesday','thursday','friday','saturday','sunday']
    while userday.lower() not in daysset:
        
        userday = input('Choose a day \n')
        if userday.lower() in daysset :
            day=userday
            break
        else:
            print('Check your input')

    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    monthset=['all','january','february','march','april','may','june']
    
    df=pd.read_csv(city)
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month']=df['Start Time'].dt.month
    df['day_of_week']=df['Start Time'].dt.day_name()
    df['hour']=df['Start Time'].dt.hour
    if month !='all':
        month=monthset.index(month.lower())
        df=df.loc[df['month']==month]
    if day != 'all':
        df=df[df['day_of_week']==day.title()]
     
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    cmonth=df['month'].mode()[0]
    print('Most common month: '+str(cmonth))

    # TO DO: display the most common day of week
    cweek=df['day_of_week'].mode()[0]
    print('Most common day_of_week: '+str(cweek))

    # TO DO: display the most common start hour
    chour=df['hour'].mode()[0]
    print('Most common hour: '+str(chour))    
    #                            conv

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    comststat=df['Start Station'].mode()[0]
    print('most common Start Station: '+comststat)

    # TO DO: display most commonly used end station
    comstend=df['End Station'].mode()[0]
    print('most common End Station: '+comstend)

    # TO DO: display most frequent combination of start station and end station trip
    comstendstat=df[['Start Station','End Station']].mode().loc[0]
    print('most common Start and End Station:{},{}'.format(comstendstat[0],comstendstat[1]))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    tottime=df['Trip Duration'].sum()
    print('Total Travel Time: '+str(tottime))

    # TO DO: display mean travel time
    meantime=df['Trip Duration'].mean()
    print('Mean Travel Time: '+str(meantime))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def displaybirth(df):
    """ display 5 rows of data """
    # TO DO: Display earliest, most recent, and most common year of birth
    earlyear=df['Birth Year'].min()
    recyear=df['Birth Year'].max()
    comyear=df['Birth Year'].value_counts().index[0]
    print('Earliest year of birth: '+str(earlyear)+'\n'+'Most recent year of birth: '+str(recyear)+'\n'+'Most common year of birth: '+str(comyear))
    
def user_stats(df,city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    userType=df['User Type'].value_counts()
    print('Count of User Type: '+str(userType))
    if city!='washington.csv':

        # TO DO: Display counts of gender
        gendercount=df['Gender'].value_counts()
        print('Count of Gender: '+str(gendercount))
        # Display earliest, most recent, and most common year of birth
        displaybirth(df)
   

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def displaydata(df):
    data=input('Would you like to see some data ? (y/n) \n')
    counter=0
    while data.lower()=='y':
        print(df.iloc[counter:counter+5])
        counter=counter+5
        data=input('Would you like to see some data ? (y/n) \n')
        
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df,city)
        #display 5 rows of data
        displaydata(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
    main()