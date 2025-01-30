#include <iostream>
#include <thread>
#include <atomic>
#include <mutex>
#include <condition_variable>

std::atomic<int> counter(0); 
std::mutex mtx;             
std::condition_variable cv; 

void increment() {
    for (int i = 0; i < 10000; ++i) {
        std::unique_lock<std::mutex> lock(mtx); 
        counter++;                             
        cv.notify_one();                       
    }
}

void decrement() {
    for (int i = 0; i < 10000; ++i) {
        std::unique_lock<std::mutex> lock(mtx); 
        counter--;                             
        cv.notify_one();                       
    }
}

int main() {
    std::thread t1(increment); 
    std::thread t2(decrement); 

    t1.join(); 
    t2.join(); 

    std::cout << "Final Counter Value: " << counter.load() << std::endl; 
    return 0;
}
