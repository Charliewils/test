#include <iostream>

using namespace std;

void Bubble(int* A, int n){
	for (int i = 0; i < n-1; i++){
		for(int j = 0; j < n-i-1; j++){
			if(A[j] > A[j+1]){
				int temp = A[j];
				A[j] = A[j+1];
				A[j+1] = temp;
			}
		}
	}
}

void Selection(int* A, int n){
	for (int i = 0; i < n-1; i++){
		int max_a = i;
		for (int j = i+1; j < n; j++){
			if (A[i] < A[j]) 
				max_a = j;
		}
		int temp = A[i];
		A[i] = A[max_a];
		A[max_a] = temp;
	}
}

void Print(int* A, int n){
	for (int i = 0; i < n; i++){
		cout << A[i] << " ";
	}
	cout << "" << endl;
}

void Reverse(int* A, int n){
	for (int i = 0; i < n-1; i++){
		for(int j = 0; j < n-i-1; j++){
			int temp = A[j];
			A[j] = A[j+1];
			A[j+1] = temp;
		}
	}
}

int main(){
	int A[5] = {9, 16, 15, 4, 2};
	Print(A, 5);
	Bubble(A, 5);
	Print(A, 5);
	Selection(A, 5);
	Print(A, 5);
	Reverse(A, 5);
	Print(A, 5);
	return 0;
}




