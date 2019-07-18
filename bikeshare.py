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
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        try:
            '''The lower() method returns the lowercased string from the given string'''
            city=input("Which city's data you would like to explore, chicago, new york city, or washington?\n").lower()
            if city not in ('chicago','new york city','washington'):
                print('You have entered wrong city, please enter correct city name')
                continue
            else:
                break
        except ValueError as error:
            print(f'Exception occured :{error}')

    # TO DO: get user input for month (all, january, february, ... , june)
    months=['all','january','february','march','april','may','june']
    while True:
        try:
            month=input("Would you like to filter data by month. For example, All, January, February...June\n").lower()
            if month not in months:
                print('You have entered wrong month, please enter correct month')
                continue
            else:
                break
        except ValueError as error:
            print(f'Exception occured :{error}')
    
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    days=['all','monday','tuesday','wednesday','thursday','friday','saturday','sunday']
    while True:
        try:
            day=input("Would you like to filter data by day. For example, All, Monday,Tuesday...Sunday\n").lower()
            if day not in days:
                print('You have entered wrong day, please enter correct day')
                continue
            else:
                break
        except ValueError as error:
            print(f'Exception occured :{error}')


    print('-'*40)
    print (city,month,day)
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
    # read_csv: Read a comma-separated values (csv) file into DataFrame
       
    df=pd.read_csv(CITY_DATA[city])
        
    ''' Convert argument to datetime. Pandas to_datetime() method helps to convert string Date time into Python Date time object.'''
    
    df['Start Time']=pd.to_datetime(df['Start Time'])
    
    # Added new column month by extracting month from Start Time
    
    df['month']=df['Start Time'].dt.month
         
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
        print(month)
    # filter by month to create the new dataframe
        df = df[df['month'] == month]    
    
    #Added new column Week day by extracting Weekday from Start Time
    
    df['day']=df['Start Time'].dt.weekday_name
    
    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day'] == day.title()]
    
    
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    

    # TO DO: display the most common month
    # The mode of a set of values is the value that appears most often. It can be multiple values.
    common_month=df['month'].mode()[0]
    print (f'most common month is: {common_month}')
   
    # TO DO: display the most common day of week
    common_day= df['day'].mode()[0]
    print (f'most common day is: {common_day}')

    # TO DO: display the most common start hour
    #Added new column hour by extracting hour from Start Time
    df['hour']=df['Start Time'].dt.hour
    common_hour=df['hour'].mode()[0]
    print (f'most popular start hour is: {common_hour}')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    '''The mode of a set of values is the value that appears most often.
    Value_count: Return a Series containing counts of unique values.The resulting object will be in descending order
    so that the first element is the most frequently-occurring element. Excludes NA values by default.
    max():Return the maximum of the values for the requested axis.'''
    common_start_station=df['Start Station'].mode()[0]
    common_start_station_count=df['Start Station'].value_counts().max()
    print (f'most popular start station is {common_start_station}, count is:{common_start_station_count}')

    # TO DO: display most commonly used end station
    common_end_station=df['End Station'].mode()[0]
    end_station_count= df['End Station'].value_counts().max()
    print (f'most popular end station is {common_end_station}, count is:{end_station_count}')


    # TO DO: display most frequent combination of start station and end station trip
    '''display most frequent combination of start station and end station trip converting dtypes to string using astype
        Generate descriptive statistics.For numeric data, the result’s index will include count, mean, std, min, max as well as lower, 50 and upper percentiles.
        By default the lower percentile is 25 and the upper percentile is 75. The 50 percentile is the same as the median.For object data (e.g. strings or timestamps)
        , the result’s index will include count, unique, top, and freq.The top is the most common value. The freq is the most common value’s frequency.
        Timestamps also include the first and last items.Describing a round_trip '''
    round_trip= df['Start Station'].astype(str)+' to '+ df['End Station'].astype(str)
    round_trip_describe = round_trip.describe()
    round_trip_top=round_trip_describe['top']
    round_trip_count= round_trip_describe['freq']
    print(f'frequent trips are from: {round_trip_top}, count is:{round_trip_count}')
           
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time. SUM(): return the sum of the values for the requested axis
    print('total travel time is: ',df['Trip Duration'].sum())
    
    # TO DO: display mean travel time. MEAN():Return the mean of the values for the requested axis.
    print('average travel time is: ',df['Trip Duration'].mean())

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    try:
        user_types=df['User Type'].value_counts()
        print(f'user types are: \n{user_types}')
    except KeyError as error:
            print('no user types data to share')
    
    # TO DO: Display counts of gender
    try:
        gender =df['Gender'].value_counts()
        print(f'gender counts are: \n{gender}')
    except KeyError as error:
            print('no gender data to share')


    # TO DO: Display earliest, most recent, and most common year of birth
    try:
        earliest_year=df['Birth Year'].min()
        print(f'earlier year is: {earliest_year}')
        recent_year=df['Birth Year'].max()
        print(f'most recent year is: {recent_year}')
        common_year=df['Birth Year'].mode()[0]
        print(f'common year is: {common_year}')
    except KeyError as error:
        print('no birth year data to share')



    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    
def rawdata_display(df):
    '''This function will print 5 rows of data when user answers yes and continue these prompts and displays until the user says 'no'. 
    Find out the range (no of loops) by dividing length of the file by 5 (no of records we want to see each time).
    If reminder is 0 means no of rows are multiple of 5, if reminder is not equal to zero, then we have to loop again to see data till end of file.
    iloc is integer index based, so we have to specify rows and columns by their integer index. Here I am providing row index and selecting all coloumns. '''
    
    rawdata=input ('Would you like to see raw data? Please enter yes or no \n').lower()
    incr = 5
    reminder = len(df)%incr
    if reminder ==0:
        k=int(len(df)/incr)
    else:
        k=int(len(df)/incr)+1
    if rawdata=='yes':
        for i in range (0,k):
            if (i*incr)+incr<=len(df):
                print(df.iloc[i*incr:(i*incr)+incr,:])
            else:
                print(df.iloc[i*incr:len(df)+1,:])
            more_data=input('Do you want to see more data? Please enter yes or no\n').lower()
            if more_data !='yes':
                break
        


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        rawdata_display(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
