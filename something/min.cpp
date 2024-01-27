/*#include <bits/stdc++.h>
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
		
		for(int i = 0 ; i < m ; i++){
		vector <int> :: iterator it;
		for(it = vec.begin(); it != vec.end() ; it++){
			it = min_element(vec.begin() , vec.end());
			cout << *it<<"\n";
		}
	}
	}
	return 0;
}*/

#include <bits/stdc++.h>
using namespace std;
int main() {
    int n;
    cin >> n;
	int sum = 0;
    while (n--) {
        int m;
        cin >> m;
        vector<int> vec;
        for (int i = 0; i < m; i++) {
            int x;
            cin >> x;
            vec.push_back(x);
        }
        int it = *min_element(vec.begin(), vec.end());
		for (int i = 0; i < m; i++){
					sum += (vec[i] - it);
				}
				cout << sum << "\n";
	}
    return 0;
}
