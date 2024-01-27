#include <bits/stdc++.h>
using namespace std;
int main(){
	int n;
	cin >> n;
	while(n--){
		int m;
		cin >> m;
		map<int , int > mp;
		for(int i = 0 ; i < m ; i++){
			int x;
			cin >> x;
			mp[x]++;
		}
		map<int , int> :: iterator it;
		bool is = false;
		for(it = mp.begin() ; it != mp.end() ; it++){
			if(it->second >= 3){
				cout << it->first<<"\n";
				is =true;
				break;
			}
		}
		if(!is){
			cout << "-1"<<"\n";
		}
	}
	return 0;
}