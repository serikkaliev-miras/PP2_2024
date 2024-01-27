#include <bits/stdc++.h>
using namespace std;
int main(){
	int n;
	cin >> n;
	while(n--){
		int m;
		cin >> m;
		vector<int> vec;
		for(int i = 0 ; i < m ; i++){
			int x;
			cin >> x;
			vec.push_back(x);
		}
		int left = 0 , right = n - 1;
		int sum1 = 0 , sum2 = 0;
		int all = 0;
		int i1 = 0 , i2 = 0;
		while(left <= right){
			if(sum1 <= sum2){
				sum1 += vec[left];
				left++;
				i1++;
				all += i1;
			}else{
				sum2 += vec[right];
				right--;
				i2++;
				all += i2;
			}
			if(sum1 == sum2){
			   cout << all;
			}
		}
			//cout << all<<endl;
	}
	return 0;
}