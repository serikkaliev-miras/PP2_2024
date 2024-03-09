// 1 varik   task 10
#include <bits/stdc++.h>
using namespace std;
bool Perfect(int num) {
    int sumOfDivisors = 1;
    for (int i = 2; i * i <= num; ++i) {
        if (num % i == 0) {
            sumOfDivisors += i;
            if (i != num / i) {
                sumOfDivisors += num / i;
            }
        }
    }
    return sumOfDivisors == num;
}
void findPerfectNumbers(int n) {
    for (int num = 2; num <= n; ++num) {
        if (isPerfect(num)) {
            cout << num <<" ";
        }
    }
}
int main() {
    int n;
    cin >> n;
    findPerfectNumbers(n);
    return 0;
}
