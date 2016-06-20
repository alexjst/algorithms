/* Google Interview Question:

An abbreviation of a word follows the form <first letter><number><last letter>. Below are some examples of word abbreviations:

a) it                      --> it    (no abbreviation)

1
b) d|o|g                   --> d1g

1    1  1
1---5----0----5--8
c) i|nternationalizatio|n  --> i18n

1
1---5----0
d) l|ocalizatio|n          --> l10n

Assume you have a dictionary and given a word, find whether its abbreviation is unique in the dictionary. A word's abbreviation is unique if no other word from the dictionary has the same abbreviation.

Example:

Given dictionary = [ "deer", "door", "cake", "card" ]

isUnique("dear") -> false
isUnique("cart") -> true
isUnique("cane") -> false
isUnique("make") -> true

*/
#include "UniqueWordAbbreviation.h"
#include <string>
#include <vector>
#include <set>
#include <map>
#include <iostream>

using namespace std;

class ValidWordAbbr {
public:
    ValidWordAbbr(vector<string> &dictionary) {
        for (string word : dictionary) { // range-based for loop
            string abbr = word.length()>2 ? (word.substr(0, 1) + to_string(word.length() - 2) + word[word.length() - 1]) : word;
            abbrDict[abbr].insert(word);
        }
    }

    bool isUnique(string word) {
        string abbr = word.length()>2 ? (word.substr(0, 1) + to_string(word.length() - 2) + word[word.length() - 1]) : word;
        auto it = abbrDict.find(abbr);
        if (it == abbrDict.end()) // not found
            return true;
        else {
            if (it->second.size() == 1 && it->second.find(word) != it->second.end()) return true;
            else return false;
        }
    }
private:
    map<string, set<string>> abbrDict;
};

void UniqueWordAbbreviation::run()
{
    vector<string> dict = { "deer", "door", "cake", "card" };
    ValidWordAbbr vwa(dict);
    cout << vwa.isUnique("deer") << vwa.isUnique("cart") << vwa.isUnique("cane") << vwa.isUnique("make");
}