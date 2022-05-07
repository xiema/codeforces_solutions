#include <bits/stdc++.h>
using namespace std;

int t, n, o, e, a, b;

int main() {
  cin >> t;
  while (t--) {
    cin >> n;

    cin >> a;
    o = a % 2;
    cin >> a;
    e = a % 2;

    b = true;
    for (int i = 3; i <= n; ++i){
      cin >> a;
      if (a % 2 != (i % 2 ? o : e)) {
        b = false;
      }
    }

    cout << (b ? "YES\n" : "NO\n");
  }
}
