#include "BaseAlgorithm.h"

#include <iostream>
#include <chrono>

using namespace std;

BaseAlgorithm::PerfTimer::PerfTimer()
{
#if _DEBUG
    mStart = chrono::steady_clock::now();
#endif
}

BaseAlgorithm::PerfTimer::~PerfTimer()
{
#if _DEBUG
    auto diff = chrono::steady_clock::now() - mStart;
    cout << "Elapsed time = " << chrono::duration_cast<chrono::nanoseconds>(diff).count() << " nanoseconds" << endl;
    cout << "          or , " << chrono::duration_cast<chrono::microseconds>(diff).count() << " microseconds" << endl;
    cout << "          or , " << chrono::duration_cast<chrono::milliseconds>(diff).count() << " milliseconds" << endl;
    cout << "          or , " << chrono::duration_cast<chrono::seconds>(diff).count() << " seconds" << endl;
#endif
}