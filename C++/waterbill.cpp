// This program calculates 4 quarters of bill.
//Then finds the average monthly bill.

// Created by Farzad Darwazi 09/11/25

#include <iostream>


using namespace std;

int main()
{
	// Variables
	float bill1, bill2, bill3, bill4;
	float ave_bill;

	// Begining statements and inputs
	cout << "Please input your water bill for quarter 1: " << endl;
	cin >> bill1;

	cout << "Please input your water bill for quarter 2: " << endl;
	cin >> bill2;

	cout << "Please input your water bill for quarter 3: " << endl;
	cin >> bill3;

	cout << "Please input your water bill for quarter 4: " << endl;
	cin >> bill4;

	// Calculation for the average
	ave_bill = (bill1 + bill2 + bill3 + bill4) / 4;

	// Ending statement
	cout << "Your average monthly bill is $" << ave_bill;

	// Logic statements
	if(ave_bill >= 75) {
		cout << " Water usage is over budget.";
	} else if(ave_bill >= 25 && ave_bill < 75) {
		cout << " Water usage is on budget.";
	} else
		cout << " Congrats! Your water usage is under budget.";
}
