#include<bits/stdc++.h>
using namespace std;

int main()
{
    int RATE=50;
    int CAPACITY=100;
    int tokens=0;
    int secs = 10;
    for(int i=0; i<secs; i++) {
        this_thread::sleep_for(chrono::seconds(1));
        tokens+=RATE;
        if(tokens>CAPACITY){
            tokens=CAPACITY;
        }
        int tokens_needed=60;
        if(tokens>=tokens_needed){
            tokens -= tokens_needed;
            cout<<"Performed operations remaining tokens:"<<tokens<<endl;
        }
        else cout<<"Not enoigh tokens needed to wait"<<endl;
    }
    return 0;
}
