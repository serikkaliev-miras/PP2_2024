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
