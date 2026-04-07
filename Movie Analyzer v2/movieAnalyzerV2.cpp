#include <iostream>

struct movieData{
    std::string title;
    std::string director;
    int year;
    float duration; 
};

// Prototypes
movieData getData();
void printMovie(movieData &movie1);

int main() {
    
    std::cout << "Welcome to movie analyzer v2\n" 
              << "============================================\n";

    movieData movie1;
    movie1 = getData();
    printMovie(movie1);
    return 0;
}

movieData getData(){

    movieData movie1;

    while(true){

        std::cout << "Enter the title: ";
        std::getline(std::cin, movie1.title);
        std::cout << "\n";

        std::cout << "Enter the director: ";
        std::getline(std::cin, movie1.director);
        std::cout << "\n";

        do{
            std::cout << "Enter the year: ";
            std::cin >> movie1.year;
            std::cout << "\n";

            if(movie1.year < 1920 || movie1.year > 2026){
                std::cout << "Enter valid year (1920-2026)\n";
            }

        }while(movie1.year < 1920 || movie1.year > 2026);
        
        do{
            std::cout << "Enter the duration: ";
            std::cin >> movie1.duration;
            std::cout << "\n";

            if(movie1.duration < 60){
                std::cout << "Enter valid duration (min >= 60)\n";
            }

        }while(movie1.duration < 60);
        break;
    }
    return movie1;
}

void printMovie(movieData &movie1){

    std::cout << "\nMOVIE1 DATA\n" 
            << "============================================\n"
            << "Movie Title: " << movie1.title << "\n"
            << "Director: " << movie1.director << "\n"
            << "Release year: " << movie1.year << "\n"
            << "Duration: " << movie1.duration << "\n"
            << "============================================\n\n";
}