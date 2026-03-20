// Create a date of the form DDDYYYY (day of year, year)
// from a Date.

#include <iostream>


struct Date{
    short Month;
    short Day;
    short Year;
};

/*
Although arguments passed as reference types observe the syntax of non-pointer types, 
they retain one important characteristic of pointer types: they are modifiable unless declared as const.
Because the intent of the preceding code is not to modify the object date, a more appropriate function prototype is: const Date& date
*/
std::string DateofYear(const Date& date){

    static int daysInMonth[] = {
        31, 28, 30, 31, 30, 31, 30, 31, 30, 31, 30, 31
    };

    long dateofyear = 0; 

    // Add in days for months already elapsed.
    for(int i = 0; i < date.Month - 1; i++){
        dateofyear += daysInMonth[i];
    }

    // Add in days for this month.
    dateofyear += date.Day; 

    // Check for leap year.
    if ( date.Month > 2 && (( date.Year % 100 != 0 || date.Year % 400 == 0 ) && date.Year % 4 == 0 )) dateofyear++;


    // Add in year.
    dateofyear *= 10000;
    dateofyear += date.Year; 

    // add in '/' after the day and month:
    std::string new_date = std::to_string(date.Day) + "/" + std::to_string(date.Month) + "/" + std::to_string(date.Year);  
    
    return new_date;
}

int main(){

    Date date{ 8, 27, 2026};
    std::string dateOfYear = DateofYear(date);

    std::cout<< dateOfYear << std::endl; 
}