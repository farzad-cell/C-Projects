#include<iostream>
#include<random>

using namespace std;
int main() {
    char player, player1;


    cout<<"Welcome to Flip A Coin.Exit input (Q/q).\nPick ONLY one MODE (Y/y or N/n) \nCompetitive mode   --> Y or y\nFlip a coin        --> N or n"<<endl;

    while(true) {
        cin>>player;

        if(player == 'q' || player == 'Q') {
            break;
        }

            random_device rd;
            mt19937_64 rnd(rd());
            uniform_int_distribution<int> dist(0,1);
            int fc = dist(rnd);



            if(player == 'Y' || player == 'y') {
                cout<< "H/h - Heads\nT/t - Tails" <<endl;


                cin>>player1;

                if(player1 == 'H' || player1 == 'h' || player1 == 'T' || player1 == 't') {
                    if (player1 == 'H' || player1 == 'h') {
                        cout<<"You: Heads"<<endl;
                    }else if (player1 =='T' || player1 == 't') {
                        cout<<"You: Tails"<<endl;
                    }else
                        cout<<"Invalid input! | Chose only one H/h or T/t"<<endl;

                    if(fc == 0) {
                        cout<<"Coin Flip*\nHeads"<<endl;
                    }else if (fc == 1){
                        cout<<"Coin Flip*\nTails"<<endl;
                    }
                }
            }else if(!(player == 'Y' || player == 'y' || player == 'N' || player == 'n')) {
                cout<<"Invalid input! | Chose only one Y,y or N,n"<<endl;
                continue;
            }


            if(player == 'n' || player == 'N') {

            cout<<"FC: ";
            if(fc == 1) {
                cout<<"Tails"<<endl;
            }else if (fc == 0){
                cout<<"Heads"<<endl;
            }
        }
        }
    }
