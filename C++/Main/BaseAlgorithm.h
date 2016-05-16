#pragma once

#include <chrono>

class BaseAlgorithm
{
public:
	BaseAlgorithm() {};
	~BaseAlgorithm() {};

    class PerfTimer {
    public:
        PerfTimer();
        ~PerfTimer();
    private:
        std::chrono::system_clock::time_point mStart;
    };

public:
    // run the algorithm
    virtual void run() = 0;
};

