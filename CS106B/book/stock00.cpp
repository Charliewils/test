#include <iostream>
#include "stock00.h"

void Stock::acquire(const std::string & co, long n, double pr){
	company = co;
	if (n < 0){
		std::cout << "Number of shares can't be negative." << std::endl;
		shares = 0;
	}
	else shares = n;
	share_val = pr;
	set_tol();
}

int main(){
	Stock X;
	X.acquire("NonSmart", 20, 12.50);
	return 0;
}
